from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timedelta
from IPython.display import clear_output
import pandas as pd
import time
# Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi  
def get_Heikin_Ashi(prev_ha_open, prev_ha_close, current_open, current_high, current_low, current_close):
    try:
        def custom_round(num, decimals):
            return Decimal(str(num)).quantize(Decimal(f'1.{"0" * decimals}'), rounding=ROUND_HALF_UP)
        ha_close = custom_round((Decimal(current_open) + Decimal(current_high)  + Decimal(current_low)  + Decimal(current_close) ) / 4, 5)
        ha_open  = custom_round((Decimal(prev_ha_open) + Decimal(prev_ha_close)) / 2, 5)
        ha_high  = custom_round(max(Decimal(current_high), ha_open, ha_close), 5)
        ha_low   = custom_round(min(Decimal(current_low), ha_open, ha_close), 5)
        ha_color = "black" if ha_open == ha_close else "green" if ha_open < ha_close else "red"
        Heikin_Ashi = {"ha_open"  : float(ha_open),  "ha_high"  : float(ha_high), "ha_low"   : float(ha_low),
                       "ha_close" : float(ha_close), "ha_color" : ha_color }
        return Heikin_Ashi
    except Exception as e:
        print(f"Heikin_Ashi Function Error : {e}")
        return None

# Example usage:
# prev_ha_open  = 331.19
# prev_ha_close = 330.80
# current_open  = 331.50
# current_high  = 336.30
# current_low   = 331.40
# current_close = 332.60
# Heikin_Ashi = get_Heikin_Ashi(prev_ha_open, prev_ha_close, current_open, current_high, current_low, current_close)
# print(Heikin_Ashi)
# output = {'ha_open': 331.0, 'ha_high': 336.3, 'ha_low': 331.0, 'ha_close': 332.95, 'ha_color': 'green'}
#_______________________________________________________________________________________________________________________________
# Candle_time  Candle_time   Candle_time   Candle_time   Candle_time   Candle_time   Candle_time   Candle_time   Candle_time   Candle_time   
def get_Candle_time(date_str, round_to=5):
    try:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except:
            dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")

        base_time = dt.replace(minute=0, second=0, microsecond=0)
        total_seconds = (dt - base_time).total_seconds()
        round_seconds = round_to * 60
        rounded_seconds = (total_seconds // round_seconds) * round_seconds
        new_dt = base_time + timedelta(seconds=rounded_seconds)
        current_open_Time  = new_dt.strftime("%d-%m-%Y %H:%M")
        current_Round_cloce_Time = new_dt + timedelta( minutes = round_to - 1)
        current_Close_Time = dt.strftime("%d-%m-%Y %H:%M")
        prev_open_dt       = new_dt - timedelta(minutes=round_to)
        prev_close_dt      = prev_open_dt + timedelta(minutes=round_to - 1)
        prev_open_Time     = prev_open_dt.strftime("%d-%m-%Y %H:%M")
        prev_Close_Time    = prev_close_dt.strftime("%d-%m-%Y %H:%M")

        Data ={"current_Candle" : {"open_time" : current_open_Time, "close_time" : current_Close_Time },
               "prev_Candle"    : {"open_time" : prev_open_Time,    "close_time" : prev_Close_Time }, 
               "current_Round_cloce_Time" : current_Round_cloce_Time.strftime("%d-%m-%Y %H:%M") }
        return Data 
    except Exception as e:
        print(f"Candle_time Function Error : {e}")
        return None
# Example usage
# DateTime = "01-04-2025 09:28"
# Round_Minute = 10
# Data = get_Candle_time(DateTime, Round_Minute)
# print(Data)
#_______________________________________________________________________________________________________________________________

# Candle_Price   Candle_Price   Candle_Price   Candle_Price   Candle_Price   Candle_Price   Candle_Price   Candle_Price  
def get_Candle_Price(DATA, DateTime, Round_Minute, Candle_Name = None):
    if Candle_Name is None:
        Candle_Name = { "datetime": "datetime", "open": "open", "high": "high", "low": "low", "close": "close" , "datetime_format" : "%Y-%m-%d %H:%M:%S",}
    datetime_name   = Candle_Name.get("datetime").lower()
    open_name       = Candle_Name.get("open").lower()
    high_name       = Candle_Name.get("high").lower()
    low_name        = Candle_Name.get("low").lower()
    close_name      = Candle_Name.get("close").lower()
    datetime_format = Candle_Name.get("datetime_format")
    try:
      DATA = pd.DataFrame(DATA)
      DATA.columns = [col.lower() for col in DATA.columns]
      DATA[datetime_name] = pd.to_datetime(DATA[datetime_name], format = datetime_format)
      
      Candle_time_Data   = get_Candle_time(DateTime, Round_Minute)
      current_open_Time  = pd.to_datetime(Candle_time_Data["current_Candle"]["open_time"], format="%d-%m-%Y %H:%M")
      current_close_Time = pd.to_datetime(Candle_time_Data["current_Candle"]["close_time"], format="%d-%m-%Y %H:%M")
      prev_open_Time     = pd.to_datetime(Candle_time_Data["prev_Candle"]["open_time"], format="%d-%m-%Y %H:%M")
      prev_close_Time    = pd.to_datetime(Candle_time_Data["prev_Candle"]["close_time"], format="%d-%m-%Y %H:%M")
      
      current_data = DATA[(DATA[datetime_name] >= current_open_Time) & (DATA[datetime_name] <= current_close_Time)].copy()
      current_data.reset_index(drop=True, inplace=True)
      if len(current_data) != 0:
        current_Data = {"open" : float(current_data[open_name].iloc[0]), "high" : float(current_data[high_name].max()),
                        "low" : float(current_data[low_name].min()), "close" : float(current_data[close_name].iloc[-1])}
      else:
        current_Data = {"open" : None, "high" : None, "low" : None, "close" : None}
      prev_data = DATA[(DATA[datetime_name] >= prev_open_Time) & (DATA[datetime_name] <= prev_close_Time)].copy()
      prev_data.reset_index(drop=True, inplace=True)
      if len(prev_data) != 0:
        prev_Data  = {"open" : float(prev_data[open_name].iloc[0]), "high" : float(prev_data[high_name].max()),
                      "low" : float(prev_data[low_name].min()), "close" : float(prev_data[close_name].iloc[-1])}
      else:
        prev_Data  = {"open" : None, "high" : None, "low" : None, "close" : None}
      return {"current_Data" : current_Data, "prev_Data" : prev_Data }
    
    except Exception as e:
      print(f"Candle_Price Function Error : {e}")
      return {"current_Data" : None, "prev_Data" : None }

# Example usage
# DATA = Data.copy()
# DateTime = "01-04-2025 09:05"
# Round_Minute = 5
# Candle_Name = {"datetime" : "Time", "open" : "Open", "high" : "High", "low" : "Low", "close" : "Close", "datetime_format" : "%Y-%m-%d %H:%M:%S",}
# Candle_Price_Data = get_Candle_Price(DATA, DateTime, Round_Minute, Candle_Name)
# current_Data = Candle_Price_Data["current_Data"]  # 2025-01-28 22:12:00
# prev_Data = Candle_Price_Data["prev_Data"]
# print(current_Data)
# print(prev_Data)
#________________________________________________________________________________________________________________________

# get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns   
def get_HeikinAshi_Columns(DATA, Round_Minute, Candle_Name = None):
    try:
        if Candle_Name is None:
           Candle_Name = { "datetime": "datetime", "open": "open", "high": "high", "low": "low", "close": "close" , "datetime_format" : "%Y-%m-%d %H:%M:%S",}
        datetime_name   = Candle_Name.get("datetime").lower()
        open_name       = Candle_Name.get("open").lower()
        high_name       = Candle_Name.get("high").lower()
        low_name        = Candle_Name.get("low").lower()
        close_name      = Candle_Name.get("close").lower()
        datetime_format = Candle_Name.get("datetime_format")
       
        ha_open_list = []
        ha_high_list = []
        ha_low_list = []
        ha_close_list = []
        ha_color_list = []
        prev_ha_open = None
        prev_ha_close = None

        DATA.columns = [col.lower() for col in DATA.columns]
        for i in range(len(DATA)):
            DateTime = pd.to_datetime(DATA[datetime_name].iloc[i], format = datetime_format).strftime("%d-%m-%Y %H:%M")
            Candle_Price_Data = get_Candle_Price(DATA, DateTime, Round_Minute,Candle_Name)
            try:
                if prev_ha_open is None or prev_ha_close is None:
                   prev_ha_open   = Candle_Price_Data["prev_Data"]["open"]
                   prev_ha_close  = Candle_Price_Data["prev_Data"]["close"]
                current_open  = Candle_Price_Data["current_Data"]["open"]
                current_high  = Candle_Price_Data["current_Data"]["high"]
                current_low   = Candle_Price_Data["current_Data"]["low"]
                current_close = Candle_Price_Data["current_Data"]["close"]

                # Compute Heikin Ashi candle
                Heikin_Ashi = get_Heikin_Ashi(prev_ha_open, prev_ha_close, current_open, current_high, current_low, current_close)
                if Heikin_Ashi is not None:
                   # Update prev HA values only at round-close time
                   Round_time = pd.to_datetime(get_Candle_time(DateTime, Round_Minute)["current_Round_cloce_Time"], format="%d-%m-%Y %H:%M")
                   if DateTime == Round_time.strftime("%d-%m-%Y %H:%M"):
                      prev_ha_open  = Heikin_Ashi.get("ha_open")
                      prev_ha_close = Heikin_Ashi.get("ha_close")

                   ha_open_list .append(Heikin_Ashi.get("ha_open"))
                   ha_high_list .append(Heikin_Ashi.get("ha_high"))
                   ha_low_list  .append(Heikin_Ashi.get("ha_low"))
                   ha_close_list.append(Heikin_Ashi.get("ha_close"))
                   ha_color_list.append(Heikin_Ashi.get("ha_color"))
                else:
                   ha_open_list .append(None)
                   ha_high_list .append(None)
                   ha_low_list  .append(None)
                   ha_close_list.append(None)
                   ha_color_list.append(None)

            except Exception as e:
                print(f"Heikin_Ashi Function Error : {e}")
                ha_open_list .append(None)
                ha_high_list .append(None)
                ha_low_list  .append(None)
                ha_close_list.append(None)
                ha_color_list.append(None)
            clear_output(wait=True)
            print(f"HeikinAshi_{Round_Minute} Process DateTime : " + DateTime)
        # Add Heikin-Ashi columns to the DataFrame
        DATA[f"ha_{Round_Minute}_open"]  = ha_open_list
        DATA[f"ha_{Round_Minute}_high"]  = ha_high_list
        DATA[f"ha_{Round_Minute}_low"]   = ha_low_list
        DATA[f"ha_{Round_Minute}_close"] = ha_close_list
        DATA[f"ha_{Round_Minute}_color"] = ha_color_list
        return DATA
    except Exception as e:
        print(f"get_HeikinAshi_Columns Function Error : {e}")
        return None

# Example usage 'time'
# DATA = Filtered_Data.copy()
# Round_Minute = 5
# Candle_Name = {"datetime" : "Time_IST", "open" : "Open", "high" : "High", "low" : "Low", "close" : "Close", "datetime_format" : "%Y-%m-%d %H:%M",}
# Datas = get_HeikinAshi_Columns(DATA, Round_Minute, Candle_Name)
# print(tabulate(Datas, headers="keys", tablefmt="pretty", showindex=False))
#____________________________________________________________________________________________________________________________________________________________

# get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price   get_ORB_Price  
def get_ORB_Price(DATA, From_DateTime, To_DateTime, Candle_Name = None):
    if Candle_Name is None:
        Candle_Name = { "datetime": "datetime", "open": "open", "high": "high", "low": "low", "close": "close" , "datetime_format" : "%Y-%m-%d %H:%M:%S",}
    datetime_name   = Candle_Name.get("datetime").lower()
    open_name       = Candle_Name.get("open").lower()
    high_name       = Candle_Name.get("high").lower()
    low_name        = Candle_Name.get("low").lower()
    close_name      = Candle_Name.get("close").lower()
    datetime_format = Candle_Name.get("datetime_format")

    DATA = pd.DataFrame(DATA)
    DATA.columns = [col.lower() for col in DATA.columns]
    DATA[datetime_name] = pd.to_datetime(DATA[datetime_name], format = datetime_format)
    
    current_open_Time  = pd.to_datetime(From_DateTime, format="%d-%m-%Y %H:%M")
    current_close_Time = pd.to_datetime(To_DateTime,   format="%d-%m-%Y %H:%M")
    current_data = DATA[(DATA[datetime_name] >= current_open_Time) & (DATA[datetime_name] <= current_close_Time)].copy()
    current_data.reset_index(drop=True, inplace=True)
    if len(current_data) != 0:
      current_Data = {"open" : float(current_data[open_name].iloc[0]), "high" : float(current_data[high_name].max()),
                      "low" : float(current_data[low_name].min()), "close" : float(current_data[close_name].iloc[-1])}
    else:
      current_Data = {"open" : None, "high" : None, "low" : None, "close" : None}
    return current_Data 

# Example usage
# DATA = Data.copy()
# From_DateTime = "30-04-2025 09:00"
# To_DateTime   = "30-04-2025 09:15"
# Round_Minute = 5
# Candle_Name = {"datetime" : "datetime", "open" : "fx_open", "high" : "fx_high", "low" : "fx_low", "close" : "fx_close", "datetime_format" : "%d-%m-%Y %H:%M",}
# current_Data = get_ORB_Price(DATA, From_DateTime, To_DateTime, Candle_Name)
# print(current_Data)
#____________________________________________________________________________________________________________________________________________________________
