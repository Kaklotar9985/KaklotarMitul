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
'''
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
'''
#  login_to_Anjal   login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal    login_to_Anjal   
# !pip install smartapi-python
# !pip install logzero
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from SmartApi import SmartConnect
import pyotp

def login_to_Anjal(LoginData):
    global  smartApi, AUTH_TOKEN, refreshToken, FEED_TOKEN, sws
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
def fetch_Candle_Data_Fast(symboltoken, Symbol, StrikePrice, OP_tipe, time_frame, last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi):
    try:
        if "09:20:00" <= get_live_datetime("live_time") <= "23:59:00":
            time_frame_list = { 5 : "FIVE_MINUTE", 15 : "FIFTEEN_MINUTE",}
            interval = time_frame_list.get(time_frame)
            historicParam = { "exchange": "NFO", "symboltoken": symboltoken, "interval": interval, "fromdate": f"{last_trading_date} 09:00",  "todate": f"{last_trading_date} 15:30" }
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

def fetch_Candle_Data(smartApi, Scrip_Data, strike, Next_Expiry, time_frame, last_trading_date, First_Candle_Time):
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
        Previous_Candle_Time = get_candle_times(time_frame = time_frame, Candle_no=-2, format="%H:%M")
        with ThreadPoolExecutor(max_workers=2) as executor:
            ce_future = executor.submit( fetch_Candle_Data_Fast, CE_SymbolToken, CEToken, CEstrike, "CE", time_frame, last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi )
            pe_future = executor.submit( fetch_Candle_Data_Fast, PE_SymbolToken, PEToken, PEstrike, "PE", time_frame, last_trading_date, First_Candle_Time, Previous_Candle_Time, smartApi)
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
# time_frame = 15
# Candal_Data = fetch_Candle_Data(smartApi, Scrip_Data, strike, Next_Expiry, time_frame, last_trading_date, First_Candle_Time)
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

# fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol  fetch_Kotak_Symbol
from datetime import datetime, timedelta
import pandas as pd
def fetch_Kotak_scrip_data(client):
    try:
        url = client.scrip_master(exchange_segment="NFO")
        usecols = ['pSymbolName', 'pInstType', 'pExchSeg', 'pSymbol', 'pTrdSymbol', 'pOptionType', 'pExpiryDate', 'dStrikePrice;']
        scrip_data = pd.read_csv(url, usecols=usecols)
        scrip_data = scrip_data.query("(pSymbolName == 'NIFTY') and (pInstType == 'OPTIDX') and (pExchSeg == 'nse_fo')").copy()
        scrip_data['pExpiryDate'] = pd.to_datetime(scrip_data['pExpiryDate'], unit='s', errors='coerce')
        scrip_data['pExpiryDate'] = scrip_data['pExpiryDate'] + pd.DateOffset(years=10) - timedelta(days=1)
        scrip_data['ExpiryDates'] = scrip_data['pExpiryDate'].dt.strftime('%d%b%y')
        scrip_data['StrikePrice'] = (scrip_data['dStrikePrice;'] / 100).astype('int32')
        scrip_data.rename(columns={ 'pSymbol': 'Tokens', 'pTrdSymbol': 'Symbol', 'pOptionType': 'OptionType' }, inplace=True)
        return scrip_data  # <-- return DataFrame here
    except Exception as e:
        print("fetch_scrip_data function Error:", e)
        return pd.DataFrame()

def fetch_Kotak_Symbol(Tokens, Kotak_scrip_data):
    try:
        Tokens_Symbol = Kotak_scrip_data[Kotak_scrip_data['Tokens'].astype(str) == str(Tokens)]
        Symbol = Tokens_Symbol["Symbol"].iloc[0]
        return Symbol
    except Exception as e: 
        print("fetch_Tokens_Symbol function Error:", e)
        return None

# Kotak_Scrip_Data = fetch_Kotak_scrip_data(kotak_client)
# Kotak_Symbol = fetch_Kotak_Symbol("38604", Kotak_Scrip_Data)
# print(Kotak_Symbol)
#______________________________________________________________________________________________________________________________________________________

# place_order  place_order  place_order  place_order  place_order  place_order  place_order  place_order  place_order  place_order  place_order
def place_order(trading_symbol, quantity, trigger_price, transaction_type, order_type, client):
    try:
        trigger_price = float(trigger_price)         # Ensure trigger_price is treated as a float
        if order_type == "SL":  # Stop Loss order
            if transaction_type == "S":
                price = trigger_price - 0.50
            elif transaction_type == "B":
                price = trigger_price + 0.50
        elif order_type == "MKT":  # Market order
            price = 0
            trigger_price = 0
        elif order_type == "L":  # Limit order
            price = trigger_price
            trigger_price = 0
        elif order_type == "SL-M":  # Stop Loss Market order
            price = 0

        # API call to place the order
        response  = client.place_order( trading_symbol=str(trading_symbol) , price=str(price), quantity=str(quantity),order_type=str(order_type),
                                transaction_type=transaction_type, trigger_price=str(trigger_price),exchange_segment="nse_fo",
                                product="NRML", validity="DAY",amo="NO", disclosed_quantity="0", market_protection="0", pf="N", tag=None)

        if response is not None:
            if response.get("stat") == "Ok" and response.get("stCode") == 200:
                msg = f"Order Placed successfully: {trading_symbol}"
                Telegram_Message(msg)
            elif response.get("stat") == "Not_Ok":
                msg1 = f"Order Placed Error : {trading_symbol}"
                msg2 = response.get("errMsg") or None
                Telegram_Message(msg1, msg2)
            else:
                msg1 = f"Order Placed Error : {trading_symbol}"
                msg2 = json.dumps(response, indent=2)
                Telegram_Message(msg1,msg2)
        else:
            msg = f"Order placed Error No response received: {trading_symbol}"
            Telegram_Message(msg)

        # Print and return response
        print(f"Order placed {trading_symbol} Response : ", response )
        return response

    except Exception as e:
        msg1 = f"Order Placed Error: {trading_symbol}"
        print(msg1,e)
        Telegram_Message(msg1,str(e))


# trading_symbol = "NIFTY25JAN23200CE"
# quantity = "75"
# Trigger_Price = 300
# transaction_type = "B"
# order_type = "SL"
# response = place_order(trading_symbol,quantity,Trigger_Price,transaction_type,order_type)
# Error Order Response: {'stCode': 5021, 'errMsg': 'Market is closed, do you want to place an AMO order', 'stat': 'Not_Ok'}
# ok Order Response   : {'nOrdNo': '250120000337756', 'stat': 'Ok', 'stCode': 200}
#________________________________________________________________________________________________________________________________________________

# modify_order  odify_order  odify_order  odify_order  odify_order  odify_order  odify_order  odify_order  odify_order  odify_order
def modify_order(order_id, trading_symbol, quantity, trigger_price, transaction_type, order_type, client):
    try:
        quantity = int(quantity)
        trigger_price = float(trigger_price)
        if order_type == "SL":  # Stop Loss order
            if transaction_type == "S":
                price = trigger_price - 0.50
            elif transaction_type == "B":
                price = trigger_price + 0.50
        elif order_type == "L":  # Limit order
            price = trigger_price
            trigger_price = 0
        elif order_type == "MKT":  # Market order
            price = 0
            trigger_price = 0

        response  = client.modify_order(order_id = order_id, trigger_price = str(trigger_price),price = str(price),
                        quantity = str(quantity), order_type = order_type, disclosed_quantity = "0", validity = "DAY" )

        if response is not None:
            if response.get("stat") == "Ok" and response.get("stCode") == 200:
                msg = f"Modify Order successfully: {trading_symbol}"
                Telegram_Message(msg)
            elif response.get("stat") == "Not_Ok":
                msg1 = f"Modify Order Error : {trading_symbol}"
                msg2 = response.get("errMsg") or None
                Telegram_Message(msg1, msg2)
            else:
                msg1 = f"Modify Order Error : {trading_symbol}"
                msg2 = json.dumps(response, indent=2)
                Telegram_Message(msg1,msg2)
        else:
            msg = f"Modify Order Error No response received: {trading_symbol}"
            Telegram_Message(msg)

        print("Order Response:", response )
        return response

    except Exception as e:
        msg1 = f"Modify Order Error : {trading_symbol}"
        print(msg1,e)
        Telegram_Message(msg1,str(e))


# trading_symbol = "NIFTY25JAN23200CE"
# order_id = "250119000000715"
# quantity = 75
# trigger_price = 1
# transaction_type = "B"
# order_type = "L"
# response = modify_order(order_id, trading_symbol, quantity, trigger_price, transaction_type, order_type)
# print(response)
# ok Error Order Response: {'nOrdNo': '250119000000715', 'stat': 'Ok', 'stCode': 200}  order_detail
#______________________________________________________________________________________________________________________________________

# cancel_order   cancel_order   cancel_order   cancel_order   cancel_order   cancel_order   cancel_order   cancel_order
def cancel_order(order_id,trading_symbol, client):
    try:
        response  = client.cancel_order( order_id = order_id )
        if response is not None:
            if response.get("stat") == "Ok" and response.get("stCode") == 200:
                msg = f"Cancel Order successfully: {trading_symbol}"
                Telegram_Message(msg)
            elif response.get("stat") == "Not_Ok":
                msg1 = f"Cancel Order Error : {trading_symbol}"
                msg2 = response.get("errMsg") or None
                Telegram_Message(msg1, msg2)
            else:
                msg1 = f"Cancel Order Error : {trading_symbol}"
                msg2 = json.dumps(response, indent=2)
                Telegram_Message(msg1,msg2)
        else:
            msg = f"Modify Order Error No response received: {trading_symbol}"
            Telegram_Message(msg)

        print("Order Response:", response )
        return response
    except Exception as e:
        msg1 = f"Cancel Order Error : {trading_symbol}"
        print(msg1,e)
        Telegram_Message(msg1,str(e))


# trading_symbol = "NIFTY25JAN23200CE"
# order_id = "250119000000718"
# response = cancel_order(order_id,trading_symbol)
# print(response)
# ok Order Response: {'result': '250120000480289', 'stat': 'Ok', 'stCode': 200}
#__________________________________________________________________________________________________________________________

# fetch_OrderBook   fetch_OrderBook   fetch_OrderBook   fetch_OrderBook   fetch_OrderBook   fetch_OrderBook   fetch_OrderBook   fetch_OrderBook
def fetch_OrderBook(client):
    try:
        live_time = get_live_datetime("live_time")
        if "09:20:00" <= live_time <= "23:59:00":
            # Direct API call and check
            ob_response = client.order_report()
            if ob_response.get("stat") == "Ok":
                df = pd.DataFrame(ob_response["data"])
                columns_needed = [ "nOrdNo", "ordSt", "expDt", "stkPrc", "optTp", "trdSym", "trnsTp", "prcTp", "qty", "cnlQty","fldQty", "trgPrc", "prc", "avgPrc", "ordDtTm" ]
                return df[columns_needed]
    except Exception as e:
        print( "fetch_OrderBook function Error :", e )

# Order_Book = fetch_OrderBook(kotak_client)
# print(Order_Book)
#_________________________________________________________________________________________________________________________________________________________________
# Order_Status  Order_Status  Order_Status  Order_Status  Order_Status  Order_Status  Order_Status  Order_Status
import json
def Order_Status(order_id, client):
    try:
        order_book = fetch_OrderBook(client)
        if order_book is None or order_book.empty:
            msg = f"Order_id : {order_id}, OrderBook Empty or None"
            Telegram_Message(msg)
            return None

        # Check if order_id exists directly
        match = order_book.loc[order_book["nOrdNo"] == order_id]
        if match.empty:
            msg = f"Order_id : {order_id}, Information Not Available"
            Telegram_Message(msg)
            return None
        else:
            return match.iloc[0].to_dict()  # Faster than converting to JSON
    except Exception as e:
        print("Order_Status function Error:", e)
        return None
# order_id = "250429000829748"
# Status = Order_Status(order_id, kotak_client)
# print(Status)
#_________________________________________________________________________________________________________________________________________________________________________
# fetch_positions  fetch_positions  fetch_positions  fetch_positions  fetch_positions  fetch_positions  fetch_positions  fetch_positions numeric_cols
def fetch_positions(client):
    try:
        res = client.positions()
        if res.get("stat") == "ok" and res.get("stCode") == 200:
            df = pd.DataFrame(res["data"])
            numeric_cols = ["cfBuyAmt", "cfSellAmt", "buyAmt", "sellAmt", "flBuyQty", "cfBuyQty", "cfSellQty", "flSellQty"]
            df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce', axis=0)
            df["Net_Qty"] = df.eval("(flBuyQty + cfBuyQty) - (cfSellQty + flSellQty)")
            return df
        return None
    except Exception as e:
        print("fetch_positions function Error:", e)
        Telegram_Message("fetch_positions function Error: " + str(e))
        return None
# Example usage
# Positions = fetch_positions(kotak_client)
# print(tabulate(Positions, headers="keys", tablefmt="pretty", showindex=True))
#_________________________________________________________________________________________________________________________________________________________________________

# fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty  fetch_Qty
def fetch_Qty(client, Tokens):
    try:
        Positions = fetch_positions(client)
        if Positions is None:
           return 0
        row = Positions.loc[Positions["tok"] == str(Tokens)]
        if not row.empty:
            return row["Net_Qty"].values[0]
        else:
            return 0 
    except Exception as e:
        print("fetch_Qty_from_cache Error:", e)
        Telegram_Message("fetch_Qty_from_cache Error: " + str(e))
        return 0

# Example usage
# Tokens = 38604
# Qty = fetch_Qty(kotak_client, Tokens)
# print(Qty)
#_________________________________________________________________________________________________________________________________________________________________________

from datetime import datetime, timedelta, time
from tabulate import tabulate
import math
import json
import time as tm

# Execution_function   Execution_function   Execution_function   Execution_function   Execution_function   Execution_function   Execution_function   Execution_function   Execution_function  
def Execution_function(trading_symbol, Symboltoken, quantity, price, transaction_type, Timeout, client):
     try:
        response  =   place_order( trading_symbol    = trading_symbol,
                                      quantity          = quantity,
                                      trigger_price     = price,
                                      transaction_type  = transaction_type,
                                      order_type        = "L",
                                      client            = client, ) 
        if response.get("stat") == "Ok" and response.get("stCode") == 200:
            order_id = response["nOrdNo"]
            for _ in range(Timeout):
                order_detail = Order_Status(order_id, client)
                status = order_detail.get("ordSt")
                if status == "complete":
                    return response
                tm.sleep(1)
            
            Position_QTY = fetch_Qty(client, Symboltoken)
            modify_quantity = quantity - int(abs(Position_QTY))
            if modify_quantity <= 0:
               return None
            modify_response = modify_order(order_id         = order_id , 
                                              trading_symbol   = trading_symbol, 
                                              quantity         = modify_quantity,
                                              trigger_price    = 310,  #  0
                                              transaction_type = transaction_type, 
                                              order_type       = "L",  # MKT
                                              client           =  client   )
            if modify_response.get("stat") == "Ok" and response.get("stCode") == 200:
               return modify_response
            else:
               msg1 = f"modify order Error : {trading_symbol}"
               print(msg1)
               Telegram_Message(msg1)
               return None
        else:
            msg1 = f"Limit Order Placed Error : {trading_symbol}"
            print(msg1)
            Telegram_Message(msg1)
            return None      

     except Exception as e:
        msg1 = f"Execution_function Error : {trading_symbol}"
        print(msg1,e)
        Telegram_Message(msg1,str(e))
        return None

# trading_symbol  = "NIFTY2550824400PE"
# Symboltoken     = 38607
# quantity        = 75
# price           = 300
# transaction_type= "S"
# Timeout         = 10
# client          = kotak_client
# response = Execution_function(trading_symbol, Symboltoken, quantity, price, transaction_type, Timeout, client)
# print(response)
#__________________________________________________________________________________________________________________________________________________

def Entry_Data (target_dict, Symbol, Symboltoken, StrikePrice, OptionType, Sell_Price, Quantity, Exit_Type, SELL_orderid = None, Entry_Time = None, Close_915 = None, Close_PC = None ) :
        try:
          Top_Loss = math.ceil((float(Sell_Price) * 1.20) * 20) / 20 # 
          TSL_1    = math.ceil((float(Sell_Price) * 0.80) * 20) / 20
          TSL_2    = math.ceil((float(Sell_Price) * 0.60) * 20) / 20
          Target   = math.floor((float(Sell_Price)* 0.55) * 20) / 20

          if Exit_Type == "Top_Loss":
              Exit_Trigger = Top_Loss
              Exit_Type = "Top Loss"
          elif Exit_Type == "TSL_1":
              Exit_Trigger = Sell_Price
              Exit_Type = "TSL-1"
          elif Exit_Type == "TSL_2":
              Exit_Trigger = TSL_1
              Exit_Type = "TSL-2"

          Sell ={ f"{OptionType}_SELL_orderid": SELL_orderid,   f"{OptionType}_Entry_Time": Entry_Time, f"{OptionType}_SL_orderid": None,
                  f"{OptionType}_SL_orderDate": None,           f"{OptionType}_Symbol": Symbol,         f"{OptionType}_Symboltoken": Symboltoken,
                  f"{OptionType}_StrikePrice": StrikePrice,     f"{OptionType}_Close_915": Close_915,   f"{OptionType}_Close_PC": Close_PC,
                  f"{OptionType}_Sell_Qty": Quantity,           f"{OptionType}_Sell_Price": Sell_Price, f"{OptionType}_Top_Loss": Top_Loss,
                  f"{OptionType}_TSL_1": TSL_1,                 f"{OptionType}_TSL_2": TSL_2,           f"{OptionType}_Target": Target,
                  f"{OptionType}_Exit_Price": None,             f"{OptionType}_Exit_Time": None,        f"{OptionType}_Exit_Type": Exit_Type,
                  f"{OptionType}_Exit_Trigger": Exit_Trigger,   f"{OptionType}_LTP": None  }

          #WebSoket_subscribe(Symboltoken)

          update_variable(target_dict, "Yes", f"{OptionType}_Tred")
          update_variable(target_dict, Sell, f"{OptionType}_Detail")

          # Print JSON स्ट्रिंग के रूप में फॉर्मेट करें
          tabulate_data = [[key, value] for key, value in Sell.items()]
          print(tabulate(tabulate_data, headers=['Key', 'Value'], tablefmt='pretty'))
          formatted_message = json.dumps(Sell, indent=2)
          Telegram_Message(f"{OptionType}_Entry : Place Market Order Complete.",formatted_message)


        except Exception as e:  # Error handling and retry logic
            error_msg = f"Entry_Data function Error:"
            Telegram_Message(error_msg, str(e))
            print(error_msg, e)

# # Example usage
# StrikePrice = 23250
# OptionType = "PE"
# Sell_Price = 255.15
# Quantity = 375
# Exit_Type = "TSL_1"  # "Top_Loss" , "TSL_1" , "TSL_2"
# ExpiryDates = Next_Expiry  # Curnent_Expiry , Next_Expiry
# Symbol, Symboltoken = Symbol_SymbolToken("24200","CE", ExpiryDates)
# Kotak_Symbol = fetch_Kotak_Symbol(Symboltoken)
# Entry_Data (Kotak_Symbol, Symboltoken, StrikePrice, OptionType, Sell_Price, Quantity, Exit_Type )
#__________________________________________________________________________________________________________________________________________________

# Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry  Entry
def Entry(OptionType, Sell_Quantity, Execution, target_dict, Candal_Data, Kotak_Scrip_Data, client):
    if "09:20:00" <= get_live_datetime("live_time") <= "23:59:00":
      if Read_Variable( target_dict,f"{OptionType}_Tred") is None and  Candal_Data[OptionType]["Tred"] == "Yes" :
         Symboltoken  = Candal_Data[OptionType]["Symboltoken"]
         Close_915    = Candal_Data[OptionType]["Close_915"]
         Close_PC     = Candal_Data[OptionType]["Close_PC"]
         StrikePrice  = Candal_Data[OptionType]["StrikePrice"]
         Kotak_Symbol = fetch_Kotak_Symbol(Symboltoken, Kotak_Scrip_Data)
         Sell_Price   = (Close_PC + 1)

         if Execution == "Live_Auto" :
            # response  = place_order(Kotak_Symbol, Sell_Quantity, trigger_price = 0, transaction_type="S", order_type="MKT", client = kotak_client)
            response  = Execution_function(Kotak_Symbol, Symboltoken, Sell_Quantity, Sell_Price, transaction_type = "S", Timeout = 10, client = client)
         
         if Execution == "Offline" :
            response  =  {'nOrdNo': '123', 'stat': 'Ok', 'stCode': 200}
            Offline = {'nOrdNo': '123', 'ordSt': 'complete', 'ordDtTm': get_live_datetime("live_datetime"),'trdSym': Kotak_Symbol,
                        'stkPrc': StrikePrice, 'fldQty': Sell_Quantity, 'avgPrc' : Sell_Price }

         if response is not None and response.get("stat") == "Ok" and response.get("stCode") == 200:
            order_id = response["nOrdNo"]
            Order_Detail = Order_Status(order_id, client) if Execution == "Live_Auto" else Offline
            Status = Order_Detail.get("ordSt")
            if Status == "complete":   # complete
               Sell_orderid = Order_Detail.get("nOrdNo")
               Entry_Time   = Order_Detail.get("ordDtTm")
               Symbol       = Order_Detail.get("trdSym")
               StrikePrice  = Order_Detail.get("stkPrc")
               Quantity     = Order_Detail.get("fldQty")
               Sell_Price   = Order_Detail.get("avgPrc")

               Entry_Data ( target_dict, Kotak_Symbol, Symboltoken, StrikePrice, OptionType, Sell_Price, Quantity = Quantity, Exit_Type ="Top_Loss",
                            SELL_orderid = Sell_orderid, Entry_Time = Entry_Time, Close_915 = Close_915, Close_PC = Close_PC )
            else :
               msg = f"Entry Order Status : {Status}"
               print(msg)
               Telegram_Message(msg)
         else :
            msg = f"Entry Order Error : {Kotak_Symbol}"
            print(msg)
            Telegram_Message(msg)

# # Example usage
# Entry("CE", 75, "Offline", CE_Detail, Candal_Data, Kotak_Scrip_Data, kotak_client) # Live_Auto Offline
# Entry("PE", 75, "Offline", PE_Detail, Candal_Data, Kotak_Scrip_Data, kotak_client) # Live_Auto Offline
#__________________________________________________________________________________________________________________________________________________

