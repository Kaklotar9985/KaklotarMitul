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
