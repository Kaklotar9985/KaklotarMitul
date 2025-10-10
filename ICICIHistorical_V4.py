#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  ICICI_Login   ICICI_Login     ICICI_Login  ICICI_Login     ICICI_Login     ICICI_Login     ICICI_Login     ICICI_Login      ICICI_Login   ICICI_Login
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from breeze_connect import BreezeConnect
import urllib
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
#  Data_Error  Error_Data_to_Excel (v2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
Error_Data = {}
def Data_Error(stock_name, Expiry_Date, Strike_Price=None, Options_Type=None, Error_Date=None, Function_Error=None, API_Error = None):
    global Error_Data
    try:
        if not (stock_name and Expiry_Date and Strike_Price and Options_Type and Error_Date):
            print("⚠️ stock_name, Expiry_Date, Strike_Price, Options_Type aur Error_Date dena zaroori hai!")
            return
        if Expiry_Date not in Error_Data:
            Error_Data[Expiry_Date] = {}
        if Strike_Price not in Error_Data[Expiry_Date]:
            Error_Data[Expiry_Date][Strike_Price] = []
        Error_Data[Expiry_Date][Strike_Price].append({"stock_name": stock_name,"Expiry_Date": Expiry_Date,"Strike_Price": Strike_Price,
            "Options_Type": Options_Type,"Error_Date": Error_Date,"Function_Error": Function_Error,"API_Error": API_Error})
    except Exception as e:
        print(f"Data_Error Function Error: {e}")
def Error_Data_to_Excel(filename="Error_Data"):
    global Error_Data
    try:
        rows = []
        for expiry, strikes in Error_Data.items():
            for strike, errors in strikes.items():
                for err in errors:
                    rows.append([err.get("stock_name"),err.get("Expiry_Date"),err.get("Strike_Price"),err.get("Options_Type"),
                                 err.get("Error_Date"),err.get("Function_Error"),err.get("API_Error")])

        if not rows:
            print("⚠️ Error_Data खाली है, Excel file नहीं बनी।")
            return None
        df = pd.DataFrame(rows, columns=["stock_name", "Expiry_Date", "Strike_Price", "Options_Type",
                                         "Error_Date", "Function_Error", "API_Error"])
        df = df.sort_values(by=["Expiry_Date", "Strike_Price", "Error_Date"]).reset_index(drop=True)
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        filename = f"{filename}_Error.xlsx"
        df.to_excel(filename, sheet_name="ErrorLogs", index=False)
        print(f"✅ Error data Excel में save हो गया: {filename}")
        Error_Data.clear()
        return filename
    except Exception as e:
        print(f"Error_Data_to_Excel Function Error: {e}")
        return None
# # Example Usage
# Data_Error("Reliance", "30-01-2025", 2500, "CE", "2025-09-12 10:30", "Connection Error", "Timeout 504")
# Data_Error("Reliance", "30-01-2025", 2500, "PE", "2025-09-12 10:40", "Invalid Response", "Server Down")
# Data_Error("TCS", "06-02-2025", 3600, "CE", "All Date", "No Data", "Empty Result")
# Error_Data_to_Excel("Error_Logs/ICICI_Option")
#=======================================================================================================================================================================
