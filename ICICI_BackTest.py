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
