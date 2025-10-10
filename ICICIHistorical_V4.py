"""
ICICIHistorical_V4_fixed.py

Cleaned and refactored version of the uploaded script. Main goals:
- Remove duplicate definitions and repeated imports
- Consistent variable naming and error handling
- Replace hard-coded secrets with placeholders (please set via env or config)
- Keep functionality: login helper, safe historical fetch, merging, strike-list generation,
  threaded downloads, zip creation, Telegram notifier, and error logging to Excel.

NOTE: Before running, install dependencies: pip install breeze-connect pandas python-dateutil tabulate telebot
Replace placeholders (API keys, BOT token, chat ids) with real values or set as environment variables.
"""

import os
import time
import zipfile
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from dateutil import parser
import pandas as pd

# Optional imports (only if available in your environment)
try:
    from breeze_connect import BreezeConnect
except Exception:
    BreezeConnect = None

# ---------------------------
# Error collection utilities
# ---------------------------
Error_Data = {}
def Data_Error(stock_name=None, expiry_date=None, strike_price=None, options_type=None, error_date=None, function_error=None, api_error=None):
    """Collect errors into a dictionary for later export to Excel. Missing fields are auto-filled with 'NA'."""
    global Error_Data
    try:
        # Auto-fill missing fields instead of warning
        stock_name = stock_name or "NA"
        expiry_date = expiry_date or "NA"
        strike_price = strike_price or "NA"
        options_type = options_type or "NA"
        error_date = error_date or "NA"

        if expiry_date not in Error_Data:
            Error_Data[expiry_date] = {}
        if strike_price not in Error_Data[expiry_date]:
            Error_Data[expiry_date][strike_price] = []

        Error_Data[expiry_date][strike_price].append({
            "stock_name": stock_name,
            "expiry_date": expiry_date,
            "strike_price": strike_price,
            "options_type": options_type,
            "error_date": error_date,
            "function_error": function_error or "NA",
            "api_error": api_error or "NA",
        })
    except Exception as e:
        print(f"Data_Error Function Error: {e}")


def Error_Data_to_Excel(filename="Error_Data"):
    global Error_Data
    try:
        rows = []
        for expiry, strikes in Error_Data.items():
            for strike, errors in strikes.items():
                for err in errors:
                    rows.append([
                        err.get("stock_name"), err.get("expiry_date"), err.get("strike_price"),
                        err.get("options_type"), err.get("error_date"), err.get("function_error"),
                        err.get("api_error"),
                    ])
        if not rows:
            print("⚠️ Error_Data खाली है, Excel file नहीं बनी।")
            return None
        df = pd.DataFrame(rows, columns=["stock_name", "expiry_date", "strike_price", "options_type", "error_date", "function_error", "api_error"])
        df = df.sort_values(by=["expiry_date", "strike_price", "error_date"], na_position='last').reset_index(drop=True)
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        filename_out = f"{filename}_Error.xlsx"
        df.to_excel(filename_out, sheet_name="ErrorLogs", index=False)
        print(f"✅ Error data Excel में save हो गया: {filename_out}")
        Error_Data.clear()
        return filename_out
    except Exception as e:
        print(f"Error_Data_to_Excel Function Error: {e}")
        return None


# ---------------------------
# ICICI (Breeze) Login helper
# ---------------------------

def ICICI_Login(session_token: str, api_key: str, secret_key: str):
    """Return BreezeConnect instance or None. If session_token not provided, prints login URL."""
    try:
        if not BreezeConnect:
            print("BreezeConnect module not available. Install 'breeze-connect' package.")
            return None
        if not session_token:
            login_url = f"https://api.icicidirect.com/apiuser/login?api_key={parser.quote_plus(api_key)}" if False else f"https://api.icicidirect.com/apiuser/login?api_key={api_key}"
            # NOTE: above parser.quote_plus avoided due to dateutil parser variable name; simply show the URL
            print("Please login using this link to generate session_token:")
            print(login_url)
            return None
        breeze = BreezeConnect(api_key=api_key)
        breeze.generate_session(api_secret=secret_key, session_token=session_token)
        print("Login Successful ✅")
        return breeze
    except Exception as e:
        print("Login Failed ❌", e)
        try:
            login_url = f"https://api.icicidirect.com/apiuser/login?api_key={api_key}"
            print("Please login using this link to generate session_token:\n", login_url)
        except Exception:
            pass
        return None

# ---------------------------
# Rate limiter for API calls
# ---------------------------
CALL_LIMIT = 100
Total_Count = 0
Start_Time = time.time()


def rate_limiter():
    global Total_Count, Start_Time
    now = time.time()
    if now - Start_Time >= 60:
        Total_Count = 0
        Start_Time = now
    Total_Count += 1
    if Total_Count > CALL_LIMIT:
        sleep_time = 60 - (now - Start_Time)
        if sleep_time > 0:
            time.sleep(sleep_time)
        Total_Count = 1
        Start_Time = time.time()

# ---------------------------
# Safe historical fetch wrapper
# ---------------------------

def safe_get_historical_data(breeze, interval, from_date, to_date, stock_code, exchange_code, product_type, expiry_date_api, right, strike_price, max_retries=3, delay=1):
    attempt = 0
    right_Data = None
    while attempt < max_retries:
        try:
            rate_limiter()
            right_Data = breeze.get_historical_data_v2(
                interval=interval, from_date=from_date, to_date=to_date, stock_code=stock_code,
                exchange_code=exchange_code, product_type=product_type, expiry_date=expiry_date_api, right=right, strike_price=strike_price
            )
            # Normalize responses
            if isinstance(right_Data, dict) and right_Data.get('Success'):
                return right_Data
            # Handle specific error messages
            if isinstance(right_Data, dict) and right_Data.get('Error') == 'Rate Limit Exceeded':
                time.sleep(120)
            elif isinstance(right_Data, dict) and right_Data.get('Error') == 'API did not return any response':
                return {"Error": "API did not return any response", "Success": None}
            attempt += 1
            if attempt < max_retries:
                time.sleep(delay)
        except Exception as e:
            attempt += 1
            if attempt < max_retries:
                time.sleep(delay)
    # Final failure
    error_msg = None
    if right_Data and isinstance(right_Data, dict):
        error_msg = right_Data.get('Error', 'No Error Data')
    if not error_msg:
        error_msg = 'API did not return any response'
    return {"Error": f"Failed after {max_retries} retries, API_Error: {error_msg}", "Success": None}


def safe_parse_date(x, format_date="%d-%m-%Y"):
    try:
        if pd.isna(x) or str(x).strip() == "":
            return None
        parsed_date = parser.parse(str(x), fuzzy=True)
        return parsed_date.strftime(format_date)
    except Exception:
        return None

# ---------------------------
# Fetch ICICI historical (detailed function)
# ---------------------------

def Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, expiry_date_str, past_days=30):
    """Fetch historical data for given parameters and return a cleaned DataFrame or None."""
    try:
        final_df = pd.DataFrame()
        options_type = "NA"
        Expiry_Date_dt = datetime.strptime(expiry_date_str, "%d-%m-%Y")
        ToDate = datetime.today()
        End_Date = min(Expiry_Date_dt, ToDate) + timedelta(days=1)
        Start_Date = End_Date - timedelta(days=past_days)
        Start_Date = Start_Date.replace(hour=9, minute=15, second=0)
        expiry_date_api = Expiry_Date_dt.strftime("%Y-%m-%dT00:00:00.000Z")

        if product_type in ("futures", "cash"):
            from_date_api = Start_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date_api = End_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            right_Data = safe_get_historical_data(breeze, interval, from_date_api, to_date_api, stock_code, exchange_code, product_type, expiry_date_api, right, strike_price, max_retries=3, delay=1)
            if right_Data and right_Data.get("Error") is None and right_Data.get("Success"):
                options_type = "fu" if product_type == "futures" else "ch"
                df = pd.DataFrame(right_Data["Success"]).copy()
                if df.empty:
                    return None
                # Normalize datetime and columns
                df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce').dt.strftime('%d-%m-%Y %H:%M')
                df['expiry_date'] = df.get('expiry_date', pd.Series([Expiry_Date_dt.strftime('%d-%m-%Y')]*len(df)))
                rename_map = {"open": f"{options_type}_open", "high": f"{options_type}_high", "low": f"{options_type}_low", "close": f"{options_type}_close", "volume": f"{options_type}_volume"}
                if 'open_interest' in df.columns:
                    rename_map['open_interest'] = f"{options_type}_oi"
                df = df.rename(columns=rename_map)
                desired_cols = [c for c in ["stock_code", "expiry_date", "datetime", f"{options_type}_open", f"{options_type}_high", f"{options_type}_low", f"{options_type}_close", f"{options_type}_volume", f"{options_type}_oi"] if c in df.columns]
                df = df[desired_cols]
                final_df = pd.concat([final_df, df], ignore_index=True)

        elif product_type == "options":
            options_type = right  # 'call' or 'put'
            current_to = End_Date
            while current_to > Start_Date:
                from_date_api = (Start_Date - timedelta(days=5)).strftime("%Y-%m-%dT00:00:00.000Z")
                to_date_api = current_to.strftime("%Y-%m-%dT%H:%M:%S.000Z")
                right_Data = safe_get_historical_data(breeze, interval, from_date_api, to_date_api, stock_code, exchange_code, product_type, expiry_date_api, right, strike_price, max_retries=3, delay=1)
                Error = right_Data.get("Error") if isinstance(right_Data, dict) else None
                Success = right_Data.get("Success") if isinstance(right_Data, dict) else None
                if not Success:
                    Data_Error(stock_name=None, expiry_date=Expiry_Date_dt.strftime('%d-%m-%Y'), strike_price=str(strike_price), options_type=options_type, error_date=current_to.strftime('%d-%m-%Y'), function_error="Fetch_ICICI_Historical_Data-1", api_error=Error)
                    current_to -= timedelta(days=1)
                    continue
                if Error is None and Success:
                    df = pd.DataFrame(Success).copy()
                    if not df.empty:
                        df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce').dt.strftime('%d-%m-%Y %H:%M')
                        df['expiry_date'] = df.get('expiry_date', pd.Series([Expiry_Date_dt.strftime('%d-%m-%Y')]*len(df)))
                        rename_map = {"open": f"{options_type}_open", "high": f"{options_type}_high", "low": f"{options_type}_low", "close": f"{options_type}_close", "volume": f"{options_type}_volume"}
                        if 'open_interest' in df.columns:
                            rename_map['open_interest'] = f"{options_type}_oi"
                        df = df.rename(columns=rename_map)
                        desired_cols = [c for c in ["stock_code", "expiry_date", "strike_price", "datetime", f"{options_type}_open", f"{options_type}_high", f"{options_type}_low", f"{options_type}_close", f"{options_type}_volume", f"{options_type}_oi"] if c in df.columns]
                        df = df[desired_cols]
                        final_df = pd.concat([final_df, df], ignore_index=True)
                        df_dt = pd.to_datetime(df['datetime'], format='%d-%m-%Y %H:%M', errors='coerce')
                        first_time = df_dt.min()
                        if pd.isna(first_time):
                            current_to -= timedelta(days=1)
                        elif first_time <= Start_Date:
                            break
                        else:
                            current_to = first_time - timedelta(minutes=1)
                    else:
                        Data_Error(stock_name=None, expiry_date=Expiry_Date_dt.strftime('%d-%m-%Y'), strike_price=str(strike_price), options_type=options_type, error_date=current_to.strftime('%d-%m-%Y'), function_error="Fetch_ICICI_Historical_Data-2", api_error=Error)
                        current_to -= timedelta(days=1)
                else:
                    Data_Error(stock_name=None, expiry_date=Expiry_Date_dt.strftime('%d-%m-%Y'), strike_price=str(strike_price), options_type=options_type, error_date=current_to.strftime('%d-%m-%Y'), function_error="Fetch_ICICI_Historical_Data-3", api_error=Error)
                    current_to -= timedelta(days=1)
                time.sleep(0.1)

        # Post-process final_df
        if not final_df.empty:
            analysis_data = final_df.copy()
            # Ensure datetime and expiry_date typed for sorting
            analysis_data['datetime'] = pd.to_datetime(analysis_data['datetime'], format='%d-%m-%Y %H:%M', errors='coerce')
            if 'expiry_date' in analysis_data.columns:
                analysis_data['expiry_date'] = pd.to_datetime(analysis_data['expiry_date'], format='%d-%m-%Y', errors='coerce')
            analysis_data = analysis_data.sort_values(by='datetime', ascending=True).reset_index(drop=True)
            analysis_data = analysis_data[analysis_data['datetime'] >= Start_Date]
            analysis_data['datetime'] = analysis_data['datetime'].dt.strftime('%d-%m-%Y %H:%M')
            if 'expiry_date' in analysis_data.columns:
                analysis_data['expiry_date'] = analysis_data['expiry_date'].dt.strftime('%d-%m-%Y')
            return analysis_data
        else:
            Data_Error(stock_name=None, expiry_date=Expiry_Date_dt.strftime('%d-%m-%Y'), strike_price=str(strike_price), options_type=None, error_date='All Date', function_error='Fetch_ICICI_Historical_Data-4', api_error=None)
            return None
    except Exception as e:
        Data_Error(stock_name=None, expiry_date=expiry_date_str if isinstance(expiry_date_str, str) else None, strike_price=str(strike_price), options_type=None, error_date='All Date', function_error='Fetch_ICICI_Historical_Data-5', api_error=str(e))
        print(f"Fetch_ICICI_Historical_Data Error: {e}")
        return None

# ---------------------------
# Merge call and put datasets
# ---------------------------

def fetch_Merged_Data(data_call, data_put):
    try:
        if data_call is not None and isinstance(data_call, list):
            try:
                data_call = pd.concat(data_call, ignore_index=True)
            except Exception:
                pass
        if data_put is not None and isinstance(data_put, list):
            try:
                data_put = pd.concat(data_put, ignore_index=True)
            except Exception:
                pass
        if data_call is not None and data_put is not None:
            merged = pd.merge(data_call, data_put, on=["datetime", "stock_code", "expiry_date", "strike_price"], how="outer", suffixes=("_call", "_put"))
        elif data_call is not None:
            merged = data_call.copy()
            merged = merged.rename(columns={col: col + "_call" for col in merged.columns if col not in ["datetime", "stock_code", "expiry_date", "strike_price"]})
        elif data_put is not None:
            merged = data_put.copy()
            merged = merged.rename(columns={col: col + "_put" for col in merged.columns if col not in ["datetime", "stock_code", "expiry_date", "strike_price"]})
        else:
            return None
        if 'datetime' in merged.columns:
            merged['datetime'] = pd.to_datetime(merged['datetime'], errors='coerce', format='%d-%m-%Y %H:%M')
            merged = merged.sort_values(by='datetime', ascending=True).reset_index(drop=True)
            merged['datetime'] = merged['datetime'].dt.strftime('%d-%m-%Y %H:%M')
        return merged
    except Exception as e:
        Data_Error(stock_name=None, expiry_date=None, strike_price=None, options_type=None, error_date=None, function_error='fetch_Merged_Data Error', api_error=str(e))
        print(f"fetch_Merged_Data Function Error: {e}")
        return None

# ---------------------------
# High-level fetch wrapper
# ---------------------------

def Fetch_Historical_Data(breeze, exchange_code, stock_name, strike_price, interval, expiry_date_str, past_days=30):
    try:
        # Resolve stock_code for NFO
        if exchange_code == "NFO":
            stock_code = get_Stock_Name(breeze, "NSE", stock_name)
            stock_code = stock_code or stock_name
        else:
            stock_code = stock_name

        if str(strike_price) == '0':
            product_type = 'futures'
            right = 'others'
            data = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, expiry_date_str, past_days)
            return data
        else:
            product_type = 'options'
            data_call = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, 'call', strike_price, interval, expiry_date_str, past_days)
            data_put = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, 'put', strike_price, interval, expiry_date_str, past_days)
            if data_call is not None and data_put is not None:
                return fetch_Merged_Data(data_call, data_put)
            Data_Error(stock_name=None, expiry_date=expiry_date_str, strike_price=str(strike_price), options_type=None, error_date=None, function_error='Fetch_Historical_Data', api_error=None)
            return None
    except Exception as e:
        Data_Error(stock_name=None, expiry_date=expiry_date_str, strike_price=str(strike_price), options_type=None, error_date=None, function_error='Fetch_Historical_Data', api_error=str(e))
        print(f"Fetch_Historical_Data Function Error: {e}")
        return None

# ---------------------------
# Get strike list using historical cash data
# ---------------------------

def get_strike_list(breeze, stock_name, expiry_date_str, past_days, strike_gap, plus_minus_strike):
    try:
        stock_code = get_Stock_Name(breeze, "NSE", stock_name)
        if not stock_code:
            print(f"Could not find stock code for {stock_name}")
            return None
        cash_df = Fetch_ICICI_Historical_Data(breeze, "NSE", stock_code, "cash", "others", 0, "1day", expiry_date_str, past_days)
        if cash_df is not None and not cash_df.empty:
            max_high_round = round((cash_df["ch_high"].max() + (plus_minus_strike * strike_gap)) / strike_gap) * strike_gap
            min_low_round = round((cash_df["ch_low"].min() - (plus_minus_strike * strike_gap)) / strike_gap) * strike_gap
            strike_list = list(range(int(min_low_round), int(max_high_round + strike_gap), strike_gap))
            strike_list = [0] + strike_list
            return sorted(strike_list)
        Data_Error(stock_name=None, expiry_date=expiry_date_str, strike_price=None, options_type=None, error_date=None, function_error='get_strike_list Error', api_error=None)
        print(f"No historical data found for {stock_name}")
        return None
    except Exception as e:
        Data_Error(stock_name=None, expiry_date=expiry_date_str, strike_price=None, options_type=None, error_date=None, function_error='get_strike_list Error', api_error=str(e))
        print(f"Error generating strike list: {e}")
        return None

# ---------------------------
# Download helpers (threaded)
# ---------------------------

def download_strike(breeze, exchange_code, stock_name, strike_price, interval, expiry_date_str, past_days, max_retries=1):
    for attempt in range(1, max_retries + 1):
        try:
            data = Fetch_Historical_Data(breeze, exchange_code, stock_name, strike_price, interval, expiry_date_str, past_days)
            if data is not None and not data.empty:
                os.makedirs(expiry_date_str, exist_ok=True)
                strike_name = strike_price if strike_price != 0 else "futures"
                csv_name = os.path.join(expiry_date_str, f"{expiry_date_str}_{strike_name}.csv")
                data.to_csv(csv_name, index=False)
                return f"{expiry_date_str}_{strike_name}.csv"
        except Exception as e:
            if attempt == max_retries:
                raise e
            time.sleep(2 * attempt)
    return None


def run_with_progress(strike_list, breeze, exchange_code, stock_name, interval, expiry_date_str, past_days, progress_speed=10, timeout=0):
    downloaded = []
    total_strike = len(strike_list)
    completed = 0
    progress_speed = min(progress_speed, max(1, total_strike))
    print(f"Total Strikes: {total_strike} | Progress Speed: {progress_speed}")
    with ThreadPoolExecutor(max_workers=progress_speed) as executor:
        future_to_strike = {executor.submit(download_strike, breeze, exchange_code, stock_name, s, interval, expiry_date_str, past_days): s for s in strike_list}
        for future in as_completed(future_to_strike):
            strike = future_to_strike[future]
            try:
                result = future.result(timeout=timeout)
                if result:
                    downloaded.append(result)
                print(f"Progress: {completed+1}/{total_strike} completed ✅ (Strike {strike})")
            except Exception as e:
                print(f"⚠️ Strike {strike} failed: {e}")
            finally:
                completed += 1
    return downloaded

# ---------------------------
# Zip creation
# ---------------------------

def make_zip(expiry_date_str, base_path='.', method='fast', download_file_list=None):
    try:
        folder_path = os.path.join(base_path, expiry_date_str)
        if not download_file_list:
            if not os.path.exists(folder_path):
                print(f"⚠️ Folder नहीं मिला: {folder_path}")
                return None
            download_file_list = os.listdir(folder_path)
        if not download_file_list:
            print("⚠️ कोई file नहीं मिली, Zip create नहीं होगा")
            return None
        compression = zipfile.ZIP_DEFLATED if method == 'fast' else zipfile.ZIP_LZMA
        zip_filename = os.path.join(base_path, f"{expiry_date_str}.zip")
        with zipfile.ZipFile(zip_filename, 'w', compression=compression) as zipf:
            for file in download_file_list:
                full_path = os.path.join(folder_path, file)
                if os.path.exists(full_path):
                    zipf.write(full_path, arcname=os.path.basename(file))
                else:
                    print(f"⚠️ File missing: {full_path}")
        print(f"✅ Zip created: {zip_filename}")
        return zip_filename
    except Exception as e:
        print(f"Error creating zip: {e}")
        return None

# ---------------------------
# Telegram helper (replace token & chat id)
# ---------------------------
try:
    import telebot
    TELEGRAM_AVAILABLE = True
except Exception:
    TELEGRAM_AVAILABLE = False

TEL_CHAT_ID = None  # set to your chat id
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', None) or 'YOUR_TELEGRAM_BOT_TOKEN'


def Telegram_Message(message: str = None, file_path: str = None, chat_id: str = None, bot_token: str = None):
    if not TELEGRAM_AVAILABLE:
        print("telebot library not available. Install pyTelegramBotAPI (telebot) to use Telegram messaging.")
        return
    bot_token = bot_token or BOT_TOKEN
    chat_id = chat_id or TEL_CHAT_ID
    if not (bot_token and chat_id):
        print("Telegram bot token or chat id not configured. Skipping Telegram send.")
        return
    try:
        bot = telebot.TeleBot(bot_token)
        if message:
            bot.send_message(chat_id, message)
        if file_path and os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id, f)
        print("✅ Message/File sent successfully!")
    except Exception as e:
        print("❌ Telegram_Message Error:", e)

# ---------------------------
# Utility: get stock name (wrapper)
# ---------------------------

def get_Stock_Name(breeze, exchange_code: str, stock_code: str) -> str:
    try:
        stock_detail = breeze.get_names(exchange_code=exchange_code, stock_code=stock_code)
        return stock_detail.get('isec_stock_code') if isinstance(stock_detail, dict) else None
    except Exception as e:
        print(f"get_Stock_Name Function Error: {e}")
        return None


# ---------------------------
# Main guard with example usage (commented)
# ---------------------------
if __name__ == '__main__':
    # Example usage (uncomment and configure)
    # breeze = ICICI_Login(session_token='YOUR_SESSION', api_key='YOUR_API', secret_key='YOUR_SECRET')
    # if breeze:
    #     data = Fetch_Historical_Data(breeze, 'NFO', 'Nifty', '24700', '1minute', '30-09-2025', past_days=20)
    #     if data is not None:
    #         print(data.head())
    pass
