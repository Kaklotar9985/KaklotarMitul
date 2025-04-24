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

# fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time # fetch_Date_Time
from datetime import datetime, timedelta
import threading
import time
import pytz

def fetch_Date_Time():
    global live_time , live_date , Candle_Date , First_Candle_Time , Previous_Candal_Time
    max_retries = 3
    retries = 0

    while retries < max_retries:  # री-ट्राई चक्र  datetime
        try :
            ist = pytz.timezone('Asia/Kolkata')
            now = datetime.now(ist)
            live_time = now.strftime("%H:%M:%S")  # समय (घंटा:मिनट:सेकंड)
            live_date = now.strftime("%d-%m-%Y")  # तारीख (दिन-महीना-वर्ष)

            First_Candle_Time = "09:15"

            # यदि लाइव डेट शनिवार या रविवार है, तो शुक्रवार की तारीख निकालें
            if now.weekday() == 5:  # शनिवार
                Candle_Date = (now - timedelta(days=1)).strftime("%Y-%m-%d")
            elif now.weekday() == 6:  # रविवार
                Candle_Date = (now - timedelta(days=2)).strftime("%Y-%m-%d")
            elif live_time < "09:15:01":
                Candle_Date = (now - timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                Candle_Date = now.strftime("%Y-%m-%d")  # अन्य दिनों में लाइव डेट का उपयोग करें

            # मिनट को राउंड करके पिछले 5 मिनट की कैंडल का समय निकालें
            minute = now.minute
            rounded_minute = (minute // 5) * 5 - 5

            if rounded_minute < 0:
                rounded_minute = 55
                now = now - timedelta(hours=1)

            Time_rounded = now.replace(minute=rounded_minute, second=0, microsecond=0).strftime("%H:%M")

            if "15:30" >= Time_rounded >= "09:15":
                Previous_Candal_Time = Time_rounded
            else:
                Previous_Candal_Time = "15:25"

            # print("fetch_Date_Time successfully")
            # सफल होने पर लूप से बाहर निकलें
            break

        except Exception as e:   # त्रुटि संदेश और री-ट्राई लॉजिक
            retries += 1
            Error = f"fetch_Date_Time function Error :"
            print( Error, e )
            time.sleep(1)  # री-ट्राई से पहले थोड़ी प्रतीक्षा करें

    # यदि अधिकतम री-ट्राई के बाद भी डेटा न मिले
    if retries == max_retries:
        Error = f"fetch_Date_Time function Error Max Re-try : {max_retries}"
        print(Error)

# # उदाहरण के लिए
fetch_Date_Time()
# threading.Thread(target=fetch_Date_Time).start()
# print("Live Date:", live_date)
# print("Live Time:", live_time)
# print("Candle Date:", Candle_Date)
# print("First Candle Time:", First_Candle_Time)
# print("Previous Candle Time:", Previous_Candal_Time)
#_________________________________________________________________________________________________________________________________________________________________

# Live_Time_Run_Function  # Live_Time_Run_Function  # Live_Time_Run_Function  # Live_Time_Run_Function  # Live_Time_Run_Function  # Live_Time_Run_Function
def Run_fetch_Date_Time():
    try:
        while True:
             fetch_Date_Time()
    except Exception as e:
        Error =  f"Run_fetch_Date_Time function Error: {e}"
        print(Error)
threading.Thread(target=Run_fetch_Date_Time).start()
#________________________________________________________________________________________________________________________________________________________________

# fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data   fetch_Scrip_Data  
from datetime import datetime, timedelta
import pandas as pd
import requests
def fetch_Scrip_Data():
    global All_Scrip_Data
    try:
        url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
        All_Scrip_Data = pd.DataFrame(requests.get(url).json())
        return All_Scrip_Data
    except Exception as e:
        print(f"fetch_Scrip_Data Function Error: {e}")
        return None
All_Scrip_Data = fetch_Scrip_Data()
#___________________________________________________________________________________________________________________________________________________________________________

# fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data # fetch_Scrip_Data
def fetch_Scrip_Data():
    global Scrip_Data, All_Scrip_Data
    try :
        Scrip_Data_Exchange_filter = All_Scrip_Data[All_Scrip_Data['exch_seg'] == "NFO"]
        Scrip_Data_Name_filter = Scrip_Data_Exchange_filter[Scrip_Data_Exchange_filter['name'] == "NIFTY"]
        Scrip_Data_instrumenttype_filter = Scrip_Data_Name_filter[Scrip_Data_Name_filter['instrumenttype'] == "OPTIDX" ]
        Scrip_Data = Scrip_Data_instrumenttype_filter
        return Scrip_Data
    except Exception as e:
        print("fetch_Scrip_Data function Error : ", e )
Scrip_Data = fetch_Scrip_Data()
#________________________________________________________________________________________________________________________________________________________________________

# fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate  # fetch_ExpiryDate
def fetch_ExpiryDate():
    global Curnent_Expiry , Next_Expiry ,Expiry_List
    try :
        today = datetime.now().strftime('%d%b%Y')
        Expiry_Data = sorted(Scrip_Data['expiry'].unique(), key=lambda x: datetime.strptime(x, '%d%b%Y'))
        Expiry_List = [expiry for expiry in Expiry_Data if datetime.strptime(expiry, "%d%b%Y") >= datetime.strptime(today, "%d%b%Y")]
        Curnent_Expiry = datetime.strptime(Expiry_List[0], '%d%b%Y').strftime('%d%b%y').upper()
        Next_Expiry = datetime.strptime(Expiry_List[1], '%d%b%Y').strftime('%d%b%y').upper()
    except Exception as e:   # त्रुटि संदेश और री-ट्राई लॉजिक
        print( f"fetch_ExpiryDate function Error : ", e )
fetch_ExpiryDate ()
#_________________________________________________________________________________________________________________________________________________________________

# Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken  # Symbol_SymbolToken
def Symbol_SymbolToken(Strike,Option_Type,Expiry = Next_Expiry, Index = "NIFTY"):
    try:
        Token = f"{Index}{Expiry}{Strike}{Option_Type}"
        SymbolToken = Scrip_Data[Scrip_Data['symbol'].str.contains(Token, case=False, na=False)]['token'].iloc[0]
        Symbol = Scrip_Data[Scrip_Data['symbol'].str.contains(Token, case=False, na=False)]['symbol'].iloc[0]
        return Symbol , SymbolToken
    except Exception as e: 
        print( f"Symbol_SymbolToken function Error : ", e )
# # उदाहरण के लिए
# Symbol,SymbolToken = Symbol_SymbolToken("24200","CE", Expiry = Next_Expiry)
# print(f"Symbol      : {Symbol}")
# print(f"SymbolToken : {SymbolToken}")
#______________________________________________________________________________________________________________________________________________________________________________

# fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data  # fetch_Candal_Data
Candal_Data = {}
def fetch_Candal_Data(symboltoken, Symbol, StrikePrice, OP_tipe):
    global Candle_Date, First_Candle_Time, Previous_Candal_Time

    try:
        if "09:20:00" <= live_time <= "15:31:00" :
            historicParam = {"exchange": "NFO","symboltoken": symboltoken, "interval": "FIVE_MINUTE", "fromdate": f"{Candle_Date} 09:00", "todate": f"{Candle_Date} 15:30"}
            response = smartApi.getCandleData(historicParam)
            if response.get("data"):
                DATA = pd.DataFrame(response["data"], columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
                DATA['Time'] = pd.to_datetime(DATA['Time'])
                DATA['Date'] = DATA['Time'].dt.strftime('%d-%m-%Y')
                DATA['Time'] = DATA['Time'].dt.strftime('%H:%M')

                # 9:15 और पिछले कैंडल के क्लोज प्राइस निकालें  Close_PC
                close_price = DATA.loc[DATA['Time'] == First_Candle_Time, 'Close']
                previous_price = DATA.loc[DATA['Time'] == Previous_Candal_Time, 'Close']

                Tred = None  # Initialize Tred
                if not close_price.empty and not previous_price.empty:
                    Close_915 = float(close_price.values[0])  # Ensure numeric
                    Close_PC = float(previous_price.values[0])  # Ensure numeric
                    Tred = "Yes" if Close_915 > Close_PC else None
                else:
                    Close_915 = None
                    Close_PC = None

                # डेटा अपडेट करें
                return { "Symbol": Symbol, "Symboltoken": symboltoken, "StrikePrice": StrikePrice , "OP_tipe" : OP_tipe  , "Close_915": Close_915, "Close_PC": Close_PC,"Tred" : Tred }
    except Exception as e:
        print(f"fetch_Candal_Data function Error :", e)

# # उदाहरण के लिए
# fetch_Candal_Data(symboltoken,Symbol,StrikePrice,OP_tipe)
# print(tabulate(pd.DataFrame(Candal_Data), headers='keys', tablefmt='pretty', showindex=True))
#__________________________________________________________________________________________________________________________________________________________________________________________________________________

# fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token  # fetch_Token
def fetch_Token(strike, name="NIFTY", exch_seg="NFO"):
    try :
        CEstrike = strike
        PEstrike = str(int(strike) + 50)
        CEToken = f"{name}{Next_Expiry}{CEstrike}CE"
        PEToken = f"{name}{Next_Expiry}{PEstrike}PE"
        CE_SymbolToken = Scrip_Data[Scrip_Data['symbol'].str.contains(CEToken, case=False, na=False)]['token'].iloc[0]
        CE_Symbol = Scrip_Data[Scrip_Data['symbol'].str.contains(CEToken, case=False, na=False)]['symbol'].iloc[0]
        PE_SymbolToken = Scrip_Data[Scrip_Data['symbol'].str.contains(PEToken, case=False, na=False)]['token'].iloc[0]
        PE_Symbol = Scrip_Data[Scrip_Data['symbol'].str.contains(PEToken, case=False, na=False)]['symbol'].iloc[0]
        Call = fetch_Candal_Data(CE_SymbolToken,CE_Symbol,CEstrike,"CE")
        Put  = fetch_Candal_Data(PE_SymbolToken,PE_Symbol,PEstrike,"PE")
        Candal_Data = { "CE" : Call , "PE" : Put }
        return Candal_Data
    except Exception as e:
        print( "fetch_Token function Error : ", e )

# # उदाहरण के लिए
# fetch_Token(ATM_Strik)
# fetch_Token("24500")
# print(tabulate(pd.DataFrame(Candal_Data), headers='keys', tablefmt='pretty', showindex=True))
#________________________________________________________________________________________________________________________________________________________





