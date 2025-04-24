from py5paisa import FivePaisaClient
from py5paisa.order import OrderType, Exchange
import pyotp

# login_to_5paisa  login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   login_to_5paisa   
def login_to_5paisa(cred):
    try:
        totp = pyotp.TOTP(cred["token"]).now()
        client = FivePaisaClient(cred=cred)
        client.get_totp_session(cred["ClientCode"], totp, cred["pin"])
        access_token = client.get_access_token()
        client.set_access_token(access_token, cred["ClientCode"])
        print("✅ Login Successful to 5Paisa for Client:", cred["ClientCode"])
        return client
    except Exception as e:
        print("❌ 5paisa Login Failed:", str(e))
        return None
#____________________________________________________________________________________________________________________________________________________________________________________
