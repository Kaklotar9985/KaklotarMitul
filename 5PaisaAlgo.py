# Telegram Message  # Telegram Message  # Telegram Message  # Telegram Message  # Telegram Message  # Telegram Message  # Telegram Message  # Telegram Message
# !pip install telebot
import telebot
def Telegram_Message(*args):
    BOT_TOKEN = '7591009372:AAEkZFnOZ1UyqxQgiTSJVqKqr1uvPP5KqPI'
    Tel_Candal_Data_ID  = "-1002257377003"
    Tel_JB_Sons_ID      = "-1002263632329"
    Tel_Jay_Mataji_ID   = '1170793375'
    CHAT_ID = Tel_Jay_Mataji_ID
    try:
      bot = telebot.TeleBot(BOT_TOKEN)
      message = "\n".join(filter(None, args))
      bot.send_message(CHAT_ID, message)
      print("Message sent successfully!")
    except Exception as e:
        print( f"Telegram_Message function Error :", e )
# Example usage
# Telegram_Message("HI")
#_____________________________________________________________________________________________________________________________________________________

# login_to_5paisa  login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   
#!pip install py5paisa
#!pip install pyotp
from py5paisa.order import OrderType, Exchange
from py5paisa import FivePaisaClient
import pyotp

def login_to_5paisa(cred):
    try:
        totp = pyotp.TOTP(cred["token"]).now()
        client = FivePaisaClient(cred=cred)
        client.get_totp_session(cred["ClientCode"], totp, cred["pin"])
        access_token = client.get_access_token()
        client.set_access_token(access_token, cred["ClientCode"])
        if access_token :
           print("✅ Login Successful to 5Paisa:", cred["ClientCode"])
        else:
           print("❌ Login Failed to 5Paisa for Client:", cred["ClientCode"])
        return client
    except Exception as e:
        print("❌ 5paisa Login Failed:", str(e))
        return None
#____________________________________________________________________________________________________________________________________________________________________________________

#  login_to_Anjal   login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal   
# !pip install smartapi-python
# !pip install logzero
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from SmartApi import SmartConnect
import pyotp

def login_to_Anjal(LoginData):
    global smartApi , data , AUTH_TOKEN , refreshToken , FEED_TOKEN , res , sms
    try:
        smartApi = SmartConnect(api_key=LoginData["API_KEY"])
        session_data = smartApi.generateSession(LoginData["USERNAME"], LoginData["PWD"], pyotp.TOTP(LoginData["TOKEN"]).now())
        AUTH_TOKEN = session_data['data']['jwtToken']
        refreshToken = session_data['data']['refreshToken']
        FEED_TOKEN = smartApi.getfeedToken()
        profile = smartApi.getProfile(refreshToken)
        sws = SmartWebSocketV2(AUTH_TOKEN, LoginData["API_KEY"], LoginData["USERNAME"], FEED_TOKEN)
        print("✅ Login Successful to Anjal :", profile['data']['name'])
        return smartApi, AUTH_TOKEN, refreshToken, FEED_TOKEN, sws
        # return { 'smartApi': smartApi, 'auth_token': AUTH_TOKEN, 'refresh_token': refreshToken, 'feed_token': FEED_TOKEN, 'websocket': sws }
    except Exception as e:
        print("❌ Anjal Login Failed:", str(e))
#______________________________________________________________________________________________________________________________________________

#  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login  #  kotak Login
from neo_api_client import NeoAPI
def login_to_kotak(LoginData):
    try:
        client = NeoAPI(consumer_key=LoginData["consumer_key"], consumer_secret= LoginData["consumer_secret"], environment="prod")
        client.login(mobilenumber=LoginData["mobilenumber"], password=LoginData["password"])
        client.session_2fa(OTP=LoginData["MPIN"])
        print("Kotak Login successfully")
        return client
    except Exception as e:
        print(f"login_to_kotak function Error: {str(e)}")
        return None
# client = login_to_kotak(Kotak_LoginData_Mitul)
#______________________________________________________________________________________________________________________________________________________

# fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time

from datetime import datetime, timedelta, time
import pytz

IST = pytz.timezone('Asia/Kolkata')
FORMATS = {"live_time": "%H:%M:%S", "live_date": "%d-%m-%Y","live_datetime": "%Y-%m-%d %H:%M:%S"}
def get_live_datetime(Times = None):
    try:
       current = datetime.now(IST)
       return current.strftime(FORMATS[Times.lower()]) if Times else current
    except KeyError:
        return datetime.now(IST).strftime(FORMATS["live_datetime"])
    except Exception as e:
        print(f"get_live_time function Error : {e}")
        return None

# Example usage
# print(get_live_datetime())  #  # live_time, live_date, live_datetime

def get_last_trading_date(fmt = None):
    try:
        current_dt = get_live_datetime()
        if current_dt.weekday() == 5:  # शनिवार
            adjusted = current_dt - timedelta(days=1)
        elif current_dt.weekday() == 6:  # रविवार
            adjusted = current_dt - timedelta(days=2)
        else:
            if current_dt.time() < time(9,15,1):
                adjusted = current_dt - timedelta(days=1)
                if adjusted.weekday() == 5:  # नया दिन शनिवार
                    adjusted -= timedelta(days=1)
                elif adjusted.weekday() == 6:  # नया दिन रविवार
                    adjusted -= timedelta(days=2)
            else:
                adjusted = current_dt
        return adjusted.strftime(fmt) if fmt else adjusted
    except Exception as e:
        print(f"get_last_trading_day function Error : {e}")
        return None

# Example usage
# print(get_last_trading_date())

def get_candle_times(time_frame=5, Candle_no=-1, format = None):
    try:
      current = get_live_datetime()
      last_day = get_last_trading_date()
      market_start = last_day.replace(hour=9, minute=15, second=0, microsecond=0)
      market_end = market_start.replace(hour=15, minute=30)
      if Candle_no < 0:  # सभी negative candle numbers को हैंडल करें
          steps_back = abs(Candle_no)
          if market_start <= current <= market_end:
              total_min = (current.hour * 60 + current.minute) - 555
              prev_candle_min = (total_min // time_frame) * time_frame
              base_candle = market_start + timedelta(minutes=prev_candle_min)
          else:
              base_candle = market_end - timedelta(minutes=time_frame)
          desired_candle = base_candle - timedelta(minutes=(steps_back-1)*time_frame)
          if desired_candle < market_start:
              desired_candle = market_start
          return desired_candle.strftime(format) if format else desired_candle
      else:
          delta = market_end - market_start
          total_trading_minutes = delta.total_seconds() // 60
          max_candles = ((total_trading_minutes - time_frame) // time_frame) + 1
          Candle_no = max(1, min(Candle_no, max_candles))
          start_time = market_start + timedelta(minutes=(Candle_no-1)*time_frame)
          return start_time.strftime(format) if format else start_time
    except Exception as e:
        print(f"get_candle_times function Error : {e}")
        return None

# Example usage
# time_Frem = 5
# Candle_no = -1
# format = "%H:%M"
# previous = get_candle_times(time_Frem, Candle_no, format)
# print(f"कैंडल: {previous}")
#___________________________________________________________________________________________________________________________________________________________________________

# fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data
from datetime import datetime, timedelta
import pandas as pd
import requests
def fetch_All_Scrip_Data():
    global All_Scrip_Data
    try:
        url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
        All_Scrip_Data = pd.DataFrame(requests.get(url).json())
        return All_Scrip_Data
    except Exception as e:
        print(f"fetch_Scrip_Data Function Error: {e}")
        return None
# All_Scrip_Data = fetch_Scrip_Data()
#___________________________________________________________________________________________________________________________________________________________________________

# fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data
def fetch_Scrip_Data(All_Scrip_Data):
    try :
        Scrip_Data_Exchange_filter = All_Scrip_Data[All_Scrip_Data['exch_seg'] == "NFO"]
        Scrip_Data_Name_filter = Scrip_Data_Exchange_filter[Scrip_Data_Exchange_filter['name'] == "NIFTY"]
        Scrip_Data_instrumenttype_filter = Scrip_Data_Name_filter[Scrip_Data_Name_filter['instrumenttype'] == "OPTIDX" ]
        Scrip_Data = Scrip_Data_instrumenttype_filter
        return Scrip_Data
    except Exception as e:
        print("fetch_Scrip_Data function Error : ", e )
# Example usage
# Scrip_Data = fetch_Scrip_Data(All_Scrip_Data)
#________________________________________________________________________________________________________________________________________________________________________

# fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate
def fetch_ExpiryDate(Scrip_Data):
    try :
        today = datetime.now().strftime('%d%b%Y')
        Expiry_Data = sorted(Scrip_Data['expiry'].unique(), key=lambda x: datetime.strptime(x, '%d%b%Y'))
        Expiry_List = [expiry for expiry in Expiry_Data if datetime.strptime(expiry, "%d%b%Y") >= datetime.strptime(today, "%d%b%Y")]
        Curnent_Expiry = datetime.strptime(Expiry_List[0], '%d%b%Y').strftime('%d%b%y').upper()
        Next_Expiry = datetime.strptime(Expiry_List[1], '%d%b%Y').strftime('%d%b%y').upper()
        return Curnent_Expiry , Next_Expiry ,Expiry_List
    except Exception as e:   # त्रुटि संदेश और री-ट्राई लॉजिक
        print( f"fetch_ExpiryDate function Error : ", e )
# Example usage
# Curnent_Expiry, Next_Expiry, Expiry_List  = fetch_ExpiryDate (Scrip_Data)
#_________________________________________________________________________________________________________________________________________________________________

# Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken
def Symbol_SymbolToken(Scrip_Data, Strike ,Option_Type, Expiry, Index = "NIFTY"):
    try:
        Token = f"{Index}{Expiry}{Strike}{Option_Type}"
        SymbolToken = Scrip_Data[Scrip_Data['symbol'].str.contains(Token, case=False, na=False)]['token'].iloc[0]
        Symbol = Scrip_Data[Scrip_Data['symbol'].str.contains(Token, case=False, na=False)]['symbol'].iloc[0]
        return Symbol , SymbolToken
    except Exception as e:
        print( f"Symbol_SymbolToken function Error : ", e )
# Example usage
# Symbol,SymbolToken = Symbol_SymbolToken( Scrip_Data, "24200", "CE", Expiry = Next_Expiry)
# print(f"Symbol      : {Symbol}")
# print(f"SymbolToken : {SymbolToken}")
#______________________________________________________________________________________________________________________________________________________________________________

# fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
def fetch_Candle_Data_Fast(symboltoken, Symbol, StrikePrice, OP_tipe, last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi):
    try:
        if "09:20:00" <= get_live_datetime("live_time") <= "23:59:00":
            historicParam = { "exchange": "NFO", "symboltoken": symboltoken, "interval": "FIVE_MINUTE", "fromdate": f"{last_trading_date} 09:00",  "todate": f"{last_trading_date} 15:30" }
            response = smartApi.getCandleData(historicParam)
            if not response.get("data"):
                return None
            columns = ['time', 'open', 'high', 'low', 'close', 'volume']
            df = pd.DataFrame(response['data'], columns=columns)
            df['time'] = pd.to_datetime(df['time'])
            df['time_str'] = df['time'].dt.strftime('%H:%M')
            Close_915 = df.loc[df['time_str'] == First_Candle_Time, 'close'].iloc[0] if not df[df['time_str'] == First_Candle_Time].empty else None
            Close_PC = df.loc[df['time_str'] == Previous_Candle_Time, 'close'].iloc[0] if not df[df['time_str'] == Previous_Candle_Time].empty else None
            Tred = "Yes" if (Close_915 and Close_PC and Close_915 > Close_PC) else None
            return { "Symbol": Symbol, "Symboltoken": symboltoken, "StrikePrice": StrikePrice, "OP_tipe": OP_tipe, "Close_915": Close_915, "Close_PC": Close_PC, "Tred": Tred }
    except Exception as e:
        print(f"fetch_Candle_Data_Fast function Error: {e}")
        return None

def fetch_Candle_Data(smartApi, Scrip_Data, strike, Next_Expiry, last_trading_date, First_Candle_Time):
    try:
        symbol_to_token = Scrip_Data.set_index('symbol')['token'].to_dict()
        CEstrike = strike
        PEstrike = str(int(strike) + 50)
        CEToken = f"NIFTY{Next_Expiry}{CEstrike}CE"
        PEToken = f"NIFTY{Next_Expiry}{PEstrike}PE"
        CE_SymbolToken = symbol_to_token.get(CEToken)
        PE_SymbolToken = symbol_to_token.get(PEToken)
        if not CE_SymbolToken or not PE_SymbolToken:
            raise ValueError("Symbol token not found for CE or PE")
        Previous_Candle_Time = get_candle_times(time_frame=5, Candle_no=-2, format="%H:%M")
        with ThreadPoolExecutor(max_workers=2) as executor:
            ce_future = executor.submit( fetch_Candle_Data_Fast, CE_SymbolToken, CEToken, CEstrike, "CE",last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi )
            pe_future = executor.submit( fetch_Candle_Data_Fast, PE_SymbolToken, PEToken, PEstrike, "PE", last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi)
            CE_Candle_Data = ce_future.result()
            PE_Candle_Data = pe_future.result()
        return {"CE": CE_Candle_Data, "PE": PE_Candle_Data}
    except Exception as e:
        print(f"fetch_Candle_Data function Error: {e}")
        return None

# strike = 24250
# All_Scrip_Data = fetch_All_Scrip_Data()
# Scrip_Data = fetch_Scrip_Data(All_Scrip_Data)
# Curnent_Expiry, Next_Expiry, Expiry_List = fetch_ExpiryDate (Scrip_Data)
# last_trading_date    = get_last_trading_date(fmt="%Y-%m-%d")
# First_Candle_Time    = get_candle_times(time_frame=5, Candle_no=1, format="%H:%M")

# Candal_Data = fetch_Candle_Data(smartApi, Scrip_Data, strike, Next_Expiry, last_trading_date, First_Candle_Time)
# print(tabulate(pd.DataFrame(Candal_Data), headers='keys', tablefmt='pretty', showindex=True))
#______________________________________________________________________________________________________________________________________________________________________________

# get_Variable_DataNone get_Variable_DataNone get_Variable_DataNone get_Variable_DataNone get_Variable_DataNone get_Variable_DataNone 
def get_Variable_DataNone(Variable_Name):
    try:
        if Variable_Name == "CE_Detail":
          return    {"CE_Tred"  : None,
                      "CE_Detail":{"CE_SELL_orderid": None, "CE_Entry_Time"  : None, "CE_SL_orderid"  : None, "CE_SL_orderDate": None, "CE_Symbol"      : None,
                                    "CE_Symboltoken" : None, "CE_StrikePrice" : None, "CE_Close_915"   : None, "CE_Close_PC"    : None, "CE_Sell_Qty"    : None,
                                    "CE_Sell_Price"  : None, "CE_Top_Loss"    : None, "CE_TSL_1"       : None, "CE_TSL_2"       : None, "CE_Target"      : None,
                                    "CE_Exit_Price"  : None, "CE_Exit_Time"   : None, "CE_Exit_Type"   : None, "CE_Exit_Trigger": None, "CE_LTP"         : None }}
        if Variable_Name == "PE_Detail":
          return    {"PE_Tred"  : None,
                      "PE_Detail":{"PE_SELL_orderid": None, "PE_Entry_Time"  : None, "PE_SL_orderid"  : None, "PE_SL_orderDate": None,  "PE_Symbol"      : None,
                                    "PE_Symboltoken" : None, "PE_StrikePrice" : None, "PE_Close_915"   : None, "PE_Close_PC"    : None,  "PE_Sell_Qty"    : None,
                                    "PE_Sell_Price"  : None, "PE_Top_Loss"    : None, "PE_TSL_1"       : None, "PE_TSL_2"       : None,  "PE_Target"      : None,
                                    "PE_Exit_Price"  : None, "PE_Exit_Time"   : None, "PE_Exit_Type"   : None, "PE_Exit_Trigger": None,  "PE_LTP"         : None }}
        if Variable_Name == "Tred_Detail":
          return    { "CALL_List": [], "PUT_List": [] }
    except Exception as e:
        print(f"get_Variable_DataNone function Error: {e}")
# ________________________________________________________________________________________________________________________________________________________________________________

# Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable  # Read_Variable
def Read_Variable(target_dict, key1, key2=None):
    try:
        if key2 is None:
            return target_dict.get(key1)
        return target_dict.get(key1, {}).get(key2)
    except Exception as e:
        print(f"Read_Variable function Error:", e)
# Example usage
# json_path = CE_Detail
# Variable_Name = "PE_Detail"
# Variable_Name2 = "PE_SELL_orderid"
# result = Read_Variable(json_path, Variable_Name, Variable_Name2)
# print(result)
#_________________________________________________________________________________________________________________________________________________________________________

# update_variable  update_variable  update_variable  update_variable  update_variable  update_variable  update_variable  update_variable  update_variable  update_variable
def update_variable(target_dict, value, key1, key2=None):
    try:
        if key2 is None:
            target_dict[key1] = value
        else:
            nested = target_dict.get(key1)
            if nested is not None:
               nested[key2] = value
    except Exception as e:
        print(f"update_variable function Error: {e}")
# Example usage
# update_variable(PE_Detail, 100, "PE_Detail","PE_LTP")
# print(CE_Detail)
# print(PE_Detail)
#_________________________________________________________________________________________________________________________________________________________________________

# Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update # Tred_Detail_Update
def Tred_Detail_Update(target_dict, new_data, list_name):
    try:
        target_dict.setdefault(list_name, []).append(new_data)
    except Exception as e:
        print(f"Tred_Detail_Update function Error: {e}")

# # उदाहरण के लिए
# target_dict = Read_Variable(PE_Detail,"PE_Detail",None)
# Tred_Detail_Update(Tred_Detail,target_dict, "PUT_List")
# print(Tred_Detail)
# ________________________________________________________________________________________________________________________________________________________________________________




