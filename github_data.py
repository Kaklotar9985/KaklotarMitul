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
                            '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025', '09-04-2025', '17-04-2025', '24-04-2025', '30-04-2025', '08-05-2025', '15-05-2025', '22-05-2025', '29-05-2025', '05-06-2025', '12-06-2025', '19-06-2025', '26-06-2025', '03-07-2025', '10-07-2025', '17-07-2025', '24-07-2025', '31-07-2025', '07-08-2025', '14-08-2025', '21-08-2025', '28-08-2025', '02-09-2025', '09-09-2025', '16-09-2025', '23-09-2025', '30-09-2025', '07-10-2025', '14-10-2025', '20-10-2025', '28-10-2025', '04-11-2025', '11-11-2025', '18-11-2025', '25-11-2025', '02-12-2025', '09-12-2025', '16-12-2025', '23-12-2024', '30-12-2024',  ]

Strike_Gep_List          = {"nifty" : 50, "nifty bank" : 100, "reliance" :10}
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
# Symbol = "nifty"  #  nifty , bank nifty
# Strike_Gep = get_Strike_Gep(Symbol)
# print(Strike_Gep)
#_____________________________________________________________________________________________________________________________________________________

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry    get_Expiry   get_Expiry
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import calendar
import pandas as pd
def get_Symbol_Expiry(Dates=None, Symbol=None, Expiry_Period=None, Expiry_Type=None, Start_Date=None, End_Date=None):
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
            Date = pandas_date_format(Dates)
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
            Start_Date = pandas_date_format(Start_Date).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            End_Date = pandas_date_format(End_Date)
            last_day = calendar.monthrange(End_Date.year, End_Date.month)[1]
            last_day = End_Date.replace(day=last_day, hour=23, minute=59, second=59, microsecond=0)
            filtered = Expiry_List[(Expiry_List >= Start_Date) & (Expiry_List <= last_day)]
            last_Expiry = filtered.iloc[-1]
            Total_day = (last_Expiry - End_Date).days
            if Total_day < 0:
                filtered = Expiry_List[(Expiry_List >= Start_Date) & (Expiry_List <= (last_day + timedelta(days=30)))]
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
# End_Date   = "28-10-2025"
# Expirys        = get_Symbol_Expiry(Dates, Symbol, Expiry_Period, Expiry_Type, Start_Date, End_Date)
# print(Expirys)
#=========================================================================================================================================================================================================================================================================================

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
import pandas as pd
from datetime import datetime
def pandas_date_format(date_input, output_format=None):
    format_list = [
        "%d-%b-%Y %H:%M", "%d-%b-%Y %H:%M:%S",
        "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S",
        "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S",
        "%d-%b-%Y", "%d-%m-%Y", "%Y-%m-%d"]

    # 🔹 Helper function for parsing a single value
    def parse_single_date(value):
        if pd.isna(value):
            return pd.NaT
        if isinstance(value, datetime):
            return value
        value = str(value).strip()
        for fmt in format_list:
            try:
                return datetime.strptime(value, fmt)
            except Exception:
                continue
        try:
            return pd.to_datetime(value, dayfirst=True, errors="coerce")
        except Exception:
            return pd.NaT

    # 🔹 If it's a Pandas Series
    if isinstance(date_input, pd.Series):
        parsed_series = date_input.apply(parse_single_date)
        return parsed_series.dt.strftime(output_format) if output_format else parsed_series

    # 🔹 If it's a list
    if isinstance(date_input, list):
        return [pandas_date_format(d, output_format) for d in date_input]

    # 🔹 Single Value
    parsed_date = parse_single_date(date_input)
    if parsed_date is pd.NaT:
        return date_input
    return parsed_date.strftime(output_format) if output_format else parsed_date
# Example
# date = "2025-10-01 09:15:00"
# output_format = "%d-%m-%Y %H:%M"
# formatted_date = pandas_date_format(date, output_format)
# print(formatted_date)   #Error: Can only use .dt accessor with datetimelike values
#=========================================================================================================================================================================================================================================================================================

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_API_limit   rate_limiter   get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter  get_API_limit   rate_limiter
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
import pandas as pd
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
from datetime import datetime, timedelta   # ⚠️ कोई डेटा नहीं मिला!
import pandas as pd
import time
def get_historical_data_API(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price,
                            max_retries=3, delay=1,stock_name="No",Loop_Type = None):
    attempt = 0
    right_Data = None
    while attempt < max_retries:
        try:
            Start_Date = pandas_date_format(Start_Date)
            End_Date   = pandas_date_format(End_Date)
            Expiry_Date= pandas_date_format(Expiry_Date)
            rate_limiter()  # ✅ Rate limit check
            Start_Date1      = (Start_Date - timedelta(days=5))
            End_Date1        = (End_Date + timedelta(days=1))
            from_date_api   = Start_Date1.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date_api     = End_Date1.strftime("%Y-%m-%dT%H:%M:%S.000Z")                   #.strftime("%Y-%m-%dT00:00:00.000Z")  strftime("%Y-%m-%dT%H:%M:%S.000Z")
            expiry_date_api = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            # API Call
            right_Data = breeze.get_historical_data_v2(interval=interval,from_date=from_date_api,to_date=to_date_api,stock_code=stock_code,exchange_code=exchange_code,
                                                       product_type=product_type,expiry_date=expiry_date_api,right=Options_Type,strike_price=int(strike_price)  )

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
                        Data["datetime"] = Data["datetime"].apply(pandas_date_format)
                        if Loop_Type == "for":
                            Data = Data[(Data["datetime"] >= dt.datetime.combine(Start_Date, dt.time(9, 15, 0))) &
                                        (Data["datetime"] <= dt.datetime.combine(End_Date, dt.time(15, 30, 0)))]
                            Data = Data.sort_values(by="datetime").reset_index(drop=True)
                        Data["datetime"] = pandas_date_format(Data["datetime"],output_format = "%d-%m-%Y %H:%M")
                        if "expiry_date" in Data.columns:
                            Data["expiry_date"] = Data["expiry_date"].apply(pandas_date_format)
                            Data["expiry_date"] = pandas_date_format(Data["expiry_date"],output_format = "%d-%m-%Y")
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
                        # else:
                        #    print(f"{Start_Date} to {End_Date} कोई डेटा नहीं मिला!")
                        return Data
                    else:
                        print(f"{Start_Date} to {End_Date} कोई डेटा नहीं मिला!")
                        return None
                else:
                  print(f"{Start_Date} to {End_Date} कोई डेटा नहीं मिला!")
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
    return None
# # Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         stock_code    = get_Stock_Name(breeze, "NSE", stock_name)
#         exchange_code = "NFO"             # "NFO" "NSE"
#         product_type  = "options"         # "options", "futures", "cash"
#         Options_Type  = "call"            # "others" , "call" , "put"
#         strike_price  =  strike_price     # integer, not string
#         interval      = "1minute"         # "1second", "1minute", "5minute", "30minute" , "1day".
#         Start_Date    = "01-09-2025"
#         End_Date      = "10-09-2025"
#         Expiry_Date   = "30-09-2025"
#         data = get_historical_data_API(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, max_retries=3, delay=1)
#         print(tabulate(pd.concat([data.head(3), data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop  fetch_options_while_loop   fetch_options_while_loop  fetch_options_while_loop   fetch_options_while_loop     fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import timedelta
import datetime as dt
import time
def fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name="No"):
    final_df = pd.DataFrame()
    Start_Date = pandas_date_format(Start_Date)
    End_Date   = pandas_date_format(End_Date)
    Expiry_Date= pandas_date_format(Expiry_Date)
    current_to = End_Date
    while current_to >= Start_Date:
        Data = get_historical_data_API( breeze, interval, Start_Date, current_to, stock_code, exchange_code, product_type,
                                                Expiry_Date, Options_Type, strike_price,max_retries=3, delay=0,stock_name=stock_name)
        if Data is not None and not Data.empty:
            final_df = pd.concat([Data, final_df], ignore_index=True)
            Data["datetime_dt"] = pandas_date_format(Data["datetime"])
            first_time = Data["datetime_dt"].min()
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
        time.sleep(0.0001)         # API rate-limit से बचने के लिए
    if not final_df.empty:
      final_df["datetime"]    = pandas_date_format(final_df["datetime"])
      if "expiry_date" in final_df.columns:
          final_df["expiry_date"] = pandas_date_format(final_df["expiry_date"])

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
      final_df["datetime"] = pandas_date_format(final_df["datetime"], output_format = "%d-%m-%Y %H:%M")
      if "expiry_date" in final_df.columns:
         final_df["expiry_date"] = pandas_date_format(final_df["expiry_date"], output_format = "%d-%m-%Y")
    return final_df

# Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         stock_code    = get_Stock_Name(breeze, "NSE", stock_name)
#         exchange_code = "NFO"             # "NFO" "NSE"
#         product_type  = "options"         # "options", "futures", "cash"
#         Options_Type  = "call"            # "others" , "call" , "put"
#         strike_price  =  strike_price     # integer, not string
#         interval      = "1minute"         # "1second", "1minute", "5minute", "30minute" , "1day".
#         Start_Date    = "01-09-2025"
#         End_Date      = "10-09-2025"
#         Expiry_Date   = "30-09-2025"
#         while_Data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
#         print(tabulate(pd.concat([while_Data.head(3), while_Data.tail(3)]), headers='keys', tablefmt='psql'))
#         print("While Loop Data Shape:", while_Data.shape)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_market_open_dates   get_market_open_dates     get_market_open_dates  get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates     get_market_open_dates
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import timedelta, datetime
import pandas as pd
market_open_dates = None
def get_market_open_dates(breeze):
    global market_open_dates
    try:
      if market_open_dates is None:
          Start_Date = pandas_date_format("01-01-2021")
          today = datetime.now()
          End_Date = today.strftime("%d-%m-%Y")
          expiry_dt = pandas_date_format(End_Date)
          data = fetch_options_while_loop(breeze,"30minute",Start_Date, today,"Nifty","NSE","cash", expiry_dt,"others",0,"Nifty")
          unique_dates = pd.to_datetime(data["datetime"], dayfirst=True).dt.strftime("%d-%m-%Y").unique().tolist()
          date_list = [] #[(today + timedelta(days=i)).strftime("%d-%m-%Y")for i in range(16)if (today + timedelta(days=i)).weekday() < 5]
          all_dates = sorted(set(unique_dates + date_list),key=lambda x: datetime.strptime(x, "%d-%m-%Y"))
          market_open_dates = all_dates
    except Exception as e:
        print(f"Error fetching market open dates: {e}")
        market_open_dates = None
# Example usage
# get_market_open_dates(breeze)
# print(market_open_dates)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date   Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Get_BTST_Date(breeze, Date=None, Get_Day_No=None, Start_Date=None, End_Date=None):
    global market_open_dates
    try:
        if market_open_dates is None:
            get_market_open_dates(breeze)
        if Date is not None and Get_Day_No is not None:
            if Get_Day_No == 0:
               return Date
            Date = pandas_date_format(Date)
            market_open = pandas_date_format(pd.Series(market_open_dates))
            filtered_dates = market_open[market_open > Date].sort_values()
            filtered_dates = filtered_dates.dt.strftime("%d-%m-%Y").tolist()
            get_Date = filtered_dates[(int(Get_Day_No) - 1)]
            if len(filtered_dates) < int(Get_Day_No):
               get_Date = Date.strftime("%d-%m-%Y")
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
# BTST_Date_List = Get_BTST_Date(breeze, Start_Date="10-10-2025 09:25", End_Date="14-10-2025 09:19")
# print(BTST_Date_List)
# BTST_Date = Get_BTST_Date(breeze, Date = "10-10-2025", Get_Day_No = 1)
# print(BTST_Date)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop  fetch_options_For_loop   fetch_options_For_loop     fetch_options_while_loop   fetch_options_while_loop   fetch_options_while_loop
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch_options_For_loop(breeze, interval, Start_Date, End_Date,stock_code, exchange_code, product_type,Expiry_Date, Options_Type, strike_price, stock_name="No", date_list = None):
    final_df = pd.DataFrame()
    Start_Date = pandas_date_format(Start_Date)
    End_Date   = pandas_date_format(End_Date)
    Expiry_Date= pandas_date_format(Expiry_Date)
    if date_list is None:
       date_list = Get_BTST_Date(breeze, Start_Date=Start_Date, End_Date=End_Date)
       if not date_list:
          date_list = []
          current_date = Start_Date.date()
          while current_date <= End_Date.date():
              if current_date.weekday() < 5:
                  date_list.append(current_date)
              current_date += timedelta(days=1)
          date_list = sorted(date_list, reverse=True)
    else:
      Start_Date = pandas_date_format("01-01-2021")
      End_Date   = pandas_date_format("01-01-2030")

    date_list = pandas_date_format(date_list)  # (pd.Series(date_list))
    # print("🗓️ Dates to Fetch:", date_list)
    Error_Date = []
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(200, len(date_list)))) as executor:
        futures = {executor.submit(get_historical_data_API, breeze, interval,
                   dt.datetime.combine(date, dt.time(9, 15, 0)),dt.datetime.combine(date, dt.time(15, 30, 0)),
                   stock_code, exchange_code, product_type,Expiry_Date,Options_Type,strike_price, 3, 0, stock_name, Loop_Type = "for"): date for date in date_list }

        for future in as_completed(futures):
            date = futures[future]
            try:
                Data = future.result()
                if isinstance(Data, pd.DataFrame) and not Data.empty:
                   results.append(Data)
                else:
                   Error_Date.append(date.strftime("%d-%m-%Y"))
            except Exception as e:
                print(f"❌ Error fetching {date}: {e}")

    # ✅ Combine & clean
    if results:
        final_df = pd.concat(results, ignore_index=True)
        final_df["datetime"]    = pandas_date_format(final_df["datetime"])
        if "expiry_date" in final_df.columns:
            final_df["expiry_date"] = pandas_date_format(final_df["expiry_date"])

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
        final_df["datetime"] = pandas_date_format(final_df["datetime"], output_format = "%d-%m-%Y %H:%M")
        if "expiry_date" in final_df.columns:
          final_df["expiry_date"] = pandas_date_format(final_df["expiry_date"], output_format = "%d-%m-%Y")
    print("📅 Error Dates:", Error_Date)
    return final_df

# Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         stock_code    = get_Stock_Name(breeze, "NSE", stock_name)
#         exchange_code = "NFO"             # "NFO" "NSE"
#         product_type  = "options"         # "options", "futures", "cash"
#         Options_Type  = "call"            # "others" , "call" , "put"
#         strike_price  =  strike_price     # integer, not string
#         interval      = "1minute"         # "1second", "1minute", "5minute", "30minute" , "1day".
#         Start_Date    = "15-09-2025"
#         End_Date      = "16-09-2025"
#         Expiry_Date   = "30-09-2025"
#         date_list     = None #['15-09-2025', '17-09-2025']
#         For_Data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name, date_list)
#         print(tabulate(pd.concat([For_Data.head(3), For_Data.tail(3)]), headers='keys', tablefmt='psql'))
#         print("For Loop Data Shape:", For_Data.shape)
#         while_Data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
#         print(tabulate(pd.concat([while_Data.head(3), while_Data.tail(3)]), headers='keys', tablefmt='psql'))
#         print("While Loop Data Shape:", while_Data.shape)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_start_end_expiry_formet   get_start_end_expiry_formet     get_start_end_expiry_formet  get_start_end_expiry_formet     get_start_end_expiry_formet     get_start_end_expiry_formet     get_start_end_expiry_formet     get_start_end_expiry_formet      get_start_end_expiry_formet   get_start_end_expiry_formet
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
def get_start_end_expiry_formet(Expiry_Date: str, Start_Date, End_Date):
    Expiry_Date = pandas_date_format(Expiry_Date)
    # 🔹 Start Date Handling
    if isinstance(Start_Date, (int, float, str)) and not isinstance(Start_Date, datetime):
        try:
            Days_Before_Expiry = float(Start_Date)
            Start_Date = (Expiry_Date - timedelta(days=Days_Before_Expiry)).replace(hour=0, minute=0, second=0)
        except ValueError:
            Start_Date = pandas_date_format(Start_Date)
    elif not isinstance(Start_Date, datetime):
        Start_Date = pandas_date_format(Start_Date)
    # 🔹 End Date Handling
    if isinstance(End_Date, (int, float, str)) and not isinstance(End_Date, datetime):
        try:
            End_Days = float(End_Date)
            if End_Days <= 0:
                End_Date = Expiry_Date
            else:
                End_Date = (Start_Date + timedelta(days=End_Days)).replace(hour=0, minute=0, second=0)
        except ValueError:
            End_Date = pandas_date_format(End_Date)
    elif not isinstance(End_Date, datetime):
        End_Date = pandas_date_format(End_Date)
    # 🔸 Ensure End_Date not beyond expiry
    if End_Date > Expiry_Date:
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
def Read_Strike_Data(breeze, stock_name, Expiry_Date=None, Options_Type=None, strike_price=None, Start_Date = 60, End_Date = 0, interval = "1minute", Loop_Type = "for", date_list=None ):
    stock_code = get_Stock_Name(breeze, "NSE", stock_name)
    Expiry_Date, Start_Date, No = get_start_end_expiry_formet(Expiry_Date, Start_Date, End_Date)

    # ========================= CASH =========================
    if Options_Type == "ch":
        exchange_code = "NSE"
        product_type = "cash"
        option_type = "others"
        Expiry_Date =  End_Date #datetime.strptime("01-01-2000", "%d-%m-%Y")
        strike_price = 0
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name, date_list)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= FUTURES =========================
    elif Options_Type == "fu":
        exchange_code = "NFO"
        product_type = "futures"
        option_type = "others"
        strike_price = 0
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name, date_list)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= CALL OPTIONS =========================
    elif Options_Type == "call":
        exchange_code = "NFO"
        product_type = "options"
        option_type = "call"
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name, date_list)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    # ========================= PUT OPTIONS =========================
    elif Options_Type == "put":
        exchange_code = "NFO"
        product_type = "options"
        option_type = "put"
        if Loop_Type == "for":
            data = fetch_options_For_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name, date_list)
        elif Loop_Type == "while":
            data = fetch_options_while_loop(breeze, interval, Start_Date, End_Date, stock_code, exchange_code, product_type, Expiry_Date, Options_Type, strike_price, stock_name)
    else:
        print("❌ Invalid Option Type! (Use: 'ch', 'fu', 'call', 'put', or 'op')")
        return
    # ========================= PRINT FINAL TABLE =========================
    if not data.empty:
        return data
        # print(tabulate(pd.concat([data.head(3), data.tail(3)]), headers="keys", tablefmt="psql"))
    # else:
    #     print(f"{Start_Date} to {End_Date} कोई डेटा नहीं मिला!")


# # interval =  "1second", "1minute", "5minute", "30minute" , "1day".
# # Loop_Type = "for"
# # 🔹 Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         Expiry_Date  = "28-10-2025"
#         Options_Type = "call"                # 'ch', 'fu', 'call', 'put', 'op'
#         Start_Date   = "21-10-2025"
#         End_Date     = "28-10-2025"
#         interval     = "1minute"
#         date_list    = ['26-10-2025', '28-10-2025']
#         data = Read_Strike_Data(breeze, stock_name=stock_name, Expiry_Date=Expiry_Date, Options_Type=Options_Type, strike_price=strike_price,
#                                 Start_Date=Start_Date, End_Date=End_Date, date_list=date_list)
#         print(tabulate(pd.concat([data.head(3), data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================






from datetime import datetime, timedelta  # #
from tabulate import tabulate
from io import StringIO
import pandas as pd
import requests
import base64
import time
import os
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# GitHub_rate_limiter   GitHub_rate_limiter   GitHub_GitHub_rate_limiter   GitHub_rate_limiter  GitHub_GitHub_rate_limiter   GitHub_rate_limiter  GitHub_GitHub_rate_limiter   GitHub_rate_limiter  GitHub_GitHub_rate_limiter   GitHub_rate_limiter  GitHub_GitHub_rate_limiter   GitHub_rate_limiter
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
GitHub_API_CALL_LIMIT = 5000       # GitHub authenticated limit per hour
GitHub_API_Call_Count = 0
GitHub_API_Start_Time = time.time()
def GitHub_set_api_limit(limit):
    global GitHub_API_CALL_LIMIT
    GitHub_API_CALL_LIMIT = limit
def GitHub_rate_limiter():
    global GitHub_API_Call_Count, GitHub_API_Start_Time
    now = time.time()
    elapsed = now - GitHub_API_Start_Time
    if elapsed >= 3600:
        GitHub_API_Call_Count = 0
        GitHub_API_Start_Time = now
    GitHub_API_Call_Count += 1
    if GitHub_API_Call_Count > GitHub_API_CALL_LIMIT:
        sleep_time = 3600 - elapsed
        if sleep_time > 0:
            print(f"⏳ GitHub API limit reached → Waiting for {int(sleep_time)} seconds...")
            time.sleep(sleep_time)
        # Reset after waiting
        GitHub_API_Call_Count = 1
        GitHub_API_Start_Time = time.time()

# # Example usage
# for i in range(5001):   # 15 बार call करेंगे
#     GitHub_rate_limiter()
#     clear_output(wait=True)
#     print(f"API Call {i+1} done at {time.strftime('%H:%M:%S')}")
#     time.sleep(0.005)   # हर call के बीच 0.5s का gap रखा      
#=======================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github#  upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github   upload_csv_to_github
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete_github_folder(GitHub_API, path):
    headers   = GitHub_API['headers']
    owner     = GitHub_API['owner']
    repo_name = GitHub_API['repo_name']
    GitHub_rate_limiter()
    # Step 1: Get folder info
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Folder '{path}' नहीं मिला या Error: {response.status_code}")
        return
    items = response.json()
    if not isinstance(items, list):
        items = [items]
    # Step 2: हर file को individually delete करें
    for item in items:
        sha = item["sha"]
        file_path = item["path"]
        del_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}"
        data = {"message": f"Delete {file_path}","sha": sha}
        del_response = requests.delete(del_url, headers=headers, json=data)
        if del_response.status_code == 200:
            print(f"🗑️ Deleted: {file_path}")
        else:
            print(f"⚠️ Failed to delete {file_path}: {del_response.status_code}, {del_response.text}")

# # Example usage:
# delete_github_folder(GitHub_API,"nifty/2025/1/24-1-2025")
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  create_github_folder   create_github_folder   create_github_folder   create_github_folder   create_github_folder   create_github_folder#  create_github_folder   create_github_folder   create_github_folder   create_github_folder   create_github_folder   create_github_folder   create_github_folder
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests, base64, time, json, os, re
def create_github_folder(GitHub_API, path, Print=None, retry=5):
    headers   = GitHub_API['headers']
    owner     = GitHub_API['owner']
    repo_name = GitHub_API['repo_name']
    GitHub_rate_limiter()
    # प्रत्येक folder को README.md से represent किया जाएगा
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{path}/README.md"
    content = base64.b64encode(b"This is an auto-created folder").decode("utf-8")
    data = {"message": f"Create folder {path}", "content": content}

    for attempt in range(1, retry + 1):
        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 201:    # ✅ Successfully created
            print(f"✅ Folder '{path}' बनाया गया।")
            return True
        elif response.status_code == 422: # ⚠️ Already exists
            if Print == "Yas":
                print(f"⚠️ Folder '{path}' पहले से मौजूद है।")
            return True
        elif response.status_code == 409: # 🔄 SHA Conflict Recovery
            print(f"⚠️ SHA conflict (409) for '{path}', attempt {attempt}/{retry} → re-syncing SHA...")
            time.sleep(1.5)
            # Fetch repo latest tree SHA to resync
            repo_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/refs/heads/main"
            repo_resp = requests.get(repo_url, headers=headers)
            if repo_resp.status_code == 200:
                latest_sha = repo_resp.json().get("object", {}).get("sha", None)
                if latest_sha:          # Just wait before retry (since SHA tree is internal to GitHub)
                    time.sleep(1.5)
                    continue
            else:
                print(f"⚠️ Unable to fetch latest SHA for recovery ({repo_resp.status_code})")
                continue
        elif response.status_code == 200: # ℹ️ Updated existing file
            print(f"ℹ️ Folder '{path}' update हुआ (already exists).")
            return True
        else: # ❌ Other errors
            print(f"❌ Error creating folder '{path}': {response.status_code} → {response.text}")
            time.sleep(2)
            continue

    print(f"❌ Folder '{path}' create नहीं हो पाया (after {retry} retries).")
    return False
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder#  Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder   Symbol_Create_folder
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Symbol_Create_folder(GitHub_API, main_folder, year_folder=None, month_folder=None, expiry_folder=None):
    paths = [main_folder]
    if year_folder:
        paths.append(f"{main_folder}/{year_folder}")
    if month_folder:
        paths.append(f"{main_folder}/{year_folder}/{month_folder}")
    if expiry_folder:
        paths.append(f"{main_folder}/{year_folder}/{month_folder}/{expiry_folder}")
    for path in paths:
        created = create_github_folder(GitHub_API, path)
        time.sleep(1)  # GitHub को commit sync करने का समय दें
#=========================================================================================================================================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Upload_GitHub_Options_Data (Auto-Recovery Version)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Upload_GitHub_Options_Data(GitHub_API, local_path, max_retry=5, wait_time=2):
    headers   = GitHub_API['headers']
    owner     = GitHub_API['owner']
    repo_name = GitHub_API['repo_name']
    GitHub_rate_limiter()
    parts = local_path.split("/")                                 # Split by "/"
    stock_name = parts[0]                                         # stock name
    file_name = parts[1].replace(".csv.gz", "")                   # remove extension
    expiry_date, strike_price, option_type = file_name.split("_") # Split filename by "_"
    day, month, year = expiry_date.split("-")                     # Extract year and month

    # ✅ Folder structure ensure करें
    Symbol_Create_folder(GitHub_API, main_folder = stock_name , year_folder = year, month_folder = month, expiry_folder = expiry_date)

    file_name = os.path.basename(local_path)
    github_path = f"{stock_name}/{year}/{month}/{expiry_date}/{file_name}"
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{github_path}"

    # ✅ File को Base64 encode करें
    with open(local_path, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")

    for attempt in range(1, max_retry + 1):
        get_resp = requests.get(url, headers=headers) # ✅ पहले check करें file पहले से है या नहीं
        if get_resp.status_code == 200:
            sha = get_resp.json().get("sha", None)
            data = {"message": f"Update CSV {file_name}", "content": encoded_content, "sha": sha}
        else:
            data = {"message": f"Upload CSV {file_name}", "content": encoded_content}
        response = requests.put(url, headers=headers, json=data)


        if response.status_code in [200, 201]: # ✅ Success (upload or update)
            print(f"✅ '{file_name}' uploaded/updated successfully → {github_path}")
            return True
        elif response.status_code == 409: # 🔁 409 Conflict - SHA mismatch or race condition
            print(f"⚠️ SHA conflict (409) for '{file_name}', retrying... ({attempt}/{max_retry})")
            time.sleep(wait_time)
            ref_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/refs/heads/main" # Fetch latest repo SHA for re-sync
            ref_resp = requests.get(ref_url, headers=headers)
            if ref_resp.status_code == 200:
                latest_sha = ref_resp.json().get("object", {}).get("sha")
                if latest_sha:
                    print(f"🔄 Synced latest repo SHA: {latest_sha[:8]}…")
            continue
        elif response.status_code in [502, 503, 504]: # ⚠️ Temporary server error (rate limit etc.)
            print(f"⚠️ Temporary GitHub error {response.status_code}, waiting {wait_time}s and retrying...")
            time.sleep(wait_time)
            continue
        else: # ❌ Any other error
            print(f"❌ Upload failed! {response.status_code}: {response.text}")
            time.sleep(wait_time)
            continue

    print(f"❌ Upload failed permanently after {max_retry} retries → {github_path}")
    return False

# # # Example usage
# # local_path = "nifty/28-10-2025_24700_call.csv.gz"
# # Upload_GitHub_Options_Data(GitHub_API, local_path,)
# #=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data#  Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data   Read_GitHub_Options_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests, gzip, pandas as pd
from io import BytesIO, StringIO
import re, datetime as dt, base64

session = requests.Session()
def Read_GitHub_Options_Data(GitHub_API, stock_name, Expiry_Date, strike_price,
                             Options_Type, Start_Date=None, End_Date=None):
    headers   = GitHub_API['headers']
    owner     = GitHub_API['owner']
    repo_name = GitHub_API['repo_name']
    GitHub_rate_limiter()
    safe_stock = re.sub(r'[^A-Za-z0-9_-]', '_', stock_name.lower())
    Expiry_Date = pandas_date_format(Expiry_Date, "%d-%m-%Y")
    day, month, year = Expiry_Date.split("-")
    if Options_Type.lower() in ["fu", "ch"]:
        strike_price = 0

    file_name = f"{Expiry_Date}_{strike_price}_{Options_Type.lower()}.csv.gz"
    github_path = f"{safe_stock}/{year}/{month}/{Expiry_Date}/{file_name}"
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{github_path}"
    api_resp = session.get(api_url, headers=headers)
    if api_resp.status_code != 200:
        print(f"❌ File Not Found in GitHub: {github_path}")
        return None

    # Step 2: Get Raw Download URL from API JSON
    download_url = api_resp.json().get("download_url")
    if not download_url:
        print("❌ No download_url in API response!")
        return None
    raw_resp = session.get(download_url)
    if raw_resp.status_code != 200:
        print(f"❌ RAW Download Failed: {download_url}")
        return None
    csv_data = gzip.decompress(raw_resp.content).decode("utf-8")
    df = pd.read_csv(StringIO(csv_data))
    # Step 6: Fast datetime processing
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"], dayfirst=True, errors="coerce")
        df = df.dropna(subset=["datetime"])
        if Start_Date:
            Start_Date = pd.to_datetime(Start_Date,dayfirst=True, errors="coerce")
            df = df[df["datetime"] >= pd.to_datetime(Start_Date)]
        if End_Date:
            End_Date = pd.to_datetime(End_Date,dayfirst=True, errors="coerce")
            if End_Date.time() == dt.time(0, 0):
                End_Date = dt.datetime.combine(End_Date.date(), dt.time(15, 30))
            df = df[df["datetime"] <= End_Date]
        df["datetime"] = df["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    if "expiry_date" in df.columns:
        df["expiry_date"] = (pd.to_datetime(df["expiry_date"], dayfirst=True, errors="coerce").dt.strftime("%d-%m-%Y"))
    return df

# # Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"Reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         Expiry_Date  = "28-10-2025"
#         Options_Type = "call"                # 'ch', 'fu', 'call', 'put', 'op'
#         Start_Date   = "01-09-2025"
#         End_Date     = "28-10-2025"
#         Data = Read_GitHub_Options_Data(GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date, End_Date)
#         if Data is not None:
#             print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))
##=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data#  Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data   Get_Options_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tabulate import tabulate
import datetime as dt
import pandas as pd
import threading
import os
import re
def get_Historical_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date=None, End_Date=None):
    # ---------- Date Formatting ---------- expiry_date
    Expiry_Date = pandas_date_format(Expiry_Date)
    Start_Date  = pandas_date_format(Start_Date)
    End_Date    = pandas_date_format(End_Date)
    Expiry_Date, Start_Date, End_Date = get_start_end_expiry_formet(Expiry_Date, Start_Date, End_Date)
    if End_Date.time() == dt.time(0, 0, 0):
        End_Date = dt.datetime.combine(End_Date.date(), dt.time(15, 30, 0))
    # ---------- Step 1: Read from GitHub ----------
    if GitHub_API is not None:
       GitHub_Data = Read_GitHub_Options_Data(GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type)
    else:
       GitHub_Data = None

    # ---------- Step 2: Filter Valid GitHub Data ----------
    if GitHub_Data is not None and not GitHub_Data.empty:
        GitHub_Data["datetime"] = pandas_date_format(GitHub_Data["datetime"])
        GitHub_Data_Filter = GitHub_Data[(GitHub_Data["datetime"] >= Start_Date) & (GitHub_Data["datetime"] <= End_Date)]
        GitHub_Data_Date_List = sorted(GitHub_Data_Filter["datetime"].dt.date.unique())
    else:
        GitHub_Data_Filter = pd.DataFrame()
        GitHub_Data_Date_List = []

    # ---------- Step 3: Identify Missing Dates ----------
    Teding_Date_List = [d.date() for d in Get_BTST_Date(breeze, Start_Date=Start_Date, End_Date=End_Date)]
    No_Data_Date_List = [d for d in Teding_Date_List if d not in GitHub_Data_Date_List]
    No_Data_Date_List = sorted([dt.datetime.combine(d, dt.datetime.min.time()) for d in No_Data_Date_List])
    remove_date = [] # '21-03-2024','01-11-2024'
    remove_date_dt = [dt.datetime.strptime(d, "%d-%m-%Y") for d in remove_date]
    Missing_Dates = [d for d in No_Data_Date_List if d not in remove_date_dt]

    # ---------- Step 4: If GitHub data complete ----------
    if (not Missing_Dates and not GitHub_Data_Filter.empty) or breeze == None :
        GitHub_Data_Filter = GitHub_Data_Filter.sort_values(by="datetime").reset_index(drop=True)
        GitHub_Data_Filter["datetime"]    = pandas_date_format(GitHub_Data_Filter["datetime"], output_format="%d-%m-%Y %H:%M")
        if "expiry_date" in GitHub_Data_Filter.columns:
            GitHub_Data_Filter["expiry_date"] = pandas_date_format(GitHub_Data_Filter["expiry_date"], output_format="%d-%m-%Y")
        return GitHub_Data_Filter

    # ---------- Step 5: Fetch Missing Data from API ----------
    if Missing_Dates and breeze :
        # print(f"📅 Missing Dates: {[d.strftime('%d-%m-%Y') for d in Missing_Dates]}")
        API_Data = Read_Strike_Data(breeze, stock_name=stock_name, Expiry_Date=Expiry_Date, Options_Type=Options_Type, strike_price=strike_price,
                                    Start_Date=Start_Date, End_Date=End_Date, date_list=Missing_Dates)
    else:
        API_Data = pd.DataFrame()

    # ---------- Step 6: Merge GitHub + API Data ----------
    if (GitHub_Data is not None and not GitHub_Data.empty) or (API_Data is not None and not API_Data.empty) and GitHub_API is not None :
        if GitHub_Data is None or GitHub_Data.empty:
            Merged_Data = API_Data
        elif API_Data is None or API_Data.empty:
            Merged_Data = GitHub_Data
        else:
            Merged_Data = pd.concat([GitHub_Data, API_Data], ignore_index=True)

        # ---------- Clean Merge ----------
        Merged_Data["datetime"] = pd.to_datetime(Merged_Data["datetime"], dayfirst=True, errors='coerce').dt.floor("min")
        Merged_Data = ( Merged_Data.sort_values("datetime")
            .drop_duplicates(subset=["datetime", "stock_code"], keep="last")
            .reset_index(drop=True))

        # ---------- Save to Local ----------
        if (not Merged_Data.empty) and GitHub_API is not None :
            safe_stock_name  = re.sub(r'[^A-Za-z0-9_-]', '_', stock_name.lower())
            safe_Expiry_Date = pandas_date_format(Expiry_Date, output_format="%d-%m-%Y")
            if Options_Type.lower() in ["fu","ch"]:
                strike_price = 0
            os.makedirs(safe_stock_name, exist_ok=True)
            file_name = f"{safe_stock_name}/{safe_Expiry_Date}_{strike_price}_{Options_Type.lower()}.csv.gz"
            Merged_Data["datetime"]    = pandas_date_format(Merged_Data["datetime"], output_format="%d-%b-%Y %H:%M")
            if "expiry_date" in Merged_Data.columns:
                Merged_Data["expiry_date"] = pandas_date_format(Merged_Data["expiry_date"], output_format="%d-%b-%Y")
            Merged_Data.to_csv(file_name,index=False,compression='gzip',encoding='utf-8-sig', float_format="%.2f", date_format="%d-%b-%Y %H:%M" )

            # ---------- Upload to GitHub in background ----------
            # Upload_GitHub_Options_Data(GitHub_API, file_name)
            thread = threading.Thread(target=Upload_GitHub_Options_Data,args=(GitHub_API,),kwargs={'local_path': file_name},daemon=True)
            thread.start()
            GitHub_Data = Merged_Data
        else:
            GitHub_Data = pd.DataFrame()
    else:
        if breeze:
           GitHub_Data = API_Data
        else:
           GitHub_Data = pd.DataFrame()

    # ---------- Step 7: Final Filter ----------
    if GitHub_Data is not None and not GitHub_Data.empty:
        GitHub_Data["datetime"] = pandas_date_format(GitHub_Data["datetime"])
        GitHub_Data = GitHub_Data.sort_values(by="datetime").reset_index(drop=True)
        GitHub_Data = GitHub_Data[(GitHub_Data["datetime"] >= Start_Date) & (GitHub_Data["datetime"] <= End_Date)]
        GitHub_Data["datetime"]    = pandas_date_format(GitHub_Data["datetime"], output_format="%d-%m-%Y %H:%M")
        if "expiry_date" in GitHub_Data.columns:
           GitHub_Data["expiry_date"] = pandas_date_format(GitHub_Data["expiry_date"], output_format="%d-%m-%Y")
        return GitHub_Data

    return pd.DataFrame()  # fallback safe empty

# # Example usage
# stock_name_list = [ {"Nifty": 24700}, {"Nifty Bank": 55000}, {"reliance": 1380} ]
# for item in stock_name_list:
#     for stock_name, strike_price in item.items():
#         Expiry_Date  = "28-10-2025"
#         Options_Type = "put"                # 'ch', 'fu', 'call', 'put', 'op'
#         Start_Date   = "01-09-2025"
#         End_Date     = "28-10-2025"
#         Data = get_Historical_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date, End_Date)
#         if Data is not None:
#             print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))
##=========================================================================================================================================================================================================================================================================================

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import re
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  GitHub_Single_download   GitHub_Single_download   GitHub_Single_download   GitHub_Single_download   GitHub_Single_download   GitHub_Single_download#  GitHub_Single_download   GitHub_Single_download   GitHub_Single_download   GitHub_Single_download   GitHub_Single_download
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GitHub_Single_download(GitHub_API, stock_name, path):
    owner        = GitHub_API["owner"]
    repo_name    = GitHub_API["repo_name"]
    headers      = GitHub_API["headers"]
    download_url = f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/{path}"
    file_name    = os.path.basename(path)

    try:
        r = requests.get(download_url, headers=headers, timeout=20)
        if r.status_code == 200:
            with open(os.path.join(stock_name, file_name), "wb") as f:
                f.write(r.content)
            return file_name
        else:
            print(f"❌ Failed ({r.status_code}): {file_name}")
            return None
    except Exception as e:
        print(f"❌ Error downloading {file_name}: {e}")
        return None
# # Example usage
# stock_name = "nifty"
# Path = "nifty/2025/10/28-10-2025/28-10-2025_25300_call.csv.gz"
# os.makedirs(stock_name, exist_ok=True)
# File = GitHub_Single_download(GitHub_API,stock_name, Path)
# print(File)
##=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files#  GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files   GitHub_List_Files
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GitHub_List_Files(GitHub_API, stock_name=""):
    owner     = GitHub_API["owner"]
    repo_name = GitHub_API["repo_name"]
    headers   = GitHub_API["headers"]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{stock_name}"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("❌ Error listing:", stock_name)
        return []

    items = r.json()
    all_files = []

    with ThreadPoolExecutor(max_workers=max(1, len(items))) as executor: # THREADPOOL START
        futures = []
        for item in items:
            if item["type"] == "file":
                if item["path"].endswith(".csv.gz"):
                   all_files.append(item["path"])
            elif item["type"] == "dir":
                futures.append(executor.submit(GitHub_List_Files, GitHub_API, item["path"]))
        for future in as_completed(futures):# सभी threads के result merge करो
            sub_files = future.result()
            for f in sub_files:
                if f.endswith(".csv.gz"):
                    all_files.append(f)
    return all_files

# # Example usage
# stock_name = "nifty"
# all_files = list_files(GitHub_API, stock_name)
# print("Total CSV.GZ Files Found:", len(all_files))
##=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download#  GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download   GitHub_Multi_download
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def GitHub_Multi_download(GitHub_API, stock_name):
    safe_stock = re.sub(r'[^A-Za-z0-9_-]', '_', stock_name.lower())
    path = f"/content/{safe_stock}"
    os.makedirs(path, exist_ok=True)
    Downloaded_count = sum(1 for f in os.listdir(path) if f.lower().endswith(".csv.gz"))
    raw_urls = GitHub_List_Files(GitHub_API, safe_stock)
    GitHub_count = len(raw_urls)
    if GitHub_count <= Downloaded_count:
       return []
    downloaded = []
    with ThreadPoolExecutor(max_workers=max(1, len(raw_urls))) as executor:
        futures = [executor.submit(GitHub_Single_download, GitHub_API, safe_stock, path) for path in raw_urls]
        for f in as_completed(futures):
            result = f.result()
            if result:
                downloaded.append(result)
    return downloaded

# # Example usage
# stock_name = "nifty" #"nifty", "nifty bank" "reliance"
# downloaded = GitHub_Multi_download(GitHub_API, stock_name)
# print("Downloaded Files:", len(downloaded))
##=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data#  get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data   get_Downloaded_Data
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import datetime as dt
import time
Downloaded_Data_Liat = []
def get_Downloaded_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date=60, End_Date=0, GitHub_Update=True):
    safe_stock = re.sub(r'[^A-Za-z0-9_-]', '_', stock_name.lower())
    path = f"/content/{safe_stock}/{Expiry_Date}_{strike_price}_{Options_Type}.csv.gz"
    
    Expiry_Date, Start_Date, End_Date = get_start_end_expiry_formet(Expiry_Date, Start_Date, End_Date)
    Start_Date = pd.to_datetime(Start_Date, dayfirst=True)
    End_Date   = pd.to_datetime(End_Date,   dayfirst=True)
    if End_Date.time() == dt.time(0, 0, 0):
      End_Date = dt.datetime.combine(End_Date.date(), dt.time(15, 30, 0))

    try:
      Data = pd.read_csv(path,compression="gzip",low_memory=False,)
    except:
      Data = get_Historical_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date, End_Date)
      if stock_name not in Downloaded_Data_Liat:
         downloaded = GitHub_Multi_download(GitHub_API, stock_name)
    if Data is None or Data.empty:
       return Data

    Data['datetime'] = pandas_date_format(Data['datetime'])
    none_count = Data['datetime'].isna().sum()
    if none_count > 0:
       print("❌ Total datetime None (NaT) values:", none_count)
    if Start_Date and End_Date:
      mask = (Data['datetime'] >= Start_Date) & (Data['datetime'] <= End_Date)
      Data = Data.loc[mask]
    if Data.empty:
        return Data
    
    if GitHub_Update :
        Downloaded_Data_Date_List = sorted(Data["datetime"].dt.date.unique())
        Teding_Date_List = [d.date() for d in Get_BTST_Date(breeze, Start_Date=Start_Date, End_Date=End_Date)]
        No_Data_Date_List = [d for d in Teding_Date_List if d not in Downloaded_Data_Date_List]
        No_Data_Date_List = sorted([dt.datetime.combine(d, dt.datetime.min.time()) for d in No_Data_Date_List])
        remove_date = []
        remove_date_dt = [dt.datetime.strptime(d, "%d-%m-%Y") for d in remove_date]
        Missing_Dates = [d for d in No_Data_Date_List if d not in remove_date_dt]
        if Missing_Dates and breeze and GitHub_API :
            Data = get_Historical_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date, End_Date)
            Data['datetime'] = pandas_date_format(Data['datetime'])
            none_count = Data['datetime'].isna().sum()
            if none_count > 0:
              print("❌ Total datetime None (NaT) values:", none_count)
            if Start_Date and End_Date:
              mask = (Data['datetime'] >= Start_Date) & (Data['datetime'] <= End_Date)
              Data = Data.loc[mask]
            if Data.empty:
                return Data

    if not Data['datetime'].is_monotonic_increasing:
        Data = Data.sort_values('datetime', kind='mergesort')
    Data.reset_index(drop=True, inplace=True)
    Data['datetime'] = Data['datetime'].dt.strftime("%d-%m-%Y %H:%M")
    if "expiry_date" in Data.columns:
        Data['expiry_date'] = pd.to_datetime(Data['expiry_date'], dayfirst=True, errors="coerce").dt.strftime("%d-%m-%Y")
    return Data

# Example usage
# Expiry_Date = "28-10-2025"
# stock_name_list = [{"Nifty": 26000},{"Nifty Bank": 58000},{"reliance": 1500},]
# Options_List = ["ch", "fu", "call", "put"]
# for item in stock_name_list:
#     stock_name = list(item.keys())[0]
#     base_strike_price = list(item.values())[0]
#     for Options_Type in Options_List:
#         if Options_Type in ["ch", "fu"]:
#             strike_price = 0
#         else:
#             strike_price = base_strike_price
#         Data = get_Downloaded_Data(breeze, GitHub_API, stock_name, Expiry_Date, strike_price, Options_Type, Start_Date=30, End_Date=0)
#         if Data is not None and not Data.empty:
#             print(f"\nStock: {stock_name} | Type: {Options_Type} | Strike: {strike_price}")
#             print(tabulate(pd.concat([Data.head(3), Data.tail(3)]),headers="keys",tablefmt="psql"))
#         else:
#             print(f"\n⚠️ No data found → {stock_name} | {Options_Type} | strike {strike_price}")
##=========================================================================================================================================================================================================================================================================================




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data   get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Cash_Futures_Data(breeze, GitHub_API, stock_name, Options_Type, Start_Date, End_Date):
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

    strike_price = 0
    all_data = []
    def fetch_data(start, end, expiry):
        return get_Downloaded_Data(breeze, GitHub_API, stock_name, expiry, strike_price, Options_Type, Start_Date=start, End_Date=end)
    with ThreadPoolExecutor(max_workers=10) as executor: # with ThreadPoolExecutor(max_workers=max(1, min(200, len(date_ranges)))) as executor:
        futures = [executor.submit(fetch_data, start, end, expiry) for (start, end, expiry) in date_ranges]
        for f in as_completed(futures):
            try:
                all_data.append(f.result())
            except Exception as e:
                print("⚠️ get_Cash_Futures_Data Error:", e)

    if not all_data:
        return pd.DataFrame()
    if Options_Type == "ch":
       duplicates_columns = ["datetime"]
    else:
       duplicates_columns = ["datetime", "expiry_date"]
    Futures_Data             = pd.concat(all_data, ignore_index=True)
    Futures_Data             = Futures_Data.drop_duplicates(subset=duplicates_columns, keep="last")
    Futures_Data['datetime'] = pd.to_datetime(Futures_Data['datetime'], dayfirst=True)
    Futures_Data             = Futures_Data.sort_values(by="datetime").reset_index(drop=True)
    Futures_Data["datetime"] = Futures_Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    return Futures_Data

# Example usage
# for stock_name in ["nifty", "nifty bank", "reliance"]:
#     for Options_Type in ["ch", "fu"]:
#         Start_Date = "01-10-2021"
#         End_Date   = "28-10-2022"
#         Fu_data = get_Cash_Futures_Data(breeze, GitHub_API, stock_name, Options_Type, Start_Date, End_Date) # breeze
#         print(tabulate(pd.concat([Fu_data.head(1), Fu_data.tail(1)]), headers="keys", tablefmt="psql"))
# =========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data   Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Ch_Fu_merge_data(Ch_data, Fu_data):
    Ch_data["datetime"] = pd.to_datetime(Ch_data["datetime"], format="%d-%m-%Y %H:%M") # 🔹 Step 1: datetime को proper format में convert करो
    Fu_data["datetime"] = pd.to_datetime(Fu_data["datetime"], format="%d-%m-%Y %H:%M")
    if "stock_code" not in Fu_data.columns: # 🔹 Step 2: stock_code columns ensure करो
        Fu_data["stock_code"] = Ch_data["stock_code"].iloc[0]
    if "stock_code" not in Ch_data.columns:
        Ch_data["stock_code"] = Fu_data["stock_code"].iloc[0]
    merged = pd.merge_asof(Ch_data.sort_values("datetime"),Fu_data.sort_values("datetime"),on="datetime", # 🔹 Step 3: पहले normal nearest merge करो
                           by="stock_code",direction="nearest",tolerance=pd.Timedelta("3min")) # nearest 3 min तक match allow
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
def get_Index_Data(breeze, GitHub_API, stock_name, Start_Date, End_Date,):
    def get_Round_ATM(stock_name, Price):
        Strike_Gep = get_Strike_Gep(stock_name)
        return (Price / Strike_Gep).round() * Strike_Gep
    def get_ATM_Strike(merged_data, stock_name):
        Strike_Gep = get_Strike_Gep(stock_name)
        merged_data["ch_atm"] = (merged_data["ch_close"] / Strike_Gep).round() * Strike_Gep
        merged_data["fu_atm"] = (merged_data["fu_close"] / Strike_Gep).round() * Strike_Gep
        return merged_data

    Ch_data = get_Cash_Futures_Data(breeze, GitHub_API, stock_name, Options_Type = "ch", Start_Date=Start_Date, End_Date=End_Date,)
    # print(tabulate(pd.concat([Ch_data.head(3), Ch_data.tail(3)]), headers="keys", tablefmt="psql"))
    Fu_data = get_Cash_Futures_Data(breeze, GitHub_API, stock_name, Options_Type = "fu", Start_Date=Start_Date, End_Date=End_Date,)
    # print(tabulate(pd.concat([Fu_data.head(3), Fu_data.tail(3)]), headers="keys", tablefmt="psql"))

    merged_data = Ch_Fu_merge_data(Ch_data, Fu_data)
    Data_Expiry = get_Expiry(merged_data, stock_name)
    Index_Data  = get_ATM_Strike(Data_Expiry, stock_name)
    # print(tabulate(pd.concat([Index_Data.head(3), Index_Data.tail(3)]), headers="keys", tablefmt="psql"))

    if "curr_w_expiry" in Index_Data.columns:
       Index_Data["curr_w_expiry"] = pandas_date_format(Index_Data["curr_w_expiry"], output_format = "%d-%m-%Y")
    if "next_w_expiry" in Index_Data.columns:
       Index_Data["next_w_expiry"] = pandas_date_format(Index_Data["next_w_expiry"], output_format = "%d-%m-%Y")
    if "curr_m_expiry" in Index_Data.columns:
       Index_Data["curr_m_expiry"] = pandas_date_format(Index_Data["curr_m_expiry"], output_format = "%d-%m-%Y")
    if "datetime" in Index_Data.columns:
        Index_Data["datetime"] = pandas_date_format(Index_Data["datetime"])
        Index_Data = Index_Data.sort_values(by="datetime").reset_index(drop=True)
        Index_Data["datetime"] = pandas_date_format(Index_Data["datetime"], output_format = "%d-%m-%Y %H:%M")
        Index_Data = Index_Data[Index_Data['datetime'].notnull() & (Index_Data['datetime'] != "None") & (Index_Data['datetime'] != "")]
        Index_Data = Index_Data.reset_index(drop=True)
    return Index_Data

# # Example usage
# stock_name = "nifty"            #"nifty", "nifty bank" "reliance"
# Start_Date = "01-10-2021"
# End_Date   = "28-10-2022"
# Data = get_Index_Data(breeze, GitHub_API, stock_name, Start_Date, End_Date,)
# print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update#  get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update   get_GitHub_Data_Update
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed
from IPython.display import clear_output
from tqdm import tqdm
def get_strike_list(breeze, GitHub_API, stock_name, Expiry_Date, OTM, ITM, Strike_Gep):
    try:
      Data = get_Historical_Data(breeze, GitHub_API, stock_name=stock_name, Expiry_Date=Expiry_Date, strike_price=0, Options_Type="fu", Start_Date=60, End_Date=0)
      Data = get_Historical_Data(breeze, GitHub_API, stock_name=stock_name, Expiry_Date=Expiry_Date, strike_price=0, Options_Type="ch", Start_Date=60, End_Date=0)
      Max_High = round((Data["ch_high"].max() / Strike_Gep), 0) * Strike_Gep
      Min_Low  = round((Data["ch_low"].min() / Strike_Gep), 0) * Strike_Gep
      call_Max_High = Max_High + (Strike_Gep * OTM)
      call_Min_Low  = Min_Low  - (Strike_Gep * ITM)
      put_Max_High  = Max_High + (Strike_Gep * ITM)
      put_Min_Low   = Min_Low  - (Strike_Gep * OTM)
      call_strike_list = list(range(int(call_Min_Low), int(call_Max_High + Strike_Gep), int(Strike_Gep)))
      put_strike_list  = list(range(int(put_Min_Low),  int(put_Max_High + Strike_Gep), int(Strike_Gep)))
      return {"call": call_strike_list, "put": put_strike_list}
    except Exception as e:
        print(f"Error ({stock_name}, {Expiry_Date}): {e}")
        return None
def get_Expirys_strike_List(breeze, GitHub_API, stock_name, Expirys_List, OTM, ITM, Strike_Gep):
    Expirys_strike_List = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(get_strike_list, breeze, GitHub_API, stock_name, Expiry_Date, OTM, ITM, Strike_Gep): Expiry_Date for Expiry_Date in Expirys_List}
        for future in as_completed(futures):
            expiry = futures[future]
            result = future.result()   # only once
            if result is not None:
                Expirys_strike_List[expiry] = result
    return Expirys_strike_List

def get_GitHub_Data_Update(breeze, GitHub_API, stock_name, Expiry_Period, Expiry_Type, Start_Date, End_Date, OTM=30, ITM=15, Show_Print=False):
    Strike_Gep          = get_Strike_Gep(stock_name)
    Expirys_List        = get_Symbol_Expiry(Dates=None, Symbol=stock_name, Expiry_Period=Expiry_Period, Expiry_Type=Expiry_Type, Start_Date=Start_Date, End_Date=End_Date)
    Expirys_strike_List = get_Expirys_strike_List(breeze, GitHub_API, stock_name, Expirys_List, OTM, ITM, Strike_Gep)

    for Expiry_Date in tqdm(Expirys_List, desc="Processing Expiries"):
        if Expiry_Date not in Expirys_strike_List:
            print(f"No strike list for expiry {Expiry_Date}, skipping.")
            continue
        for Options_Type, strike_list in Expirys_strike_List[Expiry_Date].items():
            if not strike_list:
                print(f"No strikes for {Options_Type} on {Expiry_Date}, skipping.")
                continue

            with ThreadPoolExecutor(max_workers=max(len(strike_list), 1)) as executor:
                futures = {executor.submit(get_Historical_Data,breeze,GitHub_API,stock_name,Expiry_Date,strike_price,Options_Type, Start_Date=60, End_Date=0):  # get_Historical_Data  get_Downloaded_Data
                                          strike_price for strike_price in strike_list}

                for future in as_completed(futures):
                    strike = futures[future]   # THIS is the strike_price for this future
                    try:
                        Data = future.result()
                    except Exception as e:
                        print(f"Exception fetching ({Options_Type}, {strike}, {Expiry_Date}): {e}")
                        continue
                    clear_output(wait=True)
                    if Show_Print :
                        if Data is not None and len(Data) > 0:
                            print("\n", Options_Type.upper(), strike, Expiry_Date, "ok")
                            try:
                                print(tabulate(pd.concat([Data.head(1), Data.tail(1)]), headers="keys", tablefmt="psql"))
                            except Exception as e:
                                print(f"Error printing data for ({Options_Type}, {strike}, {Expiry_Date}): {e}")
                        else:
                            print(f"Error (no data) ({Options_Type}, {strike}, {Expiry_Date})")
    print("\n\nAll Data Download Completed ✔")


# # Example usage
# stock_name     = "reliance"         #"nifty", "nifty bank" "reliance"
# Expiry_Period  = "Monthly"       # "Weekiy" , "Monthly"
# Expiry_Type    = "Current"       # "Current", "Next"
# Start_Date     = "01-01-2025"
# End_Date       = "31-12-2025"
# OTM         = 30
# ITM         = 15
# get_GitHub_Data_Update(breeze, GitHub_API, stock_name, Expiry_Period, Expiry_Type, Start_Date, End_Date, OTM, ITM)
#=========================================================================================================================================================================================================================================================================================






