# login_to_5paisa  login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   

#!pip install py5paisa
#!pip install pyotp
from py5paisa import FivePaisaClient
from py5paisa.order import OrderType, Exchange
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
from SmartApi import SmartConnect
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
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

# feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket  feed Anjal_WebSoket
feedjson = {}
ATM_Strik = None
Nifty_LTP = None
WebSoket_Status = None

def on_data(wsapp, message):
    global feedjson, ATM_Strik, Nifty_LTP
    try:
        # Convert token to string for consistent key matching
        token = str(message.get("token"))
        
        # Extract market data (handle division by zero)
        last_traded_price = (message.get("last_traded_price") or 0) / 100
        
        # Handle empty bid/ask data gracefully
        buy_data = message.get("best_5_buy_data", [{}])
        sell_data = message.get("best_5_sell_data", [{}])
        
        Bid_price = (max(item.get('price', 0) for item in buy_data) or 0
        Ask_price = (min(item.get('price', 0) for item in sell_data)) or 0
        
        # Update feed dictionary
        feedjson[token] = {
            "token": token,
            "last_traded_price": last_traded_price,
            "Bid_price": Bid_price,
            "Ask_price": Ask_price
        }
        
        # Update Nifty LTP only for token 26000
        if token == "26000":  # Match string token
            Nifty_LTP = last_traded_price
            ATM_Strik = round(Nifty_LTP / 50) * 50
            
    except Exception as e:
        print(f"WebSocket Data Error: {str(e)}")

def on_open(wsapp):
    global WebSoket_Status
    print("Anjal_WebSocket: Connected")
    WebSoket_Status = "Open"
    
    # Subscribe to Nifty 50 index (token 26000)
    token_list = [{
        "exchangeType": 1,      # NSE
        "tokens": ["26000"]    # Use string token
    }]
    
    # Start subscription
    try:
        sws.subscribe("nifty_feed", 3, token_list)  # Mode 3 for LTP
    except Exception as e:
        print(f"Subscription Error: {str(e)}")

def on_error(wsapp, error):
    global WebSoket_Status
    WebSoket_Status = "Error"
    print("Anjal_WebSoket : Error")

def on_close(wsapp):
    global WebSoket_Status
    print("Anjal_WebSoket : Close")
    WebSoket_Status = "Close"


def close_connection():
    sws.close_connection()
    print("Anjal_WebSoket : Connection closed manually.")

# ____________________________________________________________________________________________________________________________________________________
