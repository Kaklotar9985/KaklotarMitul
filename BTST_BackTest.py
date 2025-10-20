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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Pandas_Date_Formet   Pandas_Date_Formet     Pandas_Date_Formet  Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet      Pandas_Date_Formet   Pandas_Date_Formet
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
def pandas_date_format(date_input, output_format=None):   
    format_list = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S",
                   "%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"]
    if isinstance(date_input, datetime):
        date_obj = date_input
    else:
        for fmt in format_list:
            try:
                date_obj = datetime.strptime(date_input, fmt)
                break
            except ValueError:
                continue
        else:
            return date_input

    # ✅ Output format handle करो
    if output_format is None:
        return date_obj
    else:
        return date_obj.strftime(output_format)
# Example
# date = "2025-10-01 09:15:00"
# output_format = "%d-%m-%Y %H:%M"
# formatted_date = pandas_date_format(date, output_format)
# print(formatted_date)
#=========================================================================================================================================================================================================================================================================================

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
#  get_market_open_dates   get_market_open_dates     get_market_open_dates  get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
import pandas as pd
market_open_dates = None
def get_market_open_dates(breeze):
    global market_open_dates
    try:
      if market_open_dates is None:
          Start_Date = datetime.strptime("01-01-2021", "%d-%m-%Y")
          today = datetime.today()
          End_Date = today.strftime("%d-%m-%Y")
          expiry_dt = datetime.strptime(End_Date, "%d-%m-%Y")
          data = fetch_options_while_loop(breeze,"1day",Start_Date, today,"Nifty","NSE","cash", expiry_dt,"others",0,"Nifty")
          unique_dates = pd.to_datetime(data["datetime"], dayfirst=True).dt.strftime("%d-%m-%Y").unique().tolist()
          date_list = [(today + timedelta(days=i)).strftime("%d-%m-%Y")for i in range(16)if (today + timedelta(days=i)).weekday() < 5]
          all_dates = sorted(set(unique_dates + date_list),key=lambda x: datetime.strptime(x, "%d-%m-%Y"))
          market_open_dates = all_dates
    except Exception as e:
        print(f"Error fetching market open dates: {e}")
        market_open_dates = None
# Example usage
# get_market_open_dates(breeze)
# print(market_open_dates)
# Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date
def Get_BTST_Date(breeze, Date=None, Get_Day_No=None, Start_Date=None, End_Date=None):
    global market_open_dates
    try:
        if market_open_dates is None:
            get_market_open_dates(breeze)
        if Get_Day_No is not None:
            if Get_Day_No == 0:
                return Date
            Date = pd.to_datetime(Date, format="%d-%m-%Y")
            market_open_dates = pd.to_datetime(pd.Series(market_open_dates), format="%d-%m-%Y")
            filtered_dates = market_open_dates[market_open_dates > Date].sort_values()
            filtered_dates = filtered_dates.dt.strftime("%d-%m-%Y").tolist()
            get_Date = filtered_dates[(int(Get_Day_No) - 1)]
            return get_Date

        if Start_Date is not None and End_Date is not None:
            Start_Date = pandas_date_format(Start_Date)
            End_Date = pandas_date_format(End_Date)
            if market_open_dates is None:
                get_market_open_dates(breeze)
            market_dates = [datetime.strptime(d, "%d-%m-%Y") for d in market_open_dates]
            date_list = [d for d in market_dates if Start_Date.date() <= d.date() <= End_Date.date()]
            date_list.sort(reverse=False)
            return date_list #[d.strftime("%d-%m-%Y") for d in date_list]
    except Exception as e:
        print(f"Get_BTST_Date Function Error: {e}")
# Example usage
# Date = "10-10-2025"
# Get_Day_No = None
# Start_Date = "10-10-2025 09:25"
# End_Date  =  "13-10-2025 09:19"
# BTST_Date = Get_BTST_Date(breeze, Date, Get_Day_No=1, Start_Date=None, End_Date=None)
# print(BTST_Date)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop     fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch_options_For_loop(breeze, interval, Start_Date, End_Date,stock_code, exchange_code, product_type,Expiry_Date, Options_Type, strike_price, stock_name="No"):
    final_df = pd.DataFrame()

    date_list = Get_BTST_Date(breeze, Start_Date=Start_Date, End_Date=End_Date)
    if not date_list:
      date_list = []
      current_date = Start_Date.date()
      while current_date <= End_Date.date():
          if current_date.weekday() < 5:
              date_list.append(current_date)
          current_date += timedelta(days=1)
      date_list = sorted(date_list, reverse=True)

    # print("🗓️ Dates to Fetch:", date_list)
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(200, len(date_list)))) as executor:
        futures = {executor.submit(get_historical_data_API, breeze, interval,
                dt.datetime.combine(date, dt.time(9, 15, 0)),dt.datetime.combine(date, dt.time(15, 30, 0)),
                stock_code, exchange_code, product_type,Expiry_Date,Options_Type,strike_price, 3, 0, stock_name): date for date in date_list }

        for future in as_completed(futures):
            date = futures[future]
            try:
                Data = future.result()
                if isinstance(Data, pd.DataFrame) and not Data.empty:
                    results.append(Data)
            except Exception as e:
                print(f"❌ Error fetching {date}: {e}")

    # ✅ Combine & clean
    if results:
        final_df = pd.concat(results, ignore_index=True)
        if product_type == "futures":
            Column_Name = ["datetime", "expiry_date"]
        elif product_type == "options":
            Column_Name = ["datetime", "strike_price", "expiry_date"]
        else:
            Column_Name = ["datetime"]
            final_df = final_df.drop(columns=["expiry_date"], errors="ignore")

        final_df.drop_duplicates(subset=Column_Name, inplace=True)
        final_df["datetime"] = pd.to_datetime(final_df["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
        if "expiry_date" in final_df.columns:
            final_df["expiry_date"] = pd.to_datetime(final_df["expiry_date"], format="%d-%m-%Y", errors="coerce")

        if End_Date.time() == dt.time(0, 0):
            End_Date += dt.timedelta(days=1)
        final_df = final_df[(final_df["datetime"] >= Start_Date) & (final_df["datetime"] <= End_Date)]
        final_df.sort_values(by="datetime", inplace=True)
        final_df.reset_index(drop=True, inplace=True)
        final_df["datetime"] = final_df["datetime"].dt.strftime("%d-%m-%Y %H:%M")
        if "expiry_date" in final_df.columns:
            final_df["expiry_date"] = final_df["expiry_date"].dt.strftime("%d-%m-%Y")
    else:
        Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
        Data_Error(stock_name=stock_name, expiry_date=Error_Expiry,
                   strike_price=strike_price, options_type=Options_Type,
                   error_date="All", function_error="fetch_options_For_loop",
                   api_error=None)
    return final_df

# Example usage
# stock_name     = "Nifty"           # "Nifty Bank"  "Nifty"
# stock_code     = get_Stock_Name(breeze, "NSE", stock_name)
# exchange_code  = "NFO"             # "NFO" "NSE"
# stock_code     = stock_code        # Nifty
# product_type   = "options"         # "options", "futures", "cash"
# Options_Type   = "call"            # "others" , "call" , "put"
# strike_price   = 25250             # integer, not string
# interval       = "1minute"         # "1second", "1minute", "5minute", "30minute" , "1day".
# past_day       = 20
# Start_Date    = datetime.strptime("10-10-2025 09:25", "%d-%m-%Y %H:%M")
# End_Date      = datetime.strptime("13-10-2025 09:19", "%d-%m-%Y %H:%M")
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
# from datetime import datetime, timedelta pandas_date_format(date_input, output_format=None):
# def Pandas_Date_Formet(Date): # 🔹 Flexible Date Parsing Function
#     Formet_List = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S"]
#     for Date_Formet in Formet_List:
#         try:
#             return datetime.strptime(Date, Date_Formet)
#         except ValueError:
#             continue
#     return Date  # अगर कोई फॉर्मेट match न हो तो string 그대로 return
def get_start_end_expiry_formet(Expiry_Date: str, Start_Date: str, End_Date: str): # 🔹 Expiry, Start, End Date Convert & Adjust Function
    Expiry_Date = pandas_date_format(Expiry_Date)
    try:
        Days_Before_Expiry = float(Start_Date) # अगर Start_Date नंबर है (मतलब expiry से कुछ दिन पहले चाहिए)
        Start_Date = (Expiry_Date - timedelta(days=Days_Before_Expiry)).replace(hour=0, minute=0, second=0)
    except ValueError:
        Start_Date = pandas_date_format(Start_Date)
    try:
        End_Days = float(End_Date) # 🔸 End_Date को हैंडल करो
        if End_Days <= 0:
            End_Date = Expiry_Date
        else:
            End_Date = (Start_Date + timedelta(days=End_Days)).replace(hour=0, minute=0, second=0)
    except ValueError:
        End_Date = pandas_date_format(End_Date)
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
#  trading_minutes   trading_minutes     trading_minutes  trading_minutes     trading_minutes     trading_minutes     trading_minutes     trading_minutes      trading_minutes   trading_minutes   trading_minutes   trading_minutes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
market_start = timedelta(hours=9, minutes=15)
market_end   = timedelta(hours=15, minutes=30)
def trading_minutes(breeze, Start_Date, End_Date):
    Start_Date = pandas_date_format(Start_Date)
    End_Date   = pandas_date_format(End_Date)
    market_dates = Get_BTST_Date(breeze, Start_Date=Start_Date, End_Date=End_Date)
    if market_dates:
        total_minutes = 0
        for day in market_dates:
            day_start = datetime.combine(day.date(), datetime.min.time()) + market_start
            day_end   = datetime.combine(day.date(), datetime.min.time()) + market_end
            
            # Current day overlap with start and end
            effective_start = max(Start_Date, day_start)
            effective_end   = min(End_Date, day_end)
            
            if effective_end > effective_start:
                total_minutes += int((effective_end - effective_start).total_seconds() / 60)
        return total_minutes
    else:
        total_minutes = 0
        current_day = Start_Date.date()
        while current_day <= End_Date.date():
            if current_day.weekday() < 5:
                day_start = datetime.combine(current_day, datetime.min.time()) + market_start
                day_end   = datetime.combine(current_day, datetime.min.time()) + market_end
                effective_start = max(Start_Date, day_start)
                effective_end   = min(End_Date, day_end)
                if effective_end > effective_start:
                    total_minutes += int((effective_end - effective_start).total_seconds() / 60)
            current_day += timedelta(days=1)
        return total_minutes
# Example usage
# Start_Date_str = "10-10-2025 09:25"
# End_Date_str   = "13-10-2025 09:19"
# minutes = trading_minutes(breeze, Start_Date_str, End_Date_str)
# print(minutes)
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
    Total_Minutes = trading_minutes(breeze, Start_Date, End_Date)
    if Total_Minutes < 999 :
       Loop_Type = "while"
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
def pandas_date_format(date_input, output_format=None):
    format_list = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S",
                   "%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"]
    if isinstance(date_input, datetime):
        date_obj = date_input
    else:
        for fmt in format_list:
            try:
                date_obj = datetime.strptime(date_input, fmt)
                break
            except ValueError:
                continue
        else:
            return date_input

    # ✅ Output format handle करो
    if output_format is None:
        return date_obj
    else:
        return date_obj.strftime(output_format)
# Example
# date = "2025-10-01 09:15:00"
# output_format = "%d-%m-%Y %H:%M"
# formatted_date = pandas_date_format(date, output_format)
# print(formatted_date)
#=========================================================================================================================================================================================================================================================================================

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






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_market_open_dates   get_market_open_dates     get_market_open_dates  get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
import pandas as pd
market_open_dates = None
def get_market_open_dates(breeze):
    global market_open_dates
    if market_open_dates is None:
        Start_Date = "01-01-2021"
        today = datetime.today()
        End_Date = today.strftime("%d-%m-%Y")

        # Historical data से unique trading dates
        data = ICICI.Read_Strike_Data( breeze, stock_name="Nifty", Expiry_Date=End_Date, Options_Type="ch", strike_price=0,
                                        Start_Date=Start_Date, End_Date=End_Date, interval="1day", Loop_Type="while" )
        unique_dates = pd.to_datetime( data["datetime"], dayfirst=True ).dt.strftime("%d-%m-%Y").unique().tolist()
        # आने वाले 15 दिन के weekdays (Mon–Fri)
        date_list = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(16)if (today + timedelta(days=i)).weekday() < 5]
        # दोनों lists merge करके unique और sorted output बनाओ
        all_dates = sorted(set(unique_dates + date_list),key=lambda x: datetime.strptime(x, "%d-%m-%Y"))
        market_open_dates = all_dates
# Example usage
# get_market_open_dates(breeze)
# print(market_open_dates)

# Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date
def Get_BTST_Date(breeze, Date, Get_Day_No = 1,):
    global market_open_dates
    try :
        if market_open_dates is None:
           get_market_open_dates(breeze)
        if Get_Day_No == 0 :
           return Date
        Date = pd.to_datetime(Date, format="%d-%m-%Y")
        market_open_dates = pd.to_datetime(pd.Series(market_open_dates), format="%d-%m-%Y")
        filtered_dates = market_open_dates[market_open_dates > Date].sort_values()
        filtered_dates = filtered_dates.dt.strftime("%d-%m-%Y").tolist()
        get_Date = filtered_dates[(int(Get_Day_No) - 1)]
        return get_Date
    except Exception as e:
        print(f"Get_BTST_Date Function Error: {e}")
# # Example usage
# Date = "10-10-2025"
# Get_Day_No = 1
# BTST_Date = Get_BTST_Date(Date)
# print(BTST_Date)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate#  Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Brokerage_Calculate(buy_price, sell_price, quantity, Options_Type="OP", Min_Brokerage=20):
    try:
        op_type = Options_Type.strip().lower()
        turnover = (abs(buy_price) + abs(sell_price)) * quantity

        # Initialize values
        brokerage = 0.0
        stt = 0.0
        transaction_charges = 0.0
        sebi_charges = 0.0
        stamp_duty = 0.0

        if op_type in ["fu", "fut", "futures"]:
            one_side_brokerage = min(0.0003 * turnover, Min_Brokerage)
            brokerage = one_side_brokerage * 2
            stt = 0.0002 * sell_price * quantity
            transaction_charges = 0.0000183 * turnover  # you used this
            sebi_charges = (10 / 10000000) * turnover
            stamp_duty = round((0.00002 * buy_price * quantity), 0)

        # OPTIONS
        elif op_type in ["op", "opt", "option", "call", "put"]:
            brokerage = Min_Brokerage * 2
            stt = 0.00055 * sell_price * quantity
            transaction_charges = 0.000375 * turnover
            sebi_charges = (10 / 10000000) * turnover
            stamp_duty = round((0.00043 * buy_price * quantity), 0)
        else:
            raise ValueError(f"Invalid Options_Type: {Options_Type}")
        gst = 0.18 * (brokerage + transaction_charges + sebi_charges)
        total_charges = brokerage + stt + transaction_charges + sebi_charges + gst + stamp_duty
        return round(total_charges, 2)

    except Exception as e:
        print(f"Brokerage_Calculate Function Error: {e}")
        return 0.0

# # Example usage
# futures_result = Brokerage_Calculate(buy_price=25000, sell_price=25000, quantity=450, Options_Type="FU")
# print(f"Futures Charges: {futures_result:.2f}")
# options_result = Brokerage_Calculate(buy_price=200, sell_price=200, quantity=75, Options_Type="OP")
# print(f"Options Charges: {options_result:.2f}")
#=========================================================================================================================================================================================================================================================================================


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown#  calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown   calculate_drawdown
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
from tabulate import tabulate
def calculate_drawdown(data, trade_no):
    # Handle 'ALL' or per-trade calculation
    if isinstance(trade_no, str) and trade_no.lower() == "all":
        trade_data = data.copy()
    else:
        trade_data = data[data["Trade_No"] == trade_no].copy()

    trade_data = trade_data.sort_values(by="Entry_DateTime").reset_index(drop=True)
    drawdown_col = f"Drawdown_{trade_no}"
    trade_data[drawdown_col] = 0.0

    running_total = 0.0
    for i in range(len(trade_data)):
        running_total += trade_data.loc[i, "PNL"]
        trade_data.loc[i, drawdown_col] = round(min(running_total, 0.0), 2)

    # For ALL, no trade filtering key
    if isinstance(trade_no, str) and trade_no.lower() == "all":
        return trade_data[[drawdown_col]]
    else:
        return trade_data[["Trade_No", drawdown_col]]
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data#  get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Analysis_Data(trade_log):
    try:
        Analysis_Data = pd.DataFrame(trade_log).copy()
        Analysis_Data["Trade_No"] = Analysis_Data["Trade_No"].astype(str)

        # Convert to datetime
        Analysis_Data["Entry_DateTime"] = pd.to_datetime(Analysis_Data["Entry_DateTime"], format="%d-%m-%Y %H:%M")
        Analysis_Data["Exit_DateTime"]  = pd.to_datetime(Analysis_Data["Exit_DateTime"],  format="%d-%m-%Y %H:%M")
        Analysis_Data["Expiry_Date"]    = pd.to_datetime(Analysis_Data["Expiry_Date"],    format="%d-%m-%Y")
        Analysis_Data.sort_values(by="Entry_DateTime", inplace=True)
        Analysis_Data.reset_index(drop=True, inplace=True)

        # === Overall Drawdown ===
        Analysis_Data["Drawdown_ALL"] = calculate_drawdown(Analysis_Data, "ALL")["Drawdown_ALL"].values

        # === Fill missing drawdowns ===
        drawdown_cols = [c for c in Analysis_Data.columns if c.startswith("Drawdown_")]
        Analysis_Data[drawdown_cols] = Analysis_Data[drawdown_cols].fillna(0.0)

        # === Expiry days difference ===
        Analysis_Data["Ex_to_Day"] = (Analysis_Data["Expiry_Date"] - Analysis_Data["Entry_DateTime"]).dt.days

        # === Add Month / Quarter / Year ===
        Analysis_Data["Month"]   = Analysis_Data["Entry_DateTime"].dt.month
        Analysis_Data["Quarter"] = Analysis_Data["Entry_DateTime"].dt.quarter
        Analysis_Data["Year"]    = Analysis_Data["Entry_DateTime"].dt.year

        # === Convert datetime to string for display ===
        Analysis_Data["Entry_DateTime"] = Analysis_Data["Entry_DateTime"].dt.strftime('%d-%m-%Y %H:%M')
        Analysis_Data["Exit_DateTime"]  = Analysis_Data["Exit_DateTime"].dt.strftime('%d-%m-%Y %H:%M')
        Analysis_Data["Expiry_Date"]    = Analysis_Data["Expiry_Date"].dt.strftime('%d-%m-%Y')

        return Analysis_Data

    except Exception as e:
        print(f"get_Analysis_Data Function Error : {e}")
        return None
# # Example usage
# Analysis_Data = get_Analysis_Data(trade_log)
# print(tabulate(Analysis_Data, headers="keys", tablefmt="pretty", showindex=False))
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice#  get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_StrikePrice(stock_name, Options_Type, ATM, Target_Strike, DateTime = None, Expiry= None, column_Type = "open", Strike_No = 20,):
    try:
        Strike_Gep = ICICI.get_Strike_Gep(stock_name)
        Target_Type = type(Target_Strike)
        if Target_Type in [int,float]:
          Face_values = "options_chain"
          DATA = ICICI.get_Options_Chain(stock_name, DateTime, Expiry, ATM, Strike_No, Face_values, "open")
          Prim_List = DATA[f"{Options_Type.lower()}_{column_Type.lower()}"].tolist() if hasattr(DATA["call_open"], 'tolist') else list(DATA["call_open"])
          nearest_Prim = min(Prim_List, key=lambda x: abs(x - Target_Strike))
          filtered_data = DATA[DATA[f"{Options_Type.lower()}_{column_Type.lower()}"] == nearest_Prim]
          if not filtered_data.empty:
              strike_price =  filtered_data["strike_price"].iloc[0]
              Strike_Data = {"Strike": int(strike_price), "Premium": float(nearest_Prim)}
          else:
                Strike_Data = {"Strike": None, "Premium": None}
          return Strike_Data
        elif Target_Type == str:
          parts = Target_Strike.split('-')
          letters = str(parts[0])
          number = int(parts[1])
          if Options_Type.lower() == "call":
              Value = ATM - (number * Strike_Gep) if letters.lower() == "itm" else ATM + (number * Strike_Gep) if letters.lower() == "otm" else ATM
          elif Options_Type.lower() == "put":
              Value = ATM + (number * Strike_Gep) if letters.lower() == "itm" else ATM - (number * Strike_Gep) if letters.lower() == "otm" else ATM
          return {"Strike": Value, "Premium": None}
    except Exception as e:
        print(f"get_StrikePrice Function Error: {e}")
        return {"Strike": None, "Premium": None}

# Example usage:
# Symbol = "nifty"
# DateTime = "26-12-2024 09:30"
# Expiry = "26-12-2024"
# ATM = 23800
# Options_Type = "call"
# Target_Strike = "ATM-00"  #  "otm-2"
# Strike_Data = get_StrikePrice(Symbol,Options_Type, ATM, Target_Strike, DateTime, Expiry, column_Type = "open", Strike_No = 20, Strike_Gep = 50)
# print(Strike_Data)
# Symbol = "nifty"
# ATM = 23800
# Options_Type = "call"
# Target_Strike = "atm-00"  #  "otm-2", "itm-02" "atm-00"
# Strike_Data = get_StrikePrice(Symbol,Options_Type, ATM, Target_Strike,)["Strike"]
# print(Strike_Data)
#___________________________________________________________________________________________________________________________________________________________________


import os
os.makedirs("BackTest_Data", exist_ok=True)
#  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction
def Backtest_Positional_Function(breeze,Trade_No, Instruments_Detail, DateTime_Detail, Tradeing_Time, Exit_Logic, Index_Data,Note1 = None, Note2 = None):
    Trade_List = []
    stock_name        = str(Instruments_Detail["stock_name"])
    Expiry_Date       = Instruments_Detail["Expiry_Date"]
    Strike_Type       = str(Instruments_Detail["Strike_Type"])
    Options_Type      = str(Instruments_Detail["Options_Type"])
    Transaction_Type  = str(Instruments_Detail["Transaction_Type"])
    Quantity          = int(Instruments_Detail["Quantity"])

    Entry_DateTime    = pandas_date_format(DateTime_Detail["Entry_DateTime"])
    Entry_Date        = Entry_DateTime.strftime("%d-%m-%Y")
    Entry_Time        = Entry_DateTime.strftime("%H:%M")
    Exit_DateTime     = pandas_date_format(DateTime_Detail["Exit_DateTime"])
    Exit_Date         = Exit_DateTime.strftime("%d-%m-%Y")
    Exit_Time         = Exit_DateTime.strftime("%H:%M")

    Trading_StartTime = Tradeing_Time["Start_Time"]
    Trading_EndTime   = Tradeing_Time["End_Time"]

    StopLoss_Percent  = float(Exit_Logic["StopLoss"])
    Target_Percent    = float(Exit_Logic["Target"])
    TSL_Percent       = float(Exit_Logic["TSL"])
    Max_ReEntry       = int(max(Exit_Logic["Re_Entry"], 1))
    if Max_ReEntry > 1 :
      Re_Entry_End_Time = str(Exit_Logic["Re_Entry_End_Time"])
      Re_Entry_End_Date = Get_BTST_Date(breeze,Entry_Date,int(Exit_Logic["Re_Entry_End_Date"]))

    if Index_Data is not None :
       Index_atm = int(Index_Data["Index_atm"])

    Strike_Data   = get_StrikePrice(stock_name, Options_Type, Index_atm, Strike_Type,)
    Strike_Price  = Strike_Data.get("Strike", None)

    StopLoss_condition = ( int(StopLoss_Percent) != 0 )
    Target_condition   = ( int(Target_Percent)   != 0 )
    TSL_condition      = ( int(TSL_Percent)      != 0 )

    DATA = None
    Entry_Price = None
    ReEntry     = 0
    Trade_No    = (Trade_No + 0.1)
    while ReEntry < Max_ReEntry:
        if DATA is None:

            Data_Start_Date = pandas_date_format(Entry_DateTime, output_format="%d-%m-%Y %H:%M")
            Data_End_Date   = pandas_date_format(Exit_DateTime,  output_format="%d-%m-%Y %H:%M")
            lod_Data = Read_Strike_Data(breeze, stock_name, Expiry_Date, Options_Type, Strike_Price, Data_Start_Date, Data_End_Date, interval= "1minute" ,)#Loop_Type = "while")
            # print(lod_Data)
            if lod_Data is not None and not lod_Data.empty:
                DATA = lod_Data
                DATA.to_csv(os.path.join("BackTest_Data", f"{round(Trade_No, 0)}.csv"), index=False)
            else:
               return None
        DATA.columns = [col.lower() for col in DATA.columns]
        DATA['datetime'] = pd.to_datetime(DATA['datetime'], format="%d-%m-%Y %H:%M")
        DATA = DATA[DATA['datetime'] >= Entry_DateTime].copy()
        Data_End = DATA['datetime'].iloc[-1]
        # print(f"\nData_End_1 {Data_End}",f"Exit_DateTime_1 {Exit_DateTime}" )


        Data_End_dt = pandas_date_format(Data_End)
        Trade_DateTime = pandas_date_format(Exit_DateTime)

        # ✅ अगर Exit_DateTime data में मौजूद है या Data_End_dt से पहले है — उसी को रखो
        if Trade_DateTime <= Data_End_dt:
            Final_Exit = Trade_DateTime
            Note2 = ""
        else:
            # ✅ अगर Exit_DateTime data से आगे है, तो Data_End_dt को use करो
            Final_Exit = Data_End_dt
            Note2 = f"Exit_DateTime Updated ({Exit_DateTime} → {Final_Exit.strftime('%d-%m-%Y %H:%M')}) - Data not available till Exit time"
        Exit_DateTime = Final_Exit.strftime("%d-%m-%Y %H:%M")


        # print(f"Data_End_2 {Data_End}",f"Exit_DateTime_2 {Exit_DateTime}" )
        if Entry_Price is None:
           Entry_Price = DATA[f'{Options_Type.lower()}_open'].iloc[0]    #round(float(Entry_Price),2)

        # Calculate StopLoss, Target, and TSL_Point based on Exit_Logic
        if Transaction_Type.lower() == "sell":
            if StopLoss_condition:
               StopLoss  = round(Entry_Price * (1 + StopLoss_Percent/100), 2)
            if Target_condition:
               Target    = round(Entry_Price * (1 - Target_Percent/100), 2)
            if TSL_condition:
               TSL_Point = round(Entry_Price * (TSL_Percent/100), 2)
        elif Transaction_Type.lower() == "buy":
            if StopLoss_condition:
               StopLoss = round(Entry_Price * (1 - StopLoss_Percent/100), 2)
            if Target_condition:
               Target = round(Entry_Price * (1 + Target_Percent/100), 2)
            if TSL_condition:
               TSL_Point = round(Entry_Price * (TSL_Percent/100), 2)

        if StopLoss_condition:
           Exit_Value = StopLoss
           Exit_Type  = "StopLoss"
        TSL_No     = 1
        Exit_Time  = None

        for i in range(len(DATA)):
            datetime     = pd.to_datetime(str(DATA['datetime'].iloc[i]), format="%Y-%m-%d %H:%M:%S")
            date         = datetime.strftime("%d-%m-%Y")
            time         = datetime.strftime("%H:%M")
            Expiry_Date  = pd.to_datetime(str(DATA['expiry_date'].iloc[i]), format="%d-%m-%Y").strftime("%d-%m-%Y")
            open     = float(DATA[f'{Options_Type}_open' ].iloc[i])
            high     = float(DATA[f'{Options_Type}_high' ].iloc[i])
            low      = float(DATA[f'{Options_Type}_low'  ].iloc[i])
            close    = float(DATA[f'{Options_Type}_close'].iloc[i])
            try:
              Strike_Price = int(DATA['strike_price'].iloc[i])
            except:
              Strike_Price = 0

            Expiry_Exit_Time = pd.to_datetime(Exit_DateTime, format="%d-%m-%Y %H:%M") if Exit_DateTime else pd.to_datetime(f"{Expiry_Date} 15:28", format="%d-%m-%Y %H:%M")
            Trading_Start_Time     = pd.to_datetime(f"{date} {Trading_StartTime}", format="%d-%m-%Y %H:%M")
            Trading_End_Time       = pd.to_datetime(f"{date} {Trading_EndTime}", format="%d-%m-%Y %H:%M")
            Trading_Time_condition = (datetime >= Trading_Start_Time) & (datetime <= Trading_End_Time)


            if Transaction_Type.lower() == "sell":
                exit_condition = (datetime >= Expiry_Exit_Time) or \
                                 (StopLoss_condition and (high >= Exit_Value)) or \
                                 (Target_condition and (low  <= Target))
                TSL_condition  = (TSL_condition and (Exit_Value - (TSL_Point * 2)) >= low)
            elif Transaction_Type.lower() == "buy":
                exit_condition = (datetime >= Expiry_Exit_Time) or \
                                 (StopLoss_condition and (low <= Exit_Value)) or \
                                 (Target_condition and (high >= Target) )
                TSL_condition  = (TSL_condition and (Exit_Value + (TSL_Point * 2)) <= high)

            # print(datetime,TSL_condition)
            if Exit_Time is None and exit_condition and Trading_Time_condition :
                Exit_Time = datetime

                Morning_condition_Target   = ( Exit_Time == Trading_Start_Time ) and (
                                             (Target_condition and Transaction_Type.lower() == "sell" and open <= Target) or
                                             (Target_condition and Transaction_Type.lower() == "buy"  and open >= Target) )

                Morning_condition_StopLoss = ( Exit_Time == Trading_Start_Time ) and (
                                             (StopLoss_condition and Transaction_Type.lower() == "sell" and open >= StopLoss) or
                                             (StopLoss_condition and Transaction_Type.lower() == "buy"  and open <= StopLoss) )

                if Morning_condition_StopLoss:
                    Exit_Value = open
                    Exit_Type  = "Morning_StopLoss"
                elif Morning_condition_Target:
                    Exit_Value = open
                    Exit_Type  = "Morning_Target"

                if not (Morning_condition_StopLoss or Morning_condition_Target):
                   if Target_condition and Transaction_Type.lower() == "sell" and low <= Target:
                      Exit_Type  = "Target"
                      Exit_Value = Target
                   elif Target_condition and Transaction_Type.lower() == "buy" and high >= Target:
                      Exit_Type  = "Target"
                      Exit_Value = Target

                if datetime == Expiry_Exit_Time:
                    Exit_Type = "DateTime"
                    Exit_Value = close
                    if Exit_Time == pd.to_datetime(f"{Expiry_Date} 15:25", format="%d-%m-%Y %H:%M"):
                       Exit_Type = "Expiry"

                if Entry_Price is not None and Exit_Value is not None:
                    if Transaction_Type.lower() == "buy":
                        Net_PNL = round((float(Exit_Value) - float(Entry_Price)) * Quantity, 2)
                        Brokerage = Brokerage_Calculate(float(Entry_Price), float(Exit_Value), Quantity, Options_Type)
                    elif Transaction_Type.lower() == "sell":
                        Net_PNL = round((float(Entry_Price) - float(Exit_Value)) * Quantity, 2)
                        Brokerage = Brokerage_Calculate(float(Exit_Value), float(Entry_Price), Quantity, Options_Type)
                    else:
                        raise ValueError("Invalid Transaction_Type. Use 'buy' or 'sell'.")

                PNL = round(Net_PNL - Brokerage, 2)


                Trade_Data = {"Trade_No" : round(Trade_No, 2), "Expiry_Date" : Expiry_Date, "Strike" : Strike_Price,"Options_Type" : Options_Type, "Transaction_Type": Transaction_Type,
                              "Entry_DateTime" : Entry_DateTime.strftime("%d-%m-%Y %H:%M"), "Exit_DateTime" : datetime.strftime("%d-%m-%Y %H:%M"),
                              "Entry_Price" : round(Entry_Price,2), "Exit_Price" : round(Exit_Value,2), "Quantity" : int(Quantity), "Net_PNL" : round(Net_PNL,2),
                              "Brokerage" : round(Brokerage,2), "PNL" : round(PNL,2), "Note1" : Exit_Type, "Note2": Note2 }
                Trade_No += 0.10000000000000
                Trade_List.append(Trade_Data)
                break  # Exit the loop as trade is closed

            elif TSL_condition:
                if Transaction_Type.lower() == "sell":
                    Exit_Value = round(Exit_Value - TSL_Point, 2)
                elif Transaction_Type.lower() == "buy":
                    Exit_Value = round(Exit_Value + TSL_Point, 2)
                Exit_Type = f"TSL_{TSL_No}"
                TSL_No += 1


        # Re-entry logic after exit
        if Trade_List:
           last_trade = Trade_List[-1]
           Re_Entry_DateTime = pd.to_datetime(last_trade["Exit_DateTime"], format="%d-%m-%Y %H:%M")
           Re_Entry_EndTime  = pd.to_datetime(f"{Re_Entry_End_Date} {Re_Entry_End_Time}", format="%d-%m-%Y %H:%M")

           if Re_Entry_DateTime.strftime("%d-%m-%Y") == Entry_Date:
              DATA_reentry = DATA[(DATA['datetime'] > Re_Entry_DateTime) & (DATA['datetime'] <= Re_Entry_EndTime)]
              for i in range(len(DATA_reentry)):
                  Re_high = DATA_reentry[f'{Options_Type}_high'].iloc[i]
                  Re_low = DATA_reentry[f'{Options_Type}_low'].iloc[i]
                  Re_datetime = DATA_reentry['datetime'].iloc[i]

                    # Check if price crosses original entry price
                  if (Transaction_Type == "sell" and Re_high >= Entry_Price and Re_low  <= Entry_Price) or \
                     (Transaction_Type == "buy"  and Re_low  <= Entry_Price and Re_high >= Entry_Price) :
                     Entry_DateTime = Re_datetime
                     ReEntry += 1
                     break
                  elif Re_datetime == Re_Entry_EndTime:
                       ReEntry = Max_ReEntry
                       break
              else:
                  ReEntry = Max_ReEntry
           else:
               ReEntry = Max_ReEntry
        else:
            ReEntry = Max_ReEntry

    return Trade_List
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________
from concurrent.futures import ThreadPoolExecutor, as_completed
from tabulate import tabulate
from tqdm import tqdm
import pandas as pd

# =====================================================================
# 🔹 Single Index candle पर Backtest चलाने वाला Function
# =====================================================================
def run_backtest_for_index(i, Symbol_Data, breeze, Instruments_Detail, Entry_Settings, Exit_Logic, Tradeing_Time):
    try:
        DateTime = pandas_date_format(str(Symbol_Data['datetime'].iloc[i]))
        Date     = pandas_date_format(DateTime, output_format="%d-%m-%Y")
        Time     = pandas_date_format(DateTime, output_format="%H:%M")

        Monthly_Expiry = pandas_date_format(str(Symbol_Data['curr_m_expiry'].iloc[i]), output_format="%d-%m-%Y")
        Current_Expiry = pandas_date_format(str(Symbol_Data['curr_w_expiry'].iloc[i]), output_format="%d-%m-%Y")
        Next_Expiry    = pandas_date_format(str(Symbol_Data['next_w_expiry'].iloc[i]), output_format="%d-%m-%Y")

        Ch_ATM_Strike  = int(Symbol_Data['ch_atm'].iloc[i])
        Fu_ATM_Strike  = int(Symbol_Data['fu_atm'].iloc[i])

        # ---- Entry/Exit Settings ----
        Entry_Time      = Entry_Settings.get("Entry_Time")
        Exit_Time       = Entry_Settings.get("Exit_Time")
        BTST_Day        = Entry_Settings.get("BTST_Day", 0)
        Underlying_from = Entry_Settings.get("Underlying_from", "Cash")

        Entry_DateTime = pandas_date_format(f"{Date} {Entry_Time}")
        Exit_DateTime  = pd.to_datetime(f"{Get_BTST_Date(breeze, Date, BTST_Day)} {Exit_Time}", format="%d-%m-%Y %H:%M")

        # ---- Expiry Type Logic ----
        Expiry_type = Instruments_Detail.get("Expiry_type")
        if Expiry_type == "Monthly_Expiry":
            Expiry_Date = Monthly_Expiry
        elif Expiry_type == "Current_Expiry":
            Expiry_Date = Current_Expiry
        elif Expiry_type == "Next_Expiry":
            Expiry_Date = Next_Expiry
        else:
            Expiry_Date = None

        Inst = Instruments_Detail.copy()
        Inst["Expiry_Date"] = Expiry_Date

        # ---- ATM Strike ----
        ATM_Strike = Ch_ATM_Strike if Underlying_from == "Cash" else Fu_ATM_Strike

        # ---- Entry Time Condition ----
        if "09:15:00" <= Time <= "15:30:00" and Entry_DateTime == DateTime:
            DateTime_Detail = {"Entry_DateTime": Entry_DateTime, "Exit_DateTime": Exit_DateTime}
            Index_Data = {"Index_atm": Ch_ATM_Strike}

            Leg1_Value = Backtest_Positional_Function(breeze,Trade_No=i + 1,Instruments_Detail=Inst,DateTime_Detail=DateTime_Detail,
                                                       Tradeing_Time=Tradeing_Time,Exit_Logic=Exit_Logic,Index_Data=Index_Data,Note1=None,Note2=None)

            if Leg1_Value:
                return {"Success": True, "Trades": Leg1_Value}
            else:
                return {"Success": False, "Error": {"Expiry_Date": Expiry_Date, "Entry_DateTime": Entry_DateTime, "Leg": "Leg1"}}
        return None

    except Exception as e:
        return {"Success": False, "Error": {"Index": i, "Error": str(e)}}


# =====================================================================
# 🔹 Parallel Backtest (Multi-Threaded)
# =====================================================================
def parallel_backtest(breeze, Symbol_Data, Instruments_Detail, Entry_Settings, Exit_Logic, Tradeing_Time, max_workers=20):
    trade_log = []
    Error_list = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_backtest_for_index, i, Symbol_Data, breeze, Instruments_Detail, Entry_Settings, Exit_Logic, Tradeing_Time)
                   for i in range(len(Symbol_Data))]
        for f in tqdm(as_completed(futures), total=len(futures), desc="Processing in Parallel", unit="symbol"):
            result = f.result()
            if result:
                if result.get("Success"):
                    trade_log.extend(result["Trades"])
                elif result.get("Error"):
                    Error_list.append(result["Error"])
    return trade_log, Error_list  # ⬅️ अब सिर्फ़ data return होगा
# =====================================================================
# 🔹 Multi-Leg Management Functions
# =====================================================================
leg_list = []
leg_No = 0
def leg_list_No_Clear() :
    global leg_list
    global leg_No
    leg_list = []
    leg_No = 0
def Red_leg_list():
    global leg_list
    return leg_list
    
def get_Leg_List_add(Entry_Settings, Instruments_Detail, Exit_Logic, Tradeing_Time):
    global leg_No
    leg_No += 1
    Leg_Value = {"leg_No": leg_No,"Instruments_Detail": Instruments_Detail,"Exit_Logic": Exit_Logic,"Entry_Settings": Entry_Settings,"Tradeing_Time": Tradeing_Time}
    leg_list.append(Leg_Value)
    print(f"✅ Leg No {leg_No} जोड़ा गया")
def get_Leg_List_remove(remove_leg_no):
    global leg_list
    before = len(leg_list)
    leg_list = [leg for leg in leg_list if leg["leg_No"] != remove_leg_no]
    after = len(leg_list)
    if before == after:
        print(f"❌ Leg No {remove_leg_no} नहीं मिला")
    else:
        print(f"✅ Leg No {remove_leg_no} हटा दिया गया")

# =====================================================================
# 🔹 Backtest Function (सब Leg को Parallel Run कराना + Report Generate करना)
# =====================================================================
def BackTest(breeze, stock_name, Start_Date, End_Date, leg_list):
    Symbol_Data = get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute", Loop_Type="for")
    print(f"\n🔹 Total Candles Loaded: {len(Symbol_Data)}")
    print(f"🔹 Total Legs: {len(leg_list)}\n")

    All_Trades = []
    All_Errors = []

    for leg in leg_list:
        Instruments_Detail = leg["Instruments_Detail"]
        Exit_Logic         = leg["Exit_Logic"]
        Entry_Settings     = leg["Entry_Settings"]
        Tradeing_Time      = leg["Tradeing_Time"]

        print(f"🚀 Running Backtest for Leg {leg['leg_No']} ...")
        trade_log, Error_list = parallel_backtest(breeze, Symbol_Data, Instruments_Detail, Entry_Settings, Exit_Logic, Tradeing_Time, max_workers=50)

        All_Trades.extend(trade_log)
        All_Errors.extend(Error_list)
        print(f"✅ Leg {leg['leg_No']} Completed!\n")

    # ---- Save Results ----
    if All_Trades:
        Analysis_Data = get_Analysis_Data(All_Trades)
        Error = pd.DataFrame(All_Errors)
        Excel_File_Name = f"Backtest_Report_{stock_name}.xlsx"

        with pd.ExcelWriter(Excel_File_Name, engine="xlsxwriter") as writer:
            Analysis_Data.to_excel(writer, sheet_name="All_trade_log", index=False)
            Error.to_excel(writer, sheet_name="Error", index=False)

        print("\n✅ Reports generated and saved successfully!")
        # print("\n📘 trade_log (Top 5 rows):")
        # print(tabulate(Analysis_Data.head(5), headers="keys", tablefmt="pretty", showindex=False))
        return Analysis_Data
    else:
        print("\n⚠️ No trades executed.")


# =====================================================================
# 🔹 Example Run
# =====================================================================
# stock_name = "nifty"
# Start_Date = "01-10-2025"
# End_Date   = "13-10-2025"
# Entry_Settings     = {"Underlying_from": "Cash", "Entry_Time": "09:25", "Exit_Time": "09:16", "BTST_Day": 1}
# Instruments_Detail = {"stock_name": stock_name,"Expiry_type": "Next_Expiry","Strike_Type": "atm-00","Options_Type": "call","Transaction_Type": "sell","Quantity": 75}
# Exit_Logic         = {"StopLoss": 10, "Target": 0, "TSL": 0, "Re_Entry": 4, "Re_Entry_End_Time": "15:29", "Re_Entry_End_Date": 0}
# Tradeing_Time      = {"Start_Time": "09:16", "End_Time": "15:30"}

# # ➕ Add one leg
# get_Leg_List_add(Entry_Settings, Instruments_Detail, Exit_Logic, Tradeing_Time)

# # 🔍 Show all legs
# print("\n🟢 All Legs:")
# print(tabulate(leg_list, headers="keys", tablefmt="psql"))

# # 🚀 Run Backtest
# Data = BackTest(breeze, stock_name, Start_Date, End_Date, leg_list)
# print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))




