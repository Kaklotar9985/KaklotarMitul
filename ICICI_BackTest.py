#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  ICICI_Login   ICICI_Login     ICICI_Login  ICICI_Login     ICICI_Login     ICICI_Login     ICICI_Login     ICICI_Login      ICICI_Login   ICICI_Login
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from breeze_connect import BreezeConnect
import urllib.parse
import pyotp
import pyotp
def get_session_token_Link(APIKEY,TOTP):
    totp = pyotp.TOTP(TOTP)
    current_otp = totp.now()
    print("Current TOTP:", current_otp)
    print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus(APIKEY))
# # Example usage
# get_session_token_Link(APIKEY,TOTP)

def ICICI_Login(session_token, APIKEY, SecretKey):
    try:
        if not session_token:
            login_url = f"https://api.icicidirect.com/apiuser/login?api_key={urllib.parse.quote_plus(APIKEY)}"
            print("Please login using this link to generate session_token:")
            print(login_url)
            return None
        breeze = BreezeConnect(api_key=APIKEY)
        breeze.generate_session(api_secret=SecretKey, session_token=session_token)
        print("Login Successful ✅")
        return breeze
    except Exception as e:
        print("Login Failed ❌")
        login_url = f"https://api.icicidirect.com/apiuser/login?api_key={urllib.parse.quote_plus(APIKEY)}"
        print("Please login using this link to generate session_token:\n",)
        print(login_url,"\n")
        return None
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Telegram_Message   Telegram_Message     Telegram_Message   Telegram_Message     Telegram_Message   Telegram_Message      Telegram_Message   Telegram_Message    Telegram_Message
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telebot
BOT_TOKEN = '7591009372:AAEkZFnOZ1UyqxQgiTSJVqKqr1uvPP5KqPI'
bot = telebot.TeleBot(BOT_TOKEN)
Tel_Candal_Data_ID  = "-1002257377003"
Tel_JB_Sons_ID      = "-1002263632329"
Tel_Jay_Mataji_ID   = '1170793375'
CHAT_ID = Tel_Jay_Mataji_ID
def Telegram_Message(*args, file_path=None):
    try:
        if args:
            message = "\n".join(filter(None, args))
            bot.send_message(CHAT_ID, message)
        if file_path:
            with open(file_path, "rb") as f:
                bot.send_document(CHAT_ID, f)
        print("✅ Message/File sent successfully!")
    except Exception as e:
        print("❌ Telegram_Message Error:", e)

# # Example usage
# Telegram_Message("HI Bhai", file_path=r"D:\ICICI_BackTest\ICICIHistorical.py")
#=======================================================================================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Data_Error   Error_Data_to_Excel     Data_Error   Error_Data_to_Excel   Data_Error   Error_Data_to_Excel     Data_Error   Error_Data_to_Excel   Data_Error   Error_Data_to_Excel
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
Error_Data = {}
def Data_Error(stock_name=None, expiry_date=None, strike_price=None, options_type=None, error_date=None, function_error=None, api_error=None):
    global Error_Data
    try:
        # Auto-fill missing fields instead of warning
        stock_name   = stock_name   or "NA"
        expiry_date  = expiry_date  or "NA"
        strike_price = strike_price or "NA"
        options_type = options_type or "NA"
        error_date   = error_date   or "NA"
        if expiry_date not in Error_Data:
            Error_Data[expiry_date] = {}
        if strike_price not in Error_Data[expiry_date]:
            Error_Data[expiry_date][strike_price] = []
        Error_Data[expiry_date][strike_price].append({ "stock_name": stock_name, "expiry_date": expiry_date, "strike_price": strike_price, "options_type": options_type,
                                                       "error_date": error_date, "function_error": function_error or "NA", "api_error": api_error or "NA", })
    except Exception as e:
        print(f"Data_Error Function Error: {e}")
def Error_Data_to_Excel(filename="Error_Data"):
    global Error_Data
    try:
        rows = []
        for expiry, strikes in Error_Data.items():
            for strike, errors in strikes.items():
                for err in errors:
                    rows.append([ err.get("stock_name"), err.get("expiry_date"), err.get("strike_price"),
                                  err.get("options_type"), err.get("error_date"), err.get("function_error"),
                                  err.get("api_error"),])
        if not rows:
            print("⚠️ Error_Data खाली है, Excel file नहीं बनी।")
            return None
        df = pd.DataFrame(rows, columns=["stock_name", "expiry_date", "strike_price", "options_type", "error_date", "function_error", "api_error"])
        df = df.sort_values(by=["expiry_date", "strike_price", "error_date"], na_position='last').reset_index(drop=True)
        # df.columns = df.columns.str.lower()
        # df_clean = df.drop_duplicates(subset=["stock_name", "expiry_date", "strike_price", "options_type", "error_date"], keep="last").reset_index(drop=True)
        # all_date_df = df_clean[df_clean["error_date"].str.strip().str.lower() == "all"]
        # groups_with_all = set(zip(all_date_df["stock_name"], all_date_df["expiry_date"], all_date_df["strike_price"], all_date_df["options_type"]))
        # df_filtered = df_clean[~(
        #     df_clean.apply(lambda x: (x["stock_name"], x["expiry_date"], x["strike_price"], x["options_type"]) in groups_with_all and str(x["error_date"]).strip().lower() != "all", axis=1)
        #     )].reset_index(drop=True)
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
# # Example usage
# Data_Error(stock_name="RELIANCE", expiry_date="2024-06-27", strike_price=2500, options_type="CE", error_date="2024-06-20", function_error="ValueError", api_error="TimeoutError")
# Error_Data_to_Excel(filename="Error_Data")
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name   get_Stock_Name
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Stock_Name(breeze, exchange_code: str, stock_code: str) -> str:
    try:
        stock_detail = breeze.get_names(exchange_code=exchange_code, stock_code=stock_code)
        isec_code = stock_detail.get('isec_stock_code', None)
        if isec_code:
            return isec_code
        else:
            raise ValueError(f"Stock Code Not Found => {stock_code}")
    except Exception as e:
        print(f"get_Stock_Name Function Error: {e}")
        return None
# # Example usage
# stock_code = get_Stock_Name(breeze, "NSE", "Reliance")
# print(stock_code)   # Output: RELIND
#=======================================================================================================================================================================

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
import pandas as pd
import time
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_API_limit   rate_limiter   get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time
CALL_LIMIT = 99       # 1 minute में maximum calls
def get_API_limit(Number_of_Calls):
    global CALL_LIMIT
    CALL_LIMIT = Number_of_Calls
Total_Count = 0
Start_Time = time.time()
def rate_limiter():
    global Total_Count, Start_Time
    now = time.time()
    if now - Start_Time >= 60:
        Total_Count = 0
        Start_Time  = now
    Total_Count += 1
    if Total_Count > CALL_LIMIT:
        sleep_time = 60 - (now - Start_Time)
        if sleep_time > 0:
            time.sleep(sleep_time)
        Total_Count = 1
        Start_Time = time.time()

# # Example usage
# for i in range(105):   # 15 बार call करेंगे
#     rate_limiter()
#     print(f"API Call {i+1} done at {time.strftime('%H:%M:%S')}")
#     time.sleep(0.005)   # हर call के बीच 0.5s का gap रखा
#=======================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_historical_data_API   get_historical_data_API   get_historical_data_API   get_historical_data_API  get_historical_data_API   get_historical_data_API  get_historical_data_API   get_historical_data_API  get_API_limit   get_historical_data_API  get_API_limit   rate_limiter
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
import pandas as pd
import time
from dateutil import parser
def safe_parse_date(x, format_date="%d-%m-%Y"):
    try:
        if pd.isna(x) or str(x).strip() == "":
            return None
        parsed_date = parser.parse(str(x), fuzzy=True)
        return parsed_date.strftime(format_date)
    except Exception:
        return None
def get_historical_data_API(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price,  max_retries=3, delay=1,stock_name="No"):
    attempt = 0
    right_Data = None
    while attempt < max_retries:
        try:
            rate_limiter()  # ✅ Rate limit check
            Start_Date      = (Start_Date - timedelta(days=5))
            End_Date        = (End_Date + timedelta(days=1))
            from_date_api   = Start_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date_api     = End_Date.strftime("%Y-%m-%dT%H:%M:%S.000Z")                   #.strftime("%Y-%m-%dT00:00:00.000Z")  strftime("%Y-%m-%dT%H:%M:%S.000Z")
            expiry_date_api = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            # API Call
            right_Data = breeze.get_historical_data_v2(interval=interval,from_date=from_date_api,to_date=to_date_api,stock_code=stock_code,exchange_code=exchange_code,
                                                       product_type=product_type,expiry_date=expiry_date_api,right=Options_Type,strike_price=strike_price  )

            if (right_Data and right_Data.get("Error") is None and right_Data.get("Success"))  or \
               (right_Data and right_Data.get("Error") == "API did not return any response") or \
               (right_Data and right_Data.get("Error") is None):

                Error   = right_Data.get("Error", None)
                Success = right_Data.get("Success", None)
                if Error is None and Success:
                    Data = pd.DataFrame(Success)
                    if product_type == "futures":
                        Options_Type = "fu"
                    elif product_type == "cash":
                        Options_Type = "ch"
                    if not Data.empty:
                        Column = ["stock_code", "expiry_date", "strike_price", "datetime",
                            f"{Options_Type}_open",  f"{Options_Type}_high",   f"{Options_Type}_low",
                            f"{Options_Type}_close", f"{Options_Type}_volume", f"{Options_Type}_oi",  ]
                        # Format datetime
                        Data["datetime"] = pd.to_datetime(Data["datetime"], errors="coerce")
                        Data["datetime"] = Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
                        if "expiry_date" in Data.columns:
                            Data["expiry_date"] = Data["expiry_date"].apply(safe_parse_date)
                        else:
                            Data["expiry_date"] = None # Expiry_Date.strftime("%d-%m-%Y")
                        rename_map = {"open": f"{Options_Type}_open",  "high": f"{Options_Type}_high","low": f"{Options_Type}_low",
                                        "close": f"{Options_Type}_close","volume": f"{Options_Type}_volume"}
                        if "open_interest" in Data.columns:
                            rename_map["open_interest"] = f"{Options_Type}_oi"
                        Data = Data.rename(columns=rename_map)

                        # Keep only valid cols
                        valid_cols = [col for col in Column if col in Data.columns]
                        Data = Data[valid_cols]
                        if isinstance(Data, dict):
                           Data = pd.DataFrame(Data)
                        return Data
                    else:
                        Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
                        Error_Date   = End_Date.strftime("%d-%m-%Y")
                        Data_Error(stock_name=stock_name, expiry_date=Error_Expiry, strike_price=strike_price, options_type=Options_Type, error_date=Error_Date,
                                          function_error="Fetch_ICICI_Historical_Data (Data.empty:)", api_error=Error)
                        return None
                else:
                  Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
                  Error_Date   = End_Date.strftime("%d-%m-%Y")
                  Data_Error(stock_name=stock_name, expiry_date=Error_Expiry, strike_price=strike_price, options_type=Options_Type, error_date=Error_Date,
                                    function_error="Fetch_ICICI_Historical_Data (Error is None and Success:)", api_error=Error)
                  return None

            elif right_Data and right_Data.get("Error") == "Rate Limit Exceeded":             # 🚫 अगर Breeze ने बोला limit exceed
                time.sleep(120)

            attempt += 1                                                                      # अगर ऊपर से कोई success नहीं मिला तो retry करो
            if attempt < max_retries:
                time.sleep(delay)

        except Exception as e:
            attempt += 1
            if attempt < max_retries:
                time.sleep(delay)

    # ✅ अगर fail हो गया final error return करो
    api_error = None
    if right_Data and isinstance(right_Data, dict):
        api_error = right_Data.get("Error",None)
    Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
    Error_Date   = End_Date.strftime("%d-%m-%Y")
    Data_Error(stock_name=stock_name, expiry_date=Error_Expiry, strike_price=strike_price, options_type=Options_Type, error_date=Error_Date,
                      function_error=f"Fetch_ICICI_Historical_Data Failed after {max_retries} retries", api_error=api_error)
    return None


# # Example usage
# stock_name    = "Nifty"
# stock_code    = ICICI.get_Stock_Name(breeze, "NSE", stock_name)
# exchange_code = "NFO"          # "NFO" "NSE"
# product_type  = "options"      # "options", "futures", "cash"
# Options_Type  = "call"         # "others" , "call" , "put"
# strike_price  = 24700         # integer, not string
# interval      = "1minute"      # "1second", "1minute", "5minute", "30minute" , "1day".
# Start_Date    = datetime.strptime("01-09-2025", "%d-%m-%Y")
# End_Date      = datetime.strptime("10-09-2025", "%d-%m-%Y")
# Expiry_Date   = datetime.strptime('30-09-2025', "%d-%m-%Y")
# data = get_historical_data_API(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, max_retries=3, delay=1)
# print(data)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop  fetch_options_while_loop   fetch_options_while_loop  fetch_options_while_loop   fetch_options_while_loop     fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import timedelta
from tabulate import tabulate
import datetime as dt
import time
def fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name="No"):
    final_df = pd.DataFrame()
    current_to = End_Date
    while current_to >= Start_Date:
        Data = get_historical_data_API( breeze, interval, Start_Date, current_to, stock_code, exchange_code, product_type,
                                                Expiry_Date, Options_Type, strike_price,max_retries=3, delay=0,stock_name=stock_name)
        if Data is not None and not Data.empty:
            final_df = pd.concat([Data, final_df], ignore_index=True)
            Data["datetime_dt"] = pd.to_datetime(Data["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
            first_time = Data["datetime_dt"].min()  # pd.to_datetime(Data["datetime_dt"].min(), format="%d-%m-%Y %H:%M", errors="coerce")
            if pd.isna(first_time):  # अगर parsing fail हो
                current_to -= timedelta(days=1)
                current_to = current_to.replace(hour=0,minute=0,second=0)
            elif first_time <= Start_Date:
                break
            else:
                current_to = first_time - timedelta(minutes=1)
        else:
            current_to -= timedelta(days=1)
            current_to = current_to.replace(hour=0,minute=0,second=0)
        time.sleep(0.001)         # API rate-limit से बचने के लिए
    if not final_df.empty:
      final_df["datetime"] = pd.to_datetime(final_df["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
      final_df["expiry_date"] = pd.to_datetime(final_df["expiry_date"], format="%d-%m-%Y", errors="coerce")
      if product_type == "futures":
        Column_Name = ["datetime","expiry_date"]
      elif product_type == "options":
        Column_Name = ["datetime","strike_price","expiry_date"]
      elif product_type == "cash":
        Column_Name = ["datetime"]
        final_df = final_df.drop(columns=["expiry_date"], errors="ignore")
      final_df = final_df.drop_duplicates(subset=Column_Name).reset_index(drop=True)
      if End_Date.time() == dt.time(0, 0):
           End_Date += dt.timedelta(days=1)
      final_df = final_df[(final_df["datetime"] >= Start_Date) & (final_df["datetime"] <= End_Date)]
      final_df = final_df.sort_values(by="datetime").reset_index(drop=True)
      final_df["datetime"] = final_df["datetime"].dt.strftime("%d-%m-%Y %H:%M")
      if "expiry_date" in final_df.columns:
         final_df["expiry_date"] = final_df["expiry_date"].dt.strftime("%d-%m-%Y")
    else:
        Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
        Data_Error(stock_name=stock_name, expiry_date=Error_Expiry, strike_price=strike_price, options_type=Options_Type, error_date="All",
                   function_error="fetch_options_while_loop", api_error=None)
    return final_df
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop     fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name="No"):
    final_df = pd.DataFrame()
    # ✅ केवल weekdays (Mon–Fri)
    date_list = sorted([(Start_Date + timedelta(days=i)) for i in range((End_Date  - Start_Date).days + 1)
                       if (Start_Date + timedelta(days=i)).weekday() < 5], reverse=True)
    # ✅ ThreadPoolExecutor के साथ parallel fetch
    # with ThreadPoolExecutor(max_workers=min(200, len(date_list))) as executor:
    with ThreadPoolExecutor(max_workers=max(1, min(200, len(date_list)))) as executor:
        # futures = { executor.submit( get_historical_data_API, breeze, interval, date.replace(hour=9,minute=15,second=0), date.replace(hour=15,minute=30,second=0), stock_code, exchange_code, product_type, Expiry_Date,
        #                              Options_Type, strike_price, max_retries=3, delay=0, stock_name=stock_name ): date for date in date_list }
        futures = { executor.submit( get_historical_data_API, breeze, interval, date, date, stock_code, exchange_code, product_type, Expiry_Date,
                                     Options_Type, strike_price, max_retries=3, delay=0, stock_name=stock_name ): date for date in date_list }
        results = []
        for future in as_completed(futures):
            date = futures[future]
            try:
                Data = future.result()
                if isinstance(Data, pd.DataFrame) and not Data.empty:
                    results.append(Data)
            except Exception as e:
                print(f"❌ Error fetching {date.strftime('%d-%m-%Y')}: {e}")
    if results:
        final_df = pd.concat(results, ignore_index=True)
        if product_type == "futures":
          Column_Name = ["datetime","expiry_date"]
        elif product_type == "options":
          Column_Name = ["datetime","strike_price","expiry_date"]
        elif product_type == "cash":
          Column_Name = ["datetime"]
          final_df = final_df.drop(columns=["expiry_date"], errors="ignore")
        final_df = final_df.drop_duplicates(subset=Column_Name).reset_index(drop=True)
        final_df["datetime"] = pd.to_datetime(final_df["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
        if "expiry_date" in final_df.columns:
           final_df["expiry_date"] = pd.to_datetime(final_df["expiry_date"], format="%d-%m-%Y", errors="coerce")
        if End_Date.time() == dt.time(0, 0):
           End_Date += dt.timedelta(days=1)
        final_df = final_df[(final_df["datetime"] >= Start_Date) & (final_df["datetime"] <= End_Date)]
        final_df = final_df.sort_values(by="datetime").reset_index(drop=True)
        final_df["datetime"] = final_df["datetime"].dt.strftime("%d-%m-%Y %H:%M")
        if "expiry_date" in final_df.columns:
           final_df["expiry_date"] = final_df["expiry_date"].dt.strftime("%d-%m-%Y")
    else:
        Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
        Data_Error(stock_name=stock_name, expiry_date=Error_Expiry, strike_price=strike_price, options_type=Options_Type, error_date="All",
                   function_error="fetch_options_For_loop", api_error=None)
    return final_df

# Example usage
# stock_name     = "Nifty"           # "Nifty Bank"  "Nifty"
# stock_code     = get_Stock_Name(breeze, "NSE", stock_name)
# exchange_code  = "NFO"             # "NFO" "NSE"
# stock_code     = stock_code        # Nifty
# product_type   = "options"         # "options", "futures", "cash"
# Options_Type   = "call"            # "others" , "call" , "put"
# strike_price   = 24000             # integer, not string
# interval       = "1minute"         # "1second", "1minute", "5minute", "30minute" , "1day".
# past_day       = 20
# Start_Date    = datetime.strptime("01-10-2025 00:00", "%d-%m-%Y %H:%M")
# End_Date      = datetime.strptime("09-10-2025 00:00", "%d-%m-%Y %H:%M")
# Expiry_Date   = datetime.strptime('28-10-2025', "%d-%m-%Y")
# # Use ThreadPool version
# while_Data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
# print(tabulate(pd.concat([while_Data.head(3), while_Data.tail(3)]), headers='keys', tablefmt='psql'))
# print("While Loop Data Shape:", while_Data.shape)
# For_Data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
# print(tabulate(pd.concat([For_Data.head(3), For_Data.tail(3)]), headers='keys', tablefmt='psql'))
# print("For Loop Data Shape:", For_Data.shape)
# Error_Data_to_Excel(filename="Error_Data")
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  fetch_Merged_Data   fetch_Merged_Data     fetch_Merged_Data  fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data      fetch_Merged_Data   fetch_Merged_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch_Merged_Data(DATA1, DATA2):
    try:
        if DATA1 is not None:
            try: DATA1 = pd.concat(DATA1, ignore_index=True) if isinstance(DATA1, list) else DATA1
            except:pass
        if DATA2 is not None:
            try: DATA2 = pd.concat(DATA2, ignore_index=True) if isinstance(DATA2, list) else DATA2
            except: pass

        # Case 1: Dono available → merge ke sath suffixes
        if DATA1 is not None and DATA2 is not None:
            Merged_Data = pd.merge( DATA1, DATA2, on=["datetime", "stock_code", "expiry_date", "strike_price"], how="outer", suffixes=("_call", "_put"))

        # Case 2: Sirf DATA1 available → "_call" suffix add
        elif DATA1 is not None:
            Merged_Data = DATA1.copy()
            Merged_Data = Merged_Data.rename( columns={col: col + "_call" for col in Merged_Data.columns
                                              if col not in ["datetime", "stock_code", "expiry_date", "strike_price"]} )
        # Case 3: Sirf DATA2 available → "_put" suffix add
        elif DATA2 is not None:
            Merged_Data = DATA2.copy()
            Merged_Data = Merged_Data.rename( columns={col: col + "_put" for col in Merged_Data.columns
                                              if col not in ["datetime", "stock_code", "expiry_date", "strike_price"]} )
        else:
            return None
        if "datetime" in Merged_Data.columns:
            Merged_Data["datetime"] = pd.to_datetime(Merged_Data["datetime"], errors="coerce", format="%d-%m-%Y %H:%M")
            Merged_Data = Merged_Data.sort_values(by="datetime", ascending=True).reset_index(drop=True)
            Merged_Data['datetime'] = Merged_Data['datetime'].dt.strftime('%d-%m-%Y %H:%M')
        return Merged_Data
    except Exception as e:
        Data_Error(stock_name="No", expiry_date="No", strike_price="No", options_type="No", error_date="No",
            function_error="fetch_Merged_Data Error", api_error=e)
        print(f"fetch_Merged_Data Function Error: {e}")
        return None
# # Example usage
# Merged_Data = fetch_Merged_Data(Data_call, Data_put)
# print(tabulate(Merged_Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  fetch_Merged_Data   fetch_Merged_Data     fetch_Merged_Data  fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data     fetch_Merged_Data      fetch_Merged_Data   fetch_Merged_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
def Pandas_Date_Formet(Date): # 🔹 Flexible Date Parsing Function
    Formet_List = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S"]
    for Date_Formet in Formet_List:
        try:
            return datetime.strptime(Date, Date_Formet)
        except ValueError:
            continue
    return Date  # अगर कोई फॉर्मेट match न हो तो string 그대로 return
def get_start_end_expiry_formet(Expiry_Date: str, Start_Date: str, End_Date: str): # 🔹 Expiry, Start, End Date Convert & Adjust Function
    Expiry_Date = Pandas_Date_Formet(Expiry_Date)
    try:
        Days_Before_Expiry = float(Start_Date) # अगर Start_Date नंबर है (मतलब expiry से कुछ दिन पहले चाहिए)
        Start_Date = (Expiry_Date - timedelta(days=Days_Before_Expiry)).replace(hour=0, minute=0, second=0)
    except ValueError:
        Start_Date = Pandas_Date_Formet(Start_Date)
    try:
        End_Days = float(End_Date) # 🔸 End_Date को हैंडल करो
        if End_Days <= 0:
            End_Date = Expiry_Date
        else:
            End_Date = (Start_Date + timedelta(days=End_Days)).replace(hour=0, minute=0, second=0)
    except ValueError:
        End_Date = Pandas_Date_Formet(End_Date)
    if End_Date > Expiry_Date:     # 🔸 अगर End_Date expiry से आगे चला गया तो expiry तक सीमित करो
        End_Date = Expiry_Date
    return Expiry_Date, Start_Date, End_Date

# 🔹 Example usage
# Expiry_Date, Start_Date, End_Date = get_start_end_expiry_formet("28-10-2025", "5", "10")
# print("Expiry_Date:", Expiry_Date)
# print("Start_Date:", Start_Date)
# print("End_Date:", End_Date))
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read_Strike_Data   Read_Strike_Data     Read_Strike_Data  Read_Strike_Data     Read_Strike_Data     Read_Strike_Data     Read_Strike_Data     Read_Strike_Data      Read_Strike_Data   Read_Strike_Data   Read_Strike_Data   Read_Strike_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime
from tabulate import tabulate
import pandas as pd
def Read_Strike_Data(breeze, stock_name, Expiry_Date, Options_Type, strike_price, Start_Date = 60, End_Date = 0, interval = "1minute", Loop_Type = "for" ):
    stock_code = get_Stock_Name(breeze, "NSE", stock_name)
    Expiry_Date, Start_Date, End_Date = get_start_end_expiry_formet(Expiry_Date, Start_Date, End_Date)
    # ========================= CASH =========================
    if Options_Type == "ch":
        exchange_code = "NSE"
        product_type = "cash"
        option_type = "others"
        Expiry_Date = datetime.strptime("01-01-2000", "%d-%m-%Y")
        strike_price = 0
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= FUTURES =========================
    elif Options_Type == "fu":
        exchange_code = "NFO"
        product_type = "futures"
        option_type = "others"
        strike_price = 0
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= CALL OPTIONS =========================
    elif Options_Type == "call":
        exchange_code = "NFO"
        product_type = "options"
        option_type = "call"
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= PUT OPTIONS =========================
    elif Options_Type == "put":
        exchange_code = "NFO"
        product_type = "options"
        option_type = "put"
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= BOTH CALL & PUT =========================
    elif Options_Type == "op":
        exchange_code = "NFO"
        product_type = "options"
        if Loop_Type == "for":
            data_call = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, "call", strike_price, stock_name)
            data_put = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, "put", strike_price, stock_name)
        elif Loop_Type == "while":
            data_call = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, "call", strike_price, stock_name)
            data_put = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, "put", strike_price, stock_name)
        data = fetch_Merged_Data(data_call, data_put)
    else:
        print("❌ Invalid Option Type! (Use: 'ch', 'fu', 'call', 'put', or 'op')")
        return
    # ========================= PRINT FINAL TABLE =========================
    if not data.empty:
        return data
        # print(tabulate(pd.concat([data.head(3), data.tail(3)]), headers="keys", tablefmt="psql"))
    else:
        print("⚠️ कोई डेटा नहीं मिला!")

# # Example usage
# stock_name   = "Nifty"               # "Nifty Bank"  "Nifty"
# Expiry_Date  = "28-10-2025"          
# Options_Type = "call"                # 'ch', 'fu', 'call', 'put', 'op'
# strike_price = 24000
# Start_Date   = "01-10-2025 00:00"
# End_Date     = "10"                  # 10 days बाद तक
# interval     = "1minute"             # "1second", "1minute", "5minute", "30minute" , "1day".
# Loop_Type = "for"
# data = Read_Strike_Data(breeze, stock_name, Expiry_Date, Options_Type, strike_price, Start_Date, End_Date, interval, Loop_Type)
# print(tabulate(pd.concat([data.head(3), data.tail(3)]), headers="keys", tablefmt="psql"))

#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================
#=========================================================================================================================================================================================================================================================================================

banknifty_monthly_expiry = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '27-03-2024', '24-04-2024', '29-05-2024', '26-06-2024', '31-07-2024', '28-08-2024', '25-09-2024', '30-10-2024', '27-11-2024', '24-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025', '29-05-2025', '26-06-2025', '31-07-2025', '28-08-2025', '30-09-2025', '28-10-2025', '25-11-2025', '30-12-2025',]

nifty_monthly_expiry     = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '28-03-2024', '25-04-2024', '30-05-2024', '27-06-2024', '25-07-2024', '29-08-2024', '26-09-2024', '31-10-2024', '28-11-2024', '26-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025', '29-05-2025', '26-06-2025', '31-07-2025', '28-08-2025', '30-09-2025', '28-10-2025', '25-11-2025', '30-12-2025' ]

nifty_weekly_expiry      = ['07-01-2021', '14-01-2021', '21-01-2021', '28-01-2021', '04-02-2021', '11-02-2021', '18-02-2021', '25-02-2021', '04-03-2021', '10-03-2021', '18-03-2021', '25-03-2021', '01-04-2021', '08-04-2021', '15-04-2021', '22-04-2021', '29-04-2021', '06-05-2021', '12-05-2021', '20-05-2021', '27-05-2021', '03-06-2021', '10-06-2021', '17-06-2021', '24-06-2021', '01-07-2021', '08-07-2021', '15-07-2021', '22-07-2021', '29-07-2021', '05-08-2021', '12-08-2021', '18-08-2021', '26-08-2021', '02-09-2021', '09-09-2021', '16-09-2021', '23-09-2021', '30-09-2021', '07-10-2021', '14-10-2021', '21-10-2021', '28-10-2021', '03-11-2021', '11-11-2021', '18-11-2021', '25-11-2021', '02-12-2021', '09-12-2021', '16-12-2021', '23-12-2021', '30-12-2021',
                            '06-01-2022', '13-01-2022', '20-01-2022', '27-01-2022', '03-02-2022', '10-02-2022', '17-02-2022', '24-02-2022', '03-03-2022', '10-03-2022', '17-03-2022', '24-03-2022', '31-03-2022', '07-04-2022', '13-04-2022', '21-04-2022', '28-04-2022', '05-05-2022', '12-05-2022', '19-05-2022', '26-05-2022', '02-06-2022', '09-06-2022', '16-06-2022', '23-06-2022', '30-06-2022', '07-07-2022', '14-07-2022', '21-07-2022', '28-07-2022', '04-08-2022', '11-08-2022', '18-08-2022', '25-08-2022', '01-09-2022', '08-09-2022', '15-09-2022', '22-09-2022', '29-09-2022', '06-10-2022', '13-10-2022', '20-10-2022', '27-10-2022', '03-11-2022', '10-11-2022', '17-11-2022', '24-11-2022', '01-12-2022', '08-12-2022', '15-12-2022', '22-12-2022', '29-12-2022',
                            '05-01-2023', '12-01-2023', '19-01-2023', '25-01-2023', '02-02-2023', '09-02-2023', '16-02-2023', '23-02-2023', '02-03-2023', '09-03-2023', '16-03-2023', '23-03-2023', '29-03-2023', '06-04-2023', '13-04-2023', '20-04-2023', '27-04-2023', '04-05-2023', '11-05-2023', '18-05-2023', '25-05-2023', '01-06-2023', '08-06-2023', '15-06-2023', '22-06-2023', '28-06-2023', '06-07-2023', '13-07-2023', '20-07-2023', '27-07-2023', '03-08-2023', '10-08-2023', '17-08-2023', '24-08-2023', '31-08-2023', '07-09-2023', '14-09-2023', '21-09-2023', '28-09-2023', '05-10-2023', '12-10-2023', '19-10-2023', '26-10-2023', '02-11-2023', '09-11-2023', '16-11-2023', '23-11-2023', '30-11-2023', '07-12-2023', '14-12-2023', '21-12-2023', '28-12-2023',
                            '04-01-2024', '11-01-2024', '18-01-2024', '25-01-2024', '01-02-2024', '08-02-2024', '15-02-2024', '22-02-2024', '29-02-2024', '07-03-2024', '14-03-2024', '21-03-2024', '28-03-2024', '04-04-2024', '10-04-2024', '18-04-2024', '25-04-2024', '02-05-2024', '09-05-2024', '16-05-2024', '23-05-2024', '30-05-2024', '06-06-2024', '13-06-2024', '20-06-2024', '27-06-2024', '04-07-2024', '11-07-2024', '18-07-2024', '25-07-2024', '01-08-2024', '08-08-2024', '14-08-2024', '22-08-2024', '29-08-2024', '05-09-2024', '12-09-2024', '19-09-2024', '26-09-2024', '03-10-2024', '10-10-2024', '17-10-2024', '24-10-2024', '31-10-2024', '07-11-2024', '14-11-2024', '21-11-2024', '28-11-2024', '05-12-2024', '12-12-2024', '19-12-2024', '26-12-2024',
                            '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025', '09-04-2025', '17-04-2025', '24-04-2025', '30-04-2025', '08-05-2025', '15-05-2025', '22-05-2025', '29-05-2025', '05-06-2025', '12-06-2025', '19-06-2025', '26-06-2025', '03-07-2025', '10-07-2025', '17-07-2025', '24-07-2025', '31-07-2025', '07-08-2025', '14-08-2025', '21-08-2025', '28-08-2025', '02-09-2025', '09-09-2025', '16-09-2025', '23-09-2025', '30-09-2025', '07-10-2025', '14-10-2025', '20-10-2025', '25-10-2025', '04-11-2025', '11-11-2025', '18-11-2025', '25-11-2025', '30-12-2025',  ]

Strike_Gep_List          = {"nifty" : 50, "nifty bank" : 100, "reliance" :10}

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Pandas_Date_Formet   Pandas_Date_Formet     Pandas_Date_Formet  Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet      Pandas_Date_Formet   Pandas_Date_Formet
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
def Pandas_Date_Formet(Date): # 🔹 Flexible Date Parsing Function
    Formet_List = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S"]
    for Date_Formet in Formet_List:
        try:
            return datetime.strptime(Date, Date_Formet)
        except ValueError:
            continue
    return Date  # अगर कोई फॉर्मेट match न हो तो string 그대로 return
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry    get_Expiry   get_Expiry
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import calendar
import pandas as pd
def get_Symbol_Expiry(Dates, Symbol, Expiry_Period, Expiry_Type, Start_Date=None, End_Date=None):
    global banknifty_monthly_expiry, nifty_monthly_expiry, nifty_weekly_expiry, naturalgas_futures_monthly_expiry
    try:
        # 🔹 Select correct expiry list first (har condition me needed hai)
        if Expiry_Period.lower() == "weekiy" and Symbol.lower() == "nifty":
            Expiry_List = nifty_weekly_expiry
        elif Expiry_Period.lower() == "monthly":
            if Symbol.lower() in ["nifty", "reliance"]:             # if stock_name in ["nifty", "nifty bank"]:
                Expiry_List = nifty_monthly_expiry
            elif Symbol.lower() == "nifty bank":
                Expiry_List = banknifty_monthly_expiry
            elif Symbol.lower() == "naturalgas":
                Expiry_List = naturalgas_futures_monthly_expiry
            else:
                raise ValueError(f"Unknown symbol for monthly expiry: {Symbol}")
        else:
            raise ValueError(f"Unknown Expiry_Period: {Expiry_Period}")
        Expiry_List = pd.to_datetime(pd.Series(Expiry_List), format="%d-%m-%Y")
        # 🔹 CASE 1: Single date expiry calculation (Current / Next)
        if Dates is not None:
            Date = Pandas_Date_Formet(Dates)
            filtered = Expiry_List[Expiry_List >= Date].dt.strftime("%d-%m-%Y").tolist()
            if not filtered:
                return None

            if Expiry_Type.lower() == "current":
                return filtered[0]
            elif Expiry_Type.lower() == "next":
                return filtered[1] if len(filtered) > 1 else None
            else:
                raise ValueError(f"Unknown Expiry_Type: {Expiry_Type}")
        # 🔹 CASE 2: Date range expiry list calculation
        elif Start_Date is not None and End_Date is not None:
            Start_Date = Pandas_Date_Formet(Start_Date).replace(day=1, hour=0, minute=0, second=0, microsecond=0)

            End_Date = Pandas_Date_Formet(End_Date)
            last_day = calendar.monthrange(End_Date.year, End_Date.month)[1]
            End_Date = End_Date.replace(day=last_day, hour=23, minute=59, second=59, microsecond=0)

            filtered = Expiry_List[(Expiry_List >= Start_Date) & (Expiry_List <= End_Date)]
            return filtered.dt.strftime("%d-%m-%Y").tolist()
        return None
    except Exception as e:
        print(f"get_Expiry Function Error: {e}")
        return None

# # Example usage
# Dates          = None #"05-10-2025"
# Symbol         = "nifty bank" # nifty  "nifty bank"
# Expiry_Period  = "Monthly"  # "Weekiy" , "Monthly"
# Expiry_Type    = "Current"  # "Current", "Next"
# Start_Date = "01-06-2025"
# End_Date   = "15-09-2025"
# Expirys        = get_Symbol_Expiry(Dates, Symbol, Expiry_Period, Expiry_Type, Start_Date, End_Date)
# print(Expirys)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep   get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Strike_Gep(Symbol):
    global Strike_Gep_List
    try:
       return Strike_Gep_List[Symbol.lower()]
    except Exception as e:
       print(f"get_Strike_Gep Function Error: {e}")
       return None
# # Example usage
# Symbol = "nifty"  #  nifty , banknifty
# Strike_Gep = get_Strike_Gep(Symbol)
# print(Strike_Gep)
#_____________________________________________________________________________________________________________________________________________________
from datetime import datetime, timedelta
import time
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data   get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta, time as dtime
import pandas as pd

def get_Cash_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute", Loop_Type="for"):
    Expiry_Date = End_Date
    Options_Type = "ch"
    strike_price = 0
    Cash_Data = Read_Strike_Data(breeze, stock_name, Expiry_Date, Options_Type, strike_price, Start_Date, End_Date, interval, Loop_Type)

    # ✅ Convert and filter by market hours
    Cash_Data["datetime"] = pd.to_datetime(Cash_Data["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
    Cash_Data = Cash_Data[Cash_Data["datetime"].dt.time.between(dtime(9, 15), dtime(15, 30))]

    # ✅ Sort & format
    Cash_Data = Cash_Data.sort_values(by="datetime").reset_index(drop=True)
    Cash_Data["datetime"] = Cash_Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")

    # ✅ Drop unwanted columns
    if stock_name.lower() in ["nifty", "nifty bank"]:
        if "ch_volume" in Cash_Data.columns:
            Cash_Data.drop(columns=["ch_volume"], inplace=True)

    return Cash_Data

# # Example usage
# stock_name = "Nifty Bank"
# Start_Date = "01-07-2025"
# End_Date   = "16-10-2025"
# interval="1minute"
# Ch_data = get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval)
# print(tabulate(pd.concat([Ch_data.head(3), Ch_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data   get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for"):
    expiry_list = get_Symbol_Expiry(None, stock_name, "Monthly", "Current", Start_Date, End_Date)
    date_ranges = []
    for i, expiry in enumerate(expiry_list):
        expiry_date = datetime.strptime(expiry, "%d-%m-%Y")
        if i == 0:
            start_date = datetime.strptime(Start_Date, "%d-%m-%Y")
        else:
            start_date = datetime.strptime(expiry_list[i-1], "%d-%m-%Y") + timedelta(days=1)
        if i < len(expiry_list)-1:
            end_date = datetime.strptime(expiry_list[i+1], "%d-%m-%Y")
        else:
            end_date = datetime.strptime(End_Date, "%d-%m-%Y")
        if end_date > expiry_date:
            end_date = expiry_date
        date_ranges.append((start_date, end_date, expiry_date.strftime("%d-%m-%Y")))

    Options_Type = "fu"
    strike_price = 0
    all_data = []
    def fetch_data(start, end, expiry):
        return Read_Strike_Data(breeze, stock_name, expiry, Options_Type, strike_price,start.strftime("%d-%m-%Y"), end.strftime("%d-%m-%Y"), interval, Loop_Type)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_data, start, end, expiry) for (start, end, expiry) in date_ranges]
        for f in as_completed(futures):
            try:
                all_data.append(f.result())
            except Exception as e:
                print("⚠️ Error:", e)

    if not all_data:
        print("❌ कोई डेटा नहीं मिला")
        return pd.DataFrame()

    Futures_Data             = pd.concat(all_data, ignore_index=True)
    Futures_Data             = Futures_Data.drop_duplicates(subset=["datetime", "expiry_date"], keep="last")
    Futures_Data["datetime"] = pd.to_datetime(Futures_Data["datetime"], format="%d-%m-%Y %H:%M", errors='coerce')
    Futures_Data             = Futures_Data.sort_values(by="datetime").reset_index(drop=True)
    Futures_Data["datetime"] = Futures_Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    # Futures_Data.rename(columns={"expiry_date": "m_c_expiry"}, inplace=True)
    return Futures_Data
# # Example usage
# stock_name = "Nifty Bank"
# Start_Date = "01-07-2025"
# End_Date   = "16-10-2025"
# interval="1minute"
# Fu_data = get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval)
# print(tabulate(pd.concat([Fu_data.head(3), Fu_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data   Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Ch_Fu_merge_data(Ch_data, Fu_data):
    Ch_data["datetime"] = pd.to_datetime(Ch_data["datetime"], format="%d-%m-%Y %H:%M") # 🔹 Step 1: datetime को proper format में convert करो
    Fu_data["datetime"]    = pd.to_datetime(Fu_data["datetime"], format="%d-%m-%Y %H:%M")
    if "stock_code" not in Fu_data.columns: # 🔹 Step 2: stock_code columns ensure करो
        Fu_data["stock_code"] = Ch_data["stock_code"].iloc[0]
    if "stock_code" not in Ch_data.columns:
        Ch_data["stock_code"] = Fu_data["stock_code"].iloc[0]

    merged = pd.merge_asof(Ch_data.sort_values("datetime"),Fu_data.sort_values("datetime"),on="datetime", # 🔹 Step 3: पहले normal nearest merge करो
                           by="stock_code",direction="nearest",tolerance=pd.Timedelta("0min")) # nearest 3 min तक match allow

    missing_mask = merged["fu_open"].isna()   # 🔹 Step 4: जिन rows का match नहीं मिला उन्हें अगली available future row से भरें
    if missing_mask.any():
        for idx in merged[missing_mask].index:
            current_time = merged.loc[idx, "datetime"]
            stock = merged.loc[idx, "stock_code"]
            future_rows = Fu_data[(Fu_data["datetime"] > current_time) & (Fu_data["stock_code"] == stock)] # अगला available future row
            if not future_rows.empty:
                nearest_future = future_rows.iloc[0]
                for col in Fu_data.columns:
                    if col not in ["datetime", "stock_code"]:
                        merged.loc[idx, col] = nearest_future[col]
    merged = merged.sort_values(by="datetime").reset_index(drop=True)  # 🔹 Step 5: final formatting
    merged["datetime"] = merged["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    return merged
# # Example usage
# merged_data = merge_data(Ch_data, Fu_data)
# print(tabulate(pd.concat([merged_data.head(3), merged_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry   get_Expiry  get_Expiry  get_Expiry  get_Expiry
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Expiry(data, stock_name):
    data["datetime"] = pd.to_datetime(data["datetime"], format="%d-%m-%Y %H:%M")
    unique_dates = data["datetime"].dt.date.unique()
    expiry_map = {}
    for d in unique_dates:
        Dates = pd.Timestamp(d).strftime("%d-%m-%Y 09:15")
        curr_m_expiry = get_Symbol_Expiry(Dates, stock_name, "Monthly", "Current")      # 🔹 Monthly Current Expiry
        if stock_name.lower() == "nifty":
            curr_w_expiry = get_Symbol_Expiry(Dates, stock_name, "Weekiy", "Current")   # 🔹 Weekly Current Expiry
            next_w_expiry = get_Symbol_Expiry(Dates, stock_name, "Weekiy", "Next")      # 🔹 Weekly Next Expiry
            expiry_map[d] = {"curr_m_expiry": curr_m_expiry,"curr_w_expiry": curr_w_expiry,"next_w_expiry": next_w_expiry}
        else:
            expiry_map[d] = {"curr_m_expiry": curr_m_expiry}
    
    if "expiry_date" in data.columns:
        data["curr_m_expiry"] = data["expiry_date"]
        data.drop(columns=["expiry_date"], inplace=True)
    else:
        data["curr_m_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["curr_m_expiry"])
    if stock_name.lower() == "nifty":
        data["curr_w_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["curr_w_expiry"])
        data["next_w_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["next_w_expiry"])

    data = data.sort_values(by="datetime").reset_index(drop=True)  # 🔹 Step 5: final formatting
    data["datetime"] = data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    return data

# # Example usage
# All_Data = Data.copy()
# stock_name = "nifty"
# All_Data = get_Expiry(All_Data, stock_name)
# print(tabulate(All_Data.head(5), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data   get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for"):
    def get_Round_ATM(stock_name, Price):
        Strike_Gep = get_Strike_Gep(stock_name)
        return (Price / Strike_Gep).round() * Strike_Gep
    def get_ATM_Strike(merged_data, stock_name):
        Strike_Gep = get_Strike_Gep(stock_name)
        merged_data["ch_atm"] = (merged_data["ch_close"] / Strike_Gep).round() * Strike_Gep
        merged_data["fu_atm"] = (merged_data["fu_close"] / Strike_Gep).round() * Strike_Gep
        return merged_data
    Ch_data = get_Cash_Data(breeze, stock_name, Start_Date, End_Date, interval, Loop_Type)
    Fu_data = get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval, Loop_Type)
    merged_data = Ch_Fu_merge_data(Ch_data, Fu_data)
    Data_Expiry = get_Expiry(merged_data, stock_name)
    Index_Data  = get_ATM_Strike(Data_Expiry, stock_name)
    return Index_Data
# # Example usage
# stock_name = "reliance"  #"nifty", "nifty bank"
# Start_Date = "01-09-2025"
# End_Date   = "16-10-2025"
# interval   = "1minute"
# Loop_Type  = "for"   #  "for" "while"
# Data = get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for")
# print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

