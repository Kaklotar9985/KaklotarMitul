from IPython.display import clear_output
import logging
# Disable Breeze API debug logs
logging.getLogger("APILogger").setLevel(logging.CRITICAL)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Data_Error  Error_Data_to_Excel     Data_Error  Error_Data_to_Excel     Data_Error  Error_Data_to_Excel     Data_Error  Error_Data_to_Excel      Data_Error  Error_Data_to_Excel
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
Error_Data = {}
def Data_Error(Error, Expiry_Date=None, Strike_Price=None, Error_Datetime=None):
    global Error_Data
    try:
        if Expiry_Date is None or Strike_Price is None or Error_Datetime is None:
            print("⚠️ Expiry_Date, Strike_Price aur Error_Datetime dena zaroori hai!")
            return
        if Expiry_Date not in Error_Data:
            Error_Data[Expiry_Date] = {}
        if Strike_Price not in Error_Data[Expiry_Date]:
            Error_Data[Expiry_Date][Strike_Price] = {}
        Error_Data[Expiry_Date][Strike_Price][Error_Datetime] = Error
    except Exception as e:
        print(f"Data_Error Function Error: {e}")

def Error_Data_to_Excel(filename="Error_Data"):
    global Error_Data
    try:
        rows = []
        for expiry, strikes in Error_Data.items():
            for strike, errors in strikes.items():
                for dt, err in errors.items():
                    rows.append([expiry, strike, dt, err])

        if not rows:
            print("⚠️ Error_Data khali hai, Excel file nahi bani.")
            return

        # DataFrame banao
        df = pd.DataFrame(rows, columns=["Expiry_Date", "Strike_Price", "Error_Datetime", "Error"])
        df = df.sort_values(by=["Expiry_Date", "Strike_Price", "Error_Datetime"])

        # "All Date" filtering logic
        all_date_strikes = df.loc[df["Error_Datetime"] == "All Date", "Strike_Price"].unique()

        filtered_data = df[ (df["Strike_Price"].isin(all_date_strikes) & (df["Error_Datetime"] == "All Date")) |
                            (~df["Strike_Price"].isin(all_date_strikes))  ].reset_index(drop=True)

        # folder banana (agar exist nahi karta to)
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        filename = f"{filename}_Error.xlsx"
        filtered_data.to_excel(filename, sheet_name="ErrorLogs", index=False)
        print(f"✅ Error data Excel me save ho gaya: {filename}")

        # Clear dict after saving
        Error_Data.clear()
        return filename

    except Exception as e:
        print(f"Error_Data_to_Excel Function Error: {e}")
        return None

# # Example usage
# Data_Error("Connection Error", "30-01-2025", 2500, "2025-09-12 10:30")
# Data_Error("Timeout Error", "30-01-2025", 2500, "2025-09-12 10:35")
# Data_Error("Server Error", "30-01-2025", 2600, "2025-09-12 10:40")
# # Save Excel in folder "30-01-2025"
# Expiry_Date = '30-01-2025'
# Excel_Name = os.path.join(Expiry_Date, f"{Expiry_Date}")
# Error_Data_to_Excel(Excel_Name)
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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fetch_ICICI_Historical_Data   Fetch_ICICI_Historical_Data   Fetch_ICICI_Historical_Data   Fetch_ICICI_Historical_Data   Fetch_ICICI_Historical_Data   Fetch_ICICI_Historical_Data
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from IPython.display import clear_output
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from tabulate import tabulate
from dateutil import parser
import pandas as pd
import threading
import http.client
import time

CALL_LIMIT = 95
Total_Count = 0
Start_Time = time.time()

def rate_limiter():
    global Total_Count, Start_Time
    now = time.time()
    if now - Start_Time >= 60:
        Total_Count = 0
        Start_Time = now
    Total_Count += 1

    if Total_Count > CALL_LIMIT:
        sleep_time = 60 - (now - Start_Time)
        if sleep_time > 0:
            time.sleep(sleep_time)
        Total_Count = 1
        Start_Time = time.time()

# # Example usage
# for i in range(100):   # 15 बार call करेंगे
#     rate_limiter()
#     print(f"API Call {i+1} done at {time.strftime('%H:%M:%S')}")
#     time.sleep(0.005)   # हर call के बीच 0.5s का gap रखा

def safe_get_historical_data(breeze, interval, from_date, to_date, stock_code,
                             exchange_code, product_type, expiry_date_api, right, strike_price,
                             max_retries=3, delay=2):
    attempt = 0
    right_Data = None
    
    while attempt < max_retries:
        try:
            rate_limiter()  # ✅ पहले limit check करो

            # API Call
            right_Data = breeze.get_historical_data_v2(interval=interval,from_date=from_date,to_date=to_date,stock_code=stock_code,exchange_code=exchange_code, 
                                                       product_type=product_type,expiry_date=expiry_date_api,right=right,strike_price=strike_price  )
            
            if right_Data is not None and right_Data.get("Error") is None and right_Data.get("Success"):
                return right_Data  # ✅ Success

            elif right_Data.get("Error") == "Rate Limit Exceeded":
                time.sleep(60)  # Breeze ने बोला limit exceed → wait 1 min

            elif right_Data.get("Error") == "API did not return any response":
                break

            elif right_Data.get("Error") is None:
                break

        except http.client.IncompleteRead as e:
            attempt += 1
            print(f"⚠️ IncompleteRead Error on attempt {attempt}, retrying... ({e})")
            if attempt < max_retries:
                time.sleep(delay)
                continue  # retry करो

        except Exception as e:
            attempt += 1
            print(f"⚠️ Exception on attempt {attempt}: {e}")
            if attempt < max_retries:
                time.sleep(delay)

        attempt += 1

    # अगर max retries के बाद भी fail
    Error_msg = None
    if right_Data and isinstance(right_Data, dict):
        Error_msg = right_Data.get("Error", "No Error Data")
    if Error_msg is None:
        Error_msg = "API did not return any response"

    return {"Error": f"Failed after {max_retries} Retries, API_Error: {Error_msg}", "Success": None}

def Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day):
    try:
        final_df = pd.DataFrame()
        Options_Type = "NA"

        Expiry_Date = datetime.strptime(Expiry_Date, "%d-%m-%Y")
        ToDate = datetime.today()
        End_Date = min(Expiry_Date, ToDate)  + timedelta(days=1)
        Start_Date = End_Date - timedelta(days=past_day)
        Start_Date = Start_Date.replace(hour=9, minute=15, second=0)
        expiry_date_api = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")
        if product_type in ("futures", "cash"):
            from_date_api = Start_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date_api = End_Date.strftime("%Y-%m-%dT00:00:00.000Z")

            right_Data = safe_get_historical_data( breeze, interval, from_date_api, to_date_api, stock_code,
                exchange_code, product_type, expiry_date_api, right, strike_price,  max_retries=3, delay=0 )

            if right_Data["Error"] is None and right_Data["Success"]:
                if product_type == "futures":
                    Options_Type = "fu"
                elif product_type == "cash":
                    Options_Type = "ch"
                Column = ["stock_code", "expiry_date", "datetime", f"{Options_Type}_open", f"{Options_Type}_high",
                          f"{Options_Type}_low", f"{Options_Type}_close", f"{Options_Type}_volume", f"{Options_Type}_oi"]

                Data = pd.DataFrame(right_Data["Success"])
                Data['datetime'] = Data['datetime'].apply(lambda x: parser.parse(x).strftime('%d-%m-%Y %H:%M'))

                if "expiry_date" in Data.columns:
                    Data['expiry_date'] = Data['expiry_date'].apply(lambda x: parser.parse(x).strftime("%d-%m-%Y"))
                else:
                    Data['expiry_date'] = Expiry_Date.strftime("%d-%m-%Y")

                rename_map = { "open": f"{Options_Type}_open", "high": f"{Options_Type}_high", "low": f"{Options_Type}_low",
                              "close": f"{Options_Type}_close", "volume": f"{Options_Type}_volume" }

                if "open_interest" in Data.columns:
                    rename_map["open_interest"] = f"{Options_Type}_oi"

                Data = Data.rename(columns=rename_map)
                valid_cols = [col for col in Column if col in Data.columns]
                Data = Data[valid_cols]
                final_df = pd.concat([Data, final_df], ignore_index=True)

        elif product_type == "options":
            # Loop start (latest se shuru karke peeche ki taraf)
            Options_Type = right
            current_to = End_Date
            while current_to > Start_Date:
                # print(f"current_to: {current_to.strftime('%d-%m-%Y %H:%M')}",f"Start_Date: {Start_Date.strftime('%d-%m-%Y %H:%M')}")
                from_date_api = (Start_Date  - timedelta(days=5)).strftime("%Y-%m-%dT00:00:00.000Z")
                to_date_api   = current_to.strftime("%Y-%m-%dT%H:%M:%S.000Z")

                right_Data = safe_get_historical_data(breeze, interval, from_date_api, to_date_api, stock_code,
                    exchange_code, product_type, expiry_date_api, right, strike_price, max_retries=3, delay=0)

                Error   = right_Data.get("Error")
                Success = right_Data.get("Success")

                if Error is None and Success:
                  Column = ["stock_code", "expiry_date", "strike_price", "datetime", f"{Options_Type}_open",
                            f"{Options_Type}_high", f"{Options_Type}_low", f"{Options_Type}_close",
                            f"{Options_Type}_volume", f"{Options_Type}_oi"]

                  Data = pd.DataFrame(right_Data["Success"])

                  # Check if we got any data for this day
                  if len(Data) > 0:
                      Data['datetime'] = Data['datetime'].apply(lambda x: parser.parse(x).strftime('%d-%m-%Y %H:%M'))

                      if "expiry_date" in Data.columns:
                          Data['expiry_date'] = Data['expiry_date'].apply(lambda x: parser.parse(x).strftime("%d-%m-%Y"))
                      else:
                          Data['expiry_date'] = Expiry_Date.strftime("%d-%m-%Y")

                      rename_map = { "open" : f"{Options_Type}_open",  "high": f"{Options_Type}_high", "low": f"{Options_Type}_low",
                                      "close": f"{Options_Type}_close", "volume": f"{Options_Type}_volume" }

                      if "open_interest" in Data.columns:
                          rename_map["open_interest"] = f"{Options_Type}_oi"

                      Data = Data.rename(columns=rename_map)
                      valid_cols = [col for col in Column if col in Data.columns]
                      Data = Data[valid_cols]
                    
                      final_df = pd.concat([Data, final_df], ignore_index=True)

                      # Get the earliest datetime from the fetched data
                      Data['datetime_dt'] = pd.to_datetime(Data['datetime'], format='%d-%m-%Y %H:%M')
                      
                      first_time = Data['datetime_dt'].min()
                      if first_time <= Start_Date:
                         break
                      current_to = first_time - timedelta(minutes=1)
                  else :
                      current_to = current_to - timedelta(days=1)

                else:
                    Error_msg    = right_Data.get("Error", None)
                    if Error_msg:
                      Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
                      Error_Strike = f"{strike_price} - {Options_Type}"
                      Error_Date   = datetime.strptime(to_date_api[:10], "%Y-%m-%d").strftime("%d-%m-%Y")
                      Data_Error(f"ICICI_Historical Error : {Error_msg}", Error_Expiry, Error_Strike, Error_Date)      

                # Add a small delay to avoid hitting API rate limits
                import time
                time.sleep(0.1)

        # Combine all dataframes
        if not final_df.empty:
            Analysis_Data = final_df.copy()

            # Convert to datetime for proper sorting
            Analysis_Data["datetime"] = pd.to_datetime(Analysis_Data["datetime"], format="%d-%m-%Y %H:%M")
            Analysis_Data["expiry_date"] = pd.to_datetime(Analysis_Data["expiry_date"], format="%d-%m-%Y")

            # Sort by datetime
            Analysis_Data.sort_values(by="datetime", ascending=True, inplace=True)
            Analysis_Data = Analysis_Data[Analysis_Data["datetime"] >= Start_Date]
            Analysis_Data.reset_index(drop=True, inplace=True)

            # Convert back to string format
            Analysis_Data["datetime"] = Analysis_Data["datetime"].dt.strftime('%d-%m-%Y %H:%M')
            Analysis_Data["expiry_date"] = Analysis_Data["expiry_date"].dt.strftime('%d-%m-%Y')
            return Analysis_Data
        else:
            Error_msg_Data = right_Data.get("Error", None)
            Error_msg    = f"ICICI_Historical Combine all dataframes Error {Error_msg_Data}"
            Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
            Error_Strike = f"{strike_price} - {Options_Type}"
            Error_Date   = "All Date"
            Data_Error(Error_msg, Error_Expiry, Error_Strike, Error_Date)                   
            print(f"Fetch_Historical_Data Function Error: No Data")
            return None

    except Exception as e:
        Error_msg    = "Fetch_ICICI_Historical_Data Error"
        Error_Expiry = Expiry_Date.strftime("%d-%m-%Y")
        Error_Strike = f"{strike_price} - {Options_Type}"
        Error_Date   = "All Date"
        Data_Error(Error_msg, Error_Expiry, Error_Strike, Error_Date)                       
        print(f"Fetch_Historical_Data Function Error: {e}")
        return None

# # Example usage
# stock_name = "Nifty"
# stock_code = get_Stock_Name(breeze, "NSE", stock_name)                                      
# exchange_code = "NFO"          # "NFO" "NSE"
# stock_code    = stock_code     # Nifty
# product_type  = "options"      # "options", "futures", "cash"
# right         = "call"       # "others" , "call" , "put"
# strike_price  = 24700              # integer, not string
# interval      = "1minute"      # "1second", "1minute", "5minute", "30minute" , "1day".
# Expiry_Date   = '30-09-2025'   # Valid expiry date supported by Breeze API
# past_day      = 20

# Data = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)
# if Data is not None:
#     print(tabulate(Data.head(10), headers='keys', tablefmt='pretty', showindex=False))
#     print(Data)      
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        Error_msg = "fetch_Merged_Data Error"
        Data_Error(Error_msg, "No", "No", "No")
        print(f"fetch_Merged_Data Function Error: {e}")
        return None
# # Example usage
# Merged_Data = fetch_Merged_Data(Data_call, Data_put)
# print(tabulate(Merged_Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data    Fetch_Historical_Data  Fetch_Historical_Data  Fetch_Historical_Data
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Fetch_Historical_Data(breeze, exchange_code, stock_name, strike_price, interval, Expiry_Date, past_day):
    Data = None   # <-- Default None (fix)
    try:
        if exchange_code == "NFO":
            stock_code = get_Stock_Name(breeze, "NSE", stock_name)
            if stock_code is None:
                stock_code = stock_name
        else:
            stock_code = stock_name

        if str(strike_price) == '0':
            product_type  = "futures"
            right         = "others"
            Data = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)

        elif str(strike_price) != '0':   # <-- elif use kare
            product_type  = "options"
            Data_call = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, "call", strike_price, interval, Expiry_Date, past_day)
            Data_put  = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, "put",  strike_price, interval, Expiry_Date, past_day)

            if Data_call is not None and Data_put is not None:
                Data = fetch_Merged_Data(Data_call, Data_put)
            else:
                Options_Type = "call" if Data_call is None else "put"
                if Data_call is None and Data_put is None:
                    Options_Type = "Call And Put"
                Error_msg = f"Error : {Options_Type} Data None"
                Data_Error(Error_msg, Expiry_Date, strike_price, "No")

        if Data is not None:
            return Data
        else:
            Error_msg = "Error : All Data None"
            Data_Error(Error_msg, Expiry_Date, strike_price, "No")
            return None   # <-- Ensure explicit return
    except Exception as e:
        Error_msg = f"Fetch_Historical_Data Error {e}"
        Data_Error(Error_msg, Expiry_Date, strike_price, "No")
        print(f"Fetch_Historical_Data Function Error: {e}")
        return None

# # Example usage
# exchange_code = "NFO"        # "MCX" , "NFO"
# stock_name    = "Nifty"      # "CRUDE", "NATGAS" "Nifty"
# strike_price  = "24000"      #
# interval      = "1minute"
# Expiry_Date   = '24-04-2025' # '21-04-2025'
# past_day      = 5
# Data = Fetch_Historical_Data ( breeze, exchange_code, stock_name, strike_price, interval, Expiry_Date, past_day)
# print(tabulate(Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
# print(Data)
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  get_strike_list   get_strike_list   get_strike_list   get_strike_list    get_strike_list  get_strike_list  get_strike_list  get_strike_list  get_strike_list  get_strike_list
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_strike_list(breeze, stock_name, expiry_date, past_days, strike_gap,Plus_Minus_strike):
    try:
        # Get stock code from stock name
        stock_code = get_Stock_Name(breeze, "NSE", stock_name)
        if not stock_code:
            print(f"Could not find stock code for {stock_name}")
            return None
        # Fetch historical cash data
        Data = Fetch_ICICI_Historical_Data(breeze, "NSE", stock_code, "cash", "others", 0, "1day", expiry_date, past_days)

        if Data is not None and not Data.empty:
            # Calculate price range
            max_high_round = round((Data["ch_high"].max() + (Plus_Minus_strike*strike_gap)) / strike_gap) * strike_gap
            min_low_round = round((Data["ch_low"].min() - (Plus_Minus_strike*strike_gap)) / strike_gap) * strike_gap
            # Generate strike list
            strike_list = list(range(int(min_low_round), int(max_high_round + strike_gap), strike_gap))
            strike_list = [0] + strike_list  # Add 0 as a placeholder
            return sorted(strike_list)
        else:
            Error_msg    = "get_strike_list Error"
            Data_Error(Error_msg, expiry_date, "No", "No")
            print(f"No historical data found for {stock_name}")
            return None
    except Exception as e:
        Error_msg    = "get_strike_list Error"
        Data_Error(Error_msg, expiry_date, "No", "No")
        print(f"Error generating strike list: {e}")
        return None

# Example usage
# stock_name = "Reliance"
# expiry_date = '30-09-2025'
# past_days = 30
# strike_gap = 10
# Plus_Minus_strike = 20

# strike_list = get_strike_list(breeze, stock_name, expiry_date, past_days, strike_gap, Plus_Minus_strike)
# if strike_list:
#     print(f"Generated {len(strike_list)} strike prices for {stock_name}")
#     print(strike_list)
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  run_with_progress   download_strike     run_with_progress   download_strike     run_with_progress   download_strike      run_with_progress   download_strike    run_with_progress   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed
import os, zipfile
def download_strike(breeze, exchange_code, stock_name, strike_price, interval, Expiry_Date, past_day):
    Data = Fetch_Historical_Data(breeze, exchange_code, stock_name, strike_price, interval, Expiry_Date, past_day)
    if Data is not None:
        os.makedirs(Expiry_Date, exist_ok=True)
        strike_name = strike_price if strike_price != 0 else "futures"
        CSV_Name = os.path.join(Expiry_Date, f"{Expiry_Date}_{strike_name}.csv")
        Data.to_csv(CSV_Name, index=False)
        clear_output(wait=True)
        # print(f"Downloaded: {CSV_Name}")
        return f"{Expiry_Date}_{strike_name}.csv"
    return None

# ✅ Progress Print वाला Function
def run_with_progress(strike_list, breeze, exchange_code, stock_name, interval, Expiry_Date, past_day, progress_speed=1, timeout=0):
    Downlod_File_List = []
    total = len(strike_list)
    completed = 0
    with ThreadPoolExecutor(max_workers=progress_speed) as executor:
        future_to_strike = {executor.submit( download_strike, breeze, exchange_code, stock_name,
                strike_price, interval, Expiry_Date, past_day ): strike_price for strike_price in strike_list }
        for future in as_completed(future_to_strike):
            strike = future_to_strike[future]
            try:
                result = future.result(timeout=timeout)   # ✅ timeout added
                if result:
                    Downlod_File_List.append(result)
                print(f"Progress: {completed+1}/{total} completed ✅ (Strike {strike})")
            except Exception as e:
                print(f"⚠️ Strike {strike} failed: {e}")
            finally:
                completed += 1
    return Downlod_File_List

# # Example usage
# exchange_code = "NFO"
# stock_name = "Reliance"
# interval = "1minute"
# past_day = 40
# Strike_Gep = 10
# Plus_Minus_strike = 20
# Expiry_Date = '30-01-2025'
# strike_list = get_strike_list(breeze, stock_name, Expiry_Date, past_day, Strike_Gep, Plus_Minus_strike)  # strike_list = [1030,1020]
# Downlod_File_List = run_with_progress(strike_list, breeze, exchange_code, stock_name, interval, Expiry_Date, past_day, progress_speed=1, timeout=0)
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  run_with_progress   download_strike     run_with_progress   download_strike     run_with_progress   download_strike      run_with_progress   download_strike    run_with_progress   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os, zipfile
def make_zip(Expiry_Date, base_path="/content", method="best", Downlod_File_List=None):
    try:
        folder_path = os.path.join(base_path, Expiry_Date)
        # अगर file list नहीं दी तो पूरे folder से ले लो
        if not Downlod_File_List:
            if not os.path.exists(folder_path):
                print(f"⚠️ Folder नहीं मिला: {folder_path}")
                return None
            Downlod_File_List = os.listdir(folder_path)
        if not Downlod_File_List:
            print("⚠️ कोई file नहीं मिली, Zip create नहीं होगा")
            return None

        # Compression method select करो
        if method == "fast":
            compression = zipfile.ZIP_DEFLATED   # Fast + अच्छा compression
            compresslevel = 9
        elif method == "best":
            compression = zipfile.ZIP_LZMA       # Best compression (Slow)
            compresslevel = None
        else:
            print(f"⚠️ Unknown method '{method}', defaulting to fast")
            compression = zipfile.ZIP_DEFLATED
            compresslevel = 9
        zip_filename = os.path.join(base_path, f"{Expiry_Date}.zip")
        # compresslevel सिर्फ ZIP_DEFLATED के लिए valid है
        if compresslevel:
            zipf = zipfile.ZipFile(zip_filename, 'w', compression=compression, compresslevel=compresslevel)
        else:
            zipf = zipfile.ZipFile(zip_filename, 'w', compression=compression)
        with zipf:
            for file in Downlod_File_List:
                full_path = os.path.join(folder_path, file)
                if os.path.exists(full_path):
                    zipf.write(full_path, arcname=os.path.basename(file))
                else:
                    print(f"⚠️ File missing: {full_path}")
        print(f"✅ Zip created: {zip_filename}")
        return zip_filename
    except Exception as e:
        print(f"Error creating zip: {e}")
        return None


# Example Run
# Expiry_Date = "09-04-2025"
# zip_file = make_zip(Expiry_Date)
# print(zip_file)
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  run_with_progress   download_strike     run_with_progress   download_strike     run_with_progress   download_strike      run_with_progress   download_strike    run_with_progress   
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import telebot
# Bot को सिर्फ एक बार initialize करें (global)
BOT_TOKEN = '7591009372:AAEkZFnOZ1UyqxQgiTSJVqKqr1uvPP5KqPI'
bot = telebot.TeleBot(BOT_TOKEN)
Tel_Candal_Data_ID  = "-1002257377003"
Tel_JB_Sons_ID      = "-1002263632329"
Tel_Jay_Mataji_ID   = '1170793375'
CHAT_ID = Tel_Jay_Mataji_ID
def Telegram_Message(*args, file_path=None):
    try:
        # अगर text है तो पहले भेजो
        if args:
            message = "\n".join(filter(None, args))
            bot.send_message(CHAT_ID, message)

        # अगर file है तो भेजो
        if file_path:
            with open(file_path, "rb") as f:
                bot.send_document(CHAT_ID, f)

        print("✅ Message/File sent successfully!")

    except Exception as e:
        print("❌ Telegram_Message Error:", e)

# Example
# Telegram_Message("HI Bhai", file_path="/content/JB Sons 5M CE-0 PE-1 QTY0  (1).csv")
#=======================================================================================================================================================================








'''
#_______________________________________________________________________________________________________
!pip install breeze-connect
!pip install telebot
#_______________________________________________________________________________________________________

from importlib import import_module, reload, invalidate_caches
from datetime import datetime, timedelta
from IPython.display import clear_output
from tabulate import tabulate
import pandas as pd
import threading
import requests
import zipfile
import sys
import os

def Import_File(import_name):
    try:
        path = f"/content/importFile/{import_name}.py"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        url = f"https://raw.githubusercontent.com/Kaklotar9985/KaklotarMitul/main/{import_name}.py"
        response = requests.get(url)
        response.raise_for_status()
        with open(path, "wb") as file:
            file.write(response.content)
        module_dir = os.path.dirname(path)
        if module_dir not in sys.path:
            sys.path.append(module_dir)
        invalidate_caches()  # importlib कैश साफ़ करें
        if import_name in sys.modules:
            del sys.modules[import_name]
        imported_module = import_module(import_name)
        reload(imported_module)
        print(f"✅ Imported & Reloaded: {import_name}")
        print("📦 Available Attributes:", dir(imported_module))
        return imported_module
    except Exception as e:
        print(f"Import_File Function Error: {e}")
        return None

# यूज़ उदाहरण:
ICICI = Import_File("ICICIHistorical_V2")

import urllib
APIKEY    = "69162e_0=09u812m845534f1UYw8p27T"
SecretKey = "C98)12W9xS`13y1871&031PQ83+m8c40"
TOTP      = "GJ2EW5K2N5UGKY3BINBFQ42KJE"
UserID    = "7817857533"
Password  = "9904953138mk"
print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus(APIKEY))
#__________________________________________________________________________________________________
from breeze_connect import BreezeConnect
import logging
session_token = "53150902"
breeze = BreezeConnect(api_key=APIKEY)
breeze.generate_session(api_secret=SecretKey, session_token=session_token)
# Disable Breeze API debug logs
logging.getLogger("APILogger").setLevel(logging.CRITICAL)

#_______________________________________________________________________________________________________
exchange_code = "NFO"
stock_name = "Nifty"
interval = "1minute"
past_day = 60
Strike_Gep = 50
Plus_Minus_strike = 20
progress_speed = 3

# Expiry_Date = '29-02-2024'
Expiry_Date_List = ['09-04-2025', '17-04-2025', '24-04-2025', '30-04-2025', '08-05-2025', '15-05-2025', '22-05-2025', '29-05-2025', '05-06-2025', '12-06-2025', '19-06-2025', '26-06-2025', '03-07-2025', '10-07-2025', '17-07-2025', '24-07-2025','31-07-2025', '07-08-2025', '14-08-2025', '21-08-2025', '28-08-2025', ]

for Expiry_Date in Expiry_Date_List:
    strike_list = ICICI.get_strike_list(breeze, stock_name, Expiry_Date, past_day, Strike_Gep, Plus_Minus_strike) # strike_list = [1030,1020]
    Downlod_File_List = ICICI.run_with_progress(strike_list, breeze, exchange_code, stock_name, interval, Expiry_Date, past_day, progress_speed)

    Excel_Name = os.path.join(Expiry_Date, Expiry_Date)
    filename = ICICI.Error_Data_to_Excel(Excel_Name)
    if filename:
      Downlod_File_List.append(filename)

    zip_file = ICICI.make_zip(Downlod_File_List, Expiry_Date)
    if zip_file:
        threading.Thread(target=Telegram_Message,args=(zip_file,),kwargs={"file_path": zip_file}, daemon=True ).start()
        from google.colab import files
        files.download(zip_file)
#_______________________________________________________________________________________________________

'''
