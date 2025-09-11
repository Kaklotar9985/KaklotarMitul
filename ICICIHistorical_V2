from dateutil import parser
from IPython.display import clear_output
import logging

# Disable Breeze API debug logs
logging.getLogger("APILogger").setLevel(logging.CRITICAL)

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
import pandas as pd
from datetime import datetime, timedelta
from dateutil import parser
from IPython.display import clear_output
from tabulate import tabulate

def Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day):
    try:
        fetch_Futures_Data_Error = {}
        Datas_List = []

        # Parse Expiry_Date
        Expiry_Date = datetime.strptime(Expiry_Date, "%d-%m-%Y")
        ToDate = datetime.today()
        end_date = min(Expiry_Date, ToDate)  + timedelta(days=1)
        Start_Date = end_date - timedelta(days=past_day)
        
        if product_type in ("futures", "cash"):
            # Format dates for API
            expiry_date_api = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            from_date_api = Start_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date_api = end_date.strftime("%Y-%m-%dT00:00:00.000Z")
            
            right_Data = breeze.get_historical_data_v2( interval=interval, from_date=from_date_api, to_date=to_date_api, stock_code=stock_code,
                exchange_code=exchange_code, product_type=product_type,  expiry_date=expiry_date_api, right=right, strike_price=strike_price )
            
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
                Datas_List.append(Data)
            else:
                if Expiry_Date not in fetch_Futures_Data_Error:
                    fetch_Futures_Data_Error[Expiry_Date] = []
                fetch_Futures_Data_Error[Expiry_Date].append(str(Start_Date))

        elif product_type == "options":
            # For options, always use day-by-day fetching
            date_list = [(Start_Date + timedelta(days=i)).strftime("%d-%m-%Y") 
                        for i in range((end_date - Start_Date).days + 1)]
            
            expiry_date_api = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")
            
            for i, Dates in enumerate(date_list):
                Date = datetime.strptime(Dates, "%d-%m-%Y")
                start_date_time = datetime.strptime((Date.strftime("%d-%m-%Y 09:15")), "%d-%m-%Y %H:%M")
                end_date_time = datetime.strptime(((Date + timedelta(days=1)).strftime("%d-%m-%Y 09:14")), "%d-%m-%Y %H:%M")
                from_date = start_date_time.strftime("%Y-%m-%dT00:00:00.000Z")
                to_date = end_date_time.strftime("%Y-%m-%dT00:00:00.000Z")

                right_Data = breeze.get_historical_data_v2(interval=interval, from_date=from_date, to_date=to_date, stock_code=stock_code,
                    exchange_code=exchange_code, product_type=product_type,  expiry_date=expiry_date_api, right=right, strike_price=strike_price )
                
                clear_output(wait=True)
                print(f"Fetching options data: {i+1}/{len(date_list)} - Date: {Dates}", 
                      f"Strike: {strike_price}", f"Right: {right}")
                
                if right_Data["Error"] is None and right_Data["Success"]:
                    Options_Type = right
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
                        Datas_List.append(Data)
                else:
                    if Expiry_Date not in fetch_Futures_Data_Error:
                        fetch_Futures_Data_Error[Expiry_Date] = []
                    fetch_Futures_Data_Error[Expiry_Date].append(str(start_date_time))
                    
                # Add a small delay to avoid hitting API rate limits
                import time
                time.sleep(0.5)

        # Combine all dataframes
        if Datas_List:
            Analysis_Data = pd.concat(Datas_List)
            
            # Convert to datetime for proper sorting
            Analysis_Data["datetime"] = pd.to_datetime(Analysis_Data["datetime"], format="%d-%m-%Y %H:%M")
            Analysis_Data["expiry_date"] = pd.to_datetime(Analysis_Data["expiry_date"], format="%d-%m-%Y")
            
            # Sort by datetime
            Analysis_Data.sort_values(by="datetime", ascending=True, inplace=True)
            Analysis_Data.reset_index(drop=True, inplace=True)
            
            # Convert back to string format
            Analysis_Data["datetime"] = Analysis_Data["datetime"].dt.strftime('%d-%m-%Y %H:%M')
            Analysis_Data["expiry_date"] = Analysis_Data["expiry_date"].dt.strftime('%d-%m-%Y')
            
            clear_output(wait=True)
            return Analysis_Data
        else:
            print("No data fetched. Check parameters or API connection.")
            if fetch_Futures_Data_Error:
                print("Errors encountered:", fetch_Futures_Data_Error)
            return None
            
    except Exception as e:
        print(f"Fetch_Historical_Data Function Error: {e}")
        import traceback
        traceback.print_exc()
        return None

# # Example usage
# stock_name = "Reliance"
# stock_code = get_Stock_Name(breeze, "NSE", stock_name)
# exchange_code = "NSE"          # "NFO" "NSE"
# stock_code    = stock_code     # Nifty
# product_type  = "futures"      # "options", "futures", "cash"
# right         = "others"       # "others" , "call" , "put"
# strike_price  = 0              # integer, not string
# interval      = "1minute"      # "1second", "1minute", "5minute", "30minute" , "1day".
# Expiry_Date   = '30-09-2025'   # Valid expiry date supported by Breeze API
# past_day      = 5

# Data = Fetch_ICICI_Historical_Data(breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)
# if Data is not None:
#     print(tabulate(Data.head(10), headers='keys', tablefmt='pretty', showindex=False))
#     print(Data)
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fetch_Merged_Data(DATA1, DATA2):
    try :
        try: DATA1 = pd.concat(DATA1, ignore_index=True)
        except: pass
        try: DATA2 = pd.concat(DATA2, ignore_index=True)
        except: pass
        Merged_Data = pd.merge(DATA1, DATA2,
                              on=["datetime", "stock_code", "expiry_date", "strike_price"],
                              how="outer", suffixes=("_call", "_put"))
        Merged_Data["datetime"] = pd.to_datetime(Merged_Data["datetime"], format="%d-%m-%Y %H:%M")
        Merged_Data = Merged_Data.sort_values(by="datetime", ascending=True).reset_index(drop=True)
        Merged_Data['datetime'] = Merged_Data['datetime'].dt.strftime('%d-%m-%Y %H:%M')
        return Merged_Data
    except Exception as e:
        print(f"fetch_Merged_Data Function Error: {e}")
        return None
# # Example usage
# Merged_Data = fetch_Merged_Data(Data_call, Data_put)
# print(tabulate(Merged_Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
#=======================================================================================================================================================================

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data    Fetch_Historical_Data  Fetch_Historical_Data  Fetch_Historical_Data
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Fetch_Historical_Data ( breeze, exchange_code, stock_name, strike_price, interval, Expiry_Date, past_day):
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
          Data = Fetch_ICICI_Historical_Data ( breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)
        if str(strike_price) != '0':
          product_type  = "options"
          Data_call = Fetch_ICICI_Historical_Data ( breeze, exchange_code, stock_code, product_type, "call", strike_price, interval, Expiry_Date, past_day)
          Data_put  = Fetch_ICICI_Historical_Data ( breeze, exchange_code, stock_code, product_type, "put",  strike_price, interval, Expiry_Date, past_day)
          if Data_call is not None and Data_put is not None:
              Data = fetch_Merged_Data(Data_call, Data_put)
        return Data
    except Exception as e:
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
            print(f"No historical data found for {stock_name}")
            return None
    except Exception as e:
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
