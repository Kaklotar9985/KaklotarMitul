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
ICICI = Import_File("ICICIHistorical_V4")

banknifty_monthly_expiry = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '27-03-2024', '24-04-2024', '29-05-2024', '26-06-2024', '31-07-2024', '28-08-2024', '25-09-2024', '30-10-2024', '27-11-2024', '24-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025', '29-05-2025', '26-06-2025', '31-07-2025', '28-08-2025', '30-09-2025', '28-10-2025', '25-11-2025', '30-12-2025',]

nifty_monthly_expiry     = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '28-03-2024', '25-04-2024', '30-05-2024', '27-06-2024', '25-07-2024', '29-08-2024', '26-09-2024', '31-10-2024', '28-11-2024', '26-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025', '29-05-2025', '26-06-2025', '31-07-2025', '28-08-2025', '30-09-2025', '28-10-2025', '25-11-2025', '30-12-2025' ]

nifty_weekly_expiry      = ['07-01-2021', '14-01-2021', '21-01-2021', '28-01-2021', '04-02-2021', '11-02-2021', '18-02-2021', '25-02-2021', '04-03-2021', '10-03-2021', '18-03-2021', '25-03-2021', '01-04-2021', '08-04-2021', '15-04-2021', '22-04-2021', '29-04-2021', '06-05-2021', '12-05-2021', '20-05-2021', '27-05-2021', '03-06-2021', '10-06-2021', '17-06-2021', '24-06-2021', '01-07-2021', '08-07-2021', '15-07-2021', '22-07-2021', '29-07-2021', '05-08-2021', '12-08-2021', '18-08-2021', '26-08-2021', '02-09-2021', '09-09-2021', '16-09-2021', '23-09-2021', '30-09-2021', '07-10-2021', '14-10-2021', '21-10-2021', '28-10-2021', '03-11-2021', '11-11-2021', '18-11-2021', '25-11-2021', '02-12-2021', '09-12-2021', '16-12-2021', '23-12-2021', '30-12-2021',
                            '06-01-2022', '13-01-2022', '20-01-2022', '27-01-2022', '03-02-2022', '10-02-2022', '17-02-2022', '24-02-2022', '03-03-2022', '10-03-2022', '17-03-2022', '24-03-2022', '31-03-2022', '07-04-2022', '13-04-2022', '21-04-2022', '28-04-2022', '05-05-2022', '12-05-2022', '19-05-2022', '26-05-2022', '02-06-2022', '09-06-2022', '16-06-2022', '23-06-2022', '30-06-2022', '07-07-2022', '14-07-2022', '21-07-2022', '28-07-2022', '04-08-2022', '11-08-2022', '18-08-2022', '25-08-2022', '01-09-2022', '08-09-2022', '15-09-2022', '22-09-2022', '29-09-2022', '06-10-2022', '13-10-2022', '20-10-2022', '27-10-2022', '03-11-2022', '10-11-2022', '17-11-2022', '24-11-2022', '01-12-2022', '08-12-2022', '15-12-2022', '22-12-2022', '29-12-2022',
                            '05-01-2023', '12-01-2023', '19-01-2023', '25-01-2023', '02-02-2023', '09-02-2023', '16-02-2023', '23-02-2023', '02-03-2023', '09-03-2023', '16-03-2023', '23-03-2023', '29-03-2023', '06-04-2023', '13-04-2023', '20-04-2023', '27-04-2023', '04-05-2023', '11-05-2023', '18-05-2023', '25-05-2023', '01-06-2023', '08-06-2023', '15-06-2023', '22-06-2023', '28-06-2023', '06-07-2023', '13-07-2023', '20-07-2023', '27-07-2023', '03-08-2023', '10-08-2023', '17-08-2023', '24-08-2023', '31-08-2023', '07-09-2023', '14-09-2023', '21-09-2023', '28-09-2023', '05-10-2023', '12-10-2023', '19-10-2023', '26-10-2023', '02-11-2023', '09-11-2023', '16-11-2023', '23-11-2023', '30-11-2023', '07-12-2023', '14-12-2023', '21-12-2023', '28-12-2023',
                            '04-01-2024', '11-01-2024', '18-01-2024', '25-01-2024', '01-02-2024', '08-02-2024', '15-02-2024', '22-02-2024', '29-02-2024', '07-03-2024', '14-03-2024', '21-03-2024', '28-03-2024', '04-04-2024', '10-04-2024', '18-04-2024', '25-04-2024', '02-05-2024', '09-05-2024', '16-05-2024', '23-05-2024', '30-05-2024', '06-06-2024', '13-06-2024', '20-06-2024', '27-06-2024', '04-07-2024', '11-07-2024', '18-07-2024', '25-07-2024', '01-08-2024', '08-08-2024', '14-08-2024', '22-08-2024', '29-08-2024', '05-09-2024', '12-09-2024', '19-09-2024', '26-09-2024', '03-10-2024', '10-10-2024', '17-10-2024', '24-10-2024', '31-10-2024', '07-11-2024', '14-11-2024', '21-11-2024', '28-11-2024', '05-12-2024', '12-12-2024', '19-12-2024', '26-12-2024',
                            '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025', '09-04-2025', '17-04-2025', '24-04-2025', '30-04-2025', '08-05-2025', '15-05-2025', '22-05-2025', '29-05-2025', '05-06-2025', '12-06-2025', '19-06-2025', '26-06-2025', '03-07-2025', '10-07-2025', '17-07-2025', '24-07-2025', '31-07-2025', '07-08-2025', '14-08-2025', '21-08-2025', '28-08-2025', '02-09-2025', '09-09-2025', '16-09-2025', '23-09-2025', '30-09-2025', '07-10-2025', '14-10-2025', '20-10-2025', '25-10-2025', '04-11-2025', '11-11-2025', '18-11-2025', '25-11-2025', '30-12-2025',  ]

Strike_Gep_List          = {"nifty" : 50, "nifty bank" : 100, "reliance" :10}

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Pandas_Date_Formet   Pandas_Date_Formet     Pandas_Date_Formet  Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet     Pandas_Date_Formet      Pandas_Date_Formet   Pandas_Date_Formet
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
def Pandas_Date_Formet(Date): # 🔹 Flexible Date Parsing Function
    Formet_List = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S"]
    for Date_Formet in Formet_List:
        try:
            return datetime.strptime(Date, Date_Formet)
        except ValueError:
            continue
    return Date  # अगर कोई फॉर्मेट match न हो तो string 그대로 return
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry   get_Expiry    get_Expiry   get_Expiry
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import calendar
import pandas as pd
def get_Symbol_Expiry(Dates, Symbol, Expiry_Period, Expiry_Type, Start_Date=None, End_Date=None):
    global banknifty_monthly_expiry, nifty_monthly_expiry, nifty_weekly_expiry, naturalgas_futures_monthly_expiry
    try:
        # 🔹 Select correct expiry list first (har condition me needed hai)
        if Expiry_Period.lower() == "weekiy" and Symbol.lower() == "nifty":
            Expiry_List = nifty_weekly_expiry
        elif Expiry_Period.lower() == "monthly":
            if Symbol.lower() in ["nifty", "reliance"]:             # if stock_name in ["nifty", "nifty bank"]:
                Expiry_List = nifty_monthly_expiry
            elif Symbol.lower() == "nifty bank":
                Expiry_List = banknifty_monthly_expiry
            elif Symbol.lower() == "naturalgas":
                Expiry_List = naturalgas_futures_monthly_expiry
            else:
                raise ValueError(f"Unknown symbol for monthly expiry: {Symbol}")
        else:
            raise ValueError(f"Unknown Expiry_Period: {Expiry_Period}")
        Expiry_List = pd.to_datetime(pd.Series(Expiry_List), format="%d-%m-%Y")
        # 🔹 CASE 1: Single date expiry calculation (Current / Next)
        if Dates is not None:
            Date = Pandas_Date_Formet(Dates)
            filtered = Expiry_List[Expiry_List >= Date].dt.strftime("%d-%m-%Y").tolist()
            if not filtered:
                return None

            if Expiry_Type.lower() == "current":
                return filtered[0]
            elif Expiry_Type.lower() == "next":
                return filtered[1] if len(filtered) > 1 else None
            else:
                raise ValueError(f"Unknown Expiry_Type: {Expiry_Type}")
        # 🔹 CASE 2: Date range expiry list calculation
        elif Start_Date is not None and End_Date is not None:
            Start_Date = Pandas_Date_Formet(Start_Date).replace(day=1, hour=0, minute=0, second=0, microsecond=0)

            End_Date = Pandas_Date_Formet(End_Date)
            last_day = calendar.monthrange(End_Date.year, End_Date.month)[1]
            End_Date = End_Date.replace(day=last_day, hour=23, minute=59, second=59, microsecond=0)

            filtered = Expiry_List[(Expiry_List >= Start_Date) & (Expiry_List <= End_Date)]
            return filtered.dt.strftime("%d-%m-%Y").tolist()
        return None
    except Exception as e:
        print(f"get_Expiry Function Error: {e}")
        return None

# # Example usage
# Dates          = None #"05-10-2025"
# Symbol         = "nifty bank" # nifty  "nifty bank"
# Expiry_Period  = "Monthly"  # "Weekiy" , "Monthly"
# Expiry_Type    = "Current"  # "Current", "Next"
# Start_Date = "01-06-2025"
# End_Date   = "15-09-2025"
# Expirys        = get_Symbol_Expiry(Dates, Symbol, Expiry_Period, Expiry_Type, Start_Date, End_Date)
# print(Expirys)
#=========================================================================================================================================================================================================================================================================================

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep   get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Strike_Gep(Symbol):
    global Strike_Gep_List
    try:
       return Strike_Gep_List[Symbol.lower()]
    except Exception as e:
       print(f"get_Strike_Gep Function Error: {e}")
       return None
# # Example usage
# Symbol = "nifty"  #  nifty , banknifty
# Strike_Gep = get_Strike_Gep(Symbol)
# print(Strike_Gep)
#_____________________________________________________________________________________________________________________________________________________
from datetime import datetime, time, timedelta
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data   get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data  get_Cash_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Cash_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for"):
    Expiry_Date  = End_Date
    Options_Type = "ch"
    strike_price = 0
    Cash_Data = ICICI.Read_Strike_Data(breeze, stock_name, Expiry_Date, Options_Type,strike_price, Start_Date, End_Date, interval, Loop_Type)
    Cash_Data["datetime"] = pd.to_datetime(Cash_Data["datetime"], format="%d-%m-%Y %H:%M", errors="coerce")
    Cash_Data = Cash_Data[Cash_Data["datetime"].dt.time.between(time(9, 15), time(15, 30))]
    Cash_Data = Cash_Data.sort_values(by="datetime").reset_index(drop=True)
    Cash_Data["datetime"] = Cash_Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    if stock_name in ["nifty", "nifty bank"]:
      if "ch_volume" in Cash_Data.columns:
          Cash_Data.drop(columns=["ch_volume"], inplace=True)   
    return Cash_Data
# # Example usage
# stock_name = "Nifty Bank"
# Start_Date = "01-07-2025"
# End_Date   = "16-10-2025"
# interval="1minute"
# Ch_data = get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval)
# print(tabulate(pd.concat([Ch_data.head(3), Ch_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data   get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data  get_Futures_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for"):
    expiry_list = get_Symbol_Expiry(None, stock_name, "Monthly", "Current", Start_Date, End_Date)
    date_ranges = []
    for i, expiry in enumerate(expiry_list):
        expiry_date = datetime.strptime(expiry, "%d-%m-%Y")
        if i == 0:
            start_date = datetime.strptime(Start_Date, "%d-%m-%Y")
        else:
            start_date = datetime.strptime(expiry_list[i-1], "%d-%m-%Y") + timedelta(days=1)
        if i < len(expiry_list)-1:
            end_date = datetime.strptime(expiry_list[i+1], "%d-%m-%Y")
        else:
            end_date = datetime.strptime(End_Date, "%d-%m-%Y")
        if end_date > expiry_date:
            end_date = expiry_date
        date_ranges.append((start_date, end_date, expiry_date.strftime("%d-%m-%Y")))

    Options_Type = "fu"
    strike_price = 0
    all_data = []
    def fetch_data(start, end, expiry):
        return ICICI.Read_Strike_Data(breeze, stock_name, expiry, Options_Type, strike_price,start.strftime("%d-%m-%Y"), end.strftime("%d-%m-%Y"), interval, Loop_Type)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_data, start, end, expiry) for (start, end, expiry) in date_ranges]
        for f in as_completed(futures):
            try:
                all_data.append(f.result())
            except Exception as e:
                print("⚠️ Error:", e)

    if not all_data:
        print("❌ कोई डेटा नहीं मिला")
        return pd.DataFrame()

    Futures_Data             = pd.concat(all_data, ignore_index=True)
    Futures_Data             = Futures_Data.drop_duplicates(subset=["datetime", "expiry_date"], keep="last")
    Futures_Data["datetime"] = pd.to_datetime(Futures_Data["datetime"], format="%d-%m-%Y %H:%M", errors='coerce')
    Futures_Data             = Futures_Data.sort_values(by="datetime").reset_index(drop=True)
    Futures_Data["datetime"] = Futures_Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    # Futures_Data.rename(columns={"expiry_date": "m_c_expiry"}, inplace=True)
    return Futures_Data
# # Example usage
# stock_name = "Nifty Bank"
# Start_Date = "01-07-2025"
# End_Date   = "16-10-2025"
# interval="1minute"
# Fu_data = get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval)
# print(tabulate(pd.concat([Fu_data.head(3), Fu_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data   Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data  Ch_Fu_merge_data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Ch_Fu_merge_data(Ch_data, Fu_data):
    Ch_data["datetime"] = pd.to_datetime(Ch_data["datetime"], format="%d-%m-%Y %H:%M") # 🔹 Step 1: datetime को proper format में convert करो
    Fu_data["datetime"]    = pd.to_datetime(Fu_data["datetime"], format="%d-%m-%Y %H:%M")
    if "stock_code" not in Fu_data.columns: # 🔹 Step 2: stock_code columns ensure करो
        Fu_data["stock_code"] = Ch_data["stock_code"].iloc[0]
    if "stock_code" not in Ch_data.columns:
        Ch_data["stock_code"] = Fu_data["stock_code"].iloc[0]

    merged = pd.merge_asof(Ch_data.sort_values("datetime"),Fu_data.sort_values("datetime"),on="datetime", # 🔹 Step 3: पहले normal nearest merge करो
                           by="stock_code",direction="nearest",tolerance=pd.Timedelta("0min")) # nearest 3 min तक match allow

    missing_mask = merged["fu_open"].isna()   # 🔹 Step 4: जिन rows का match नहीं मिला उन्हें अगली available future row से भरें
    if missing_mask.any():
        for idx in merged[missing_mask].index:
            current_time = merged.loc[idx, "datetime"]
            stock = merged.loc[idx, "stock_code"]
            future_rows = Fu_data[(Fu_data["datetime"] > current_time) & (Fu_data["stock_code"] == stock)] # अगला available future row
            if not future_rows.empty:
                nearest_future = future_rows.iloc[0]
                for col in Fu_data.columns:
                    if col not in ["datetime", "stock_code"]:
                        merged.loc[idx, col] = nearest_future[col]
    merged = merged.sort_values(by="datetime").reset_index(drop=True)  # 🔹 Step 5: final formatting
    merged["datetime"] = merged["datetime"].dt.strftime("%d-%m-%Y %H:%M")
    return merged
# # Example usage
# merged_data = merge_data(Ch_data, Fu_data)
# print(tabulate(pd.concat([merged_data.head(3), merged_data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry  get_Expiry   get_Expiry  get_Expiry  get_Expiry  get_Expiry
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Expiry(data, stock_name):
    data["datetime"] = pd.to_datetime(data["datetime"], format="%d-%m-%Y %H:%M")
    unique_dates = data["datetime"].dt.date.unique()
    expiry_map = {}
    for d in unique_dates:
        Dates = pd.Timestamp(d).strftime("%d-%m-%Y 09:15")
        curr_m_expiry = get_Symbol_Expiry(Dates, stock_name, "Monthly", "Current")      # 🔹 Monthly Current Expiry
        if stock_name.lower() == "nifty":
            curr_w_expiry = get_Symbol_Expiry(Dates, stock_name, "Weekiy", "Current")   # 🔹 Weekly Current Expiry
            next_w_expiry = get_Symbol_Expiry(Dates, stock_name, "Weekiy", "Next")      # 🔹 Weekly Next Expiry
            expiry_map[d] = {"curr_m_expiry": curr_m_expiry,"curr_w_expiry": curr_w_expiry,"next_w_expiry": next_w_expiry}
        else:
            expiry_map[d] = {"curr_m_expiry": curr_m_expiry}
    
    if "expiry_date" in data.columns:
        data["curr_m_expiry"] = data["expiry_date"]
        data.drop(columns=["expiry_date"], inplace=True)
    else:
        data["curr_m_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["curr_m_expiry"])
    if stock_name.lower() == "nifty":
        data["curr_w_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["curr_w_expiry"])
        data["next_w_expiry"] = data["datetime"].dt.date.map(lambda x: expiry_map[x]["next_w_expiry"])
    return data

# # Example usage
# All_Data = Data.copy()
# stock_name = "nifty"
# All_Data = get_Expiry(All_Data, stock_name)
# print(tabulate(All_Data.head(5), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data   get_Index_Data  get_Index_Data  get_Index_Data  get_Index_Data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for"):
    def get_Round_ATM(stock_name, Price):
        Strike_Gep = get_Strike_Gep(stock_name)
        return (Price / Strike_Gep).round() * Strike_Gep
    def get_ATM_Strike(merged_data, stock_name):
        Strike_Gep = get_Strike_Gep(stock_name)
        merged_data["ch_atm"] = (merged_data["ch_close"] / Strike_Gep).round() * Strike_Gep
        merged_data["fu_atm"] = (merged_data["fu_close"] / Strike_Gep).round() * Strike_Gep
        return merged_data
    Ch_data = get_Cash_Data(breeze, stock_name, Start_Date, End_Date, interval, Loop_Type)
    Fu_data = get_Futures_Data(breeze, stock_name, Start_Date, End_Date, interval, Loop_Type)
    merged_data = Ch_Fu_merge_data(Ch_data, Fu_data)
    Data_Expiry = get_Expiry(merged_data, stock_name)
    Index_Data  = get_ATM_Strike(Data_Expiry, stock_name)
    return Index_Data
# # Example usage
# stock_name = "reliance"  #"nifty", "nifty bank"
# Start_Date = "01-09-2025"
# End_Date   = "16-10-2025"
# interval   = "1minute"
# Loop_Type  = "for"   #  "for" "while"
# Data = get_Index_Data(breeze, stock_name, Start_Date, End_Date, interval="1minute",Loop_Type = "for")
# print(tabulate(pd.concat([Data.head(3), Data.tail(3)]), headers="keys", tablefmt="psql"))
#=========================================================================================================================================================================================================================================================================================
