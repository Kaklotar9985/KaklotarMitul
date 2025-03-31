from datetime import datetime, timedelta, timezone
from dateutil import parser
import pandas as pd

# Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data   Fetch_MCX_Data
def Fetch_MCX_Data ( breeze,exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day):
    try:
        fetch_Futures_Data_Error = {}
        Datas_List = []

        Expiry_Date = datetime.strptime(Expiry_Date, "%d-%m-%Y")
        ToDate = datetime.today()
        end_date = min(Expiry_Date, ToDate)
        Start_Date = end_date - timedelta(days=past_day)
        date_list = [ (Start_Date + timedelta(days=i)).strftime("%d-%m-%Y") for i in range((end_date - Start_Date).days + 1)]

        for Dates in date_list:
            Date        =  datetime.strptime(Dates, "%d-%m-%Y")
            start_date  = datetime.strptime((Date.strftime("%d-%m-%Y 09:15")), "%d-%m-%Y %H:%M")
            end_date    = datetime.strptime(((Date + timedelta(days=1)).strftime("%d-%m-%Y 09:14")), "%d-%m-%Y %H:%M")
            from_date   = start_date.strftime("%Y-%m-%dT00:00:00.000Z")
            to_date     = end_date.strftime("%Y-%m-%dT00:00:00.000Z")
            expiry_date = Expiry_Date.strftime("%Y-%m-%dT00:00:00.000Z")

            right_Data = breeze.get_historical_data_v2( interval = interval, from_date = from_date, to_date = to_date, stock_code   = stock_code,
                         exchange_code = exchange_code, product_type = product_type, expiry_date  = expiry_date, right = right, strike_price = strike_price )

            if right_Data["Error"] is None and right_Data["Success"]:
                if right.lower() == "others":
                  Options_Type = "fu"
                  Column = ["stock_code", "expiry_date", "datetime", f"{Options_Type}_open", f"{Options_Type}_high", f"{Options_Type}_low",f"{Options_Type}_close", f"{Options_Type}_volume", f"{Options_Type}_oi"]
                else:
                  Options_Type = right
                  Column = ["stock_code", "expiry_date", "strike_price","datetime", f"{Options_Type}_open", f"{Options_Type}_high", f"{Options_Type}_low",f"{Options_Type}_close", f"{Options_Type}_volume", f"{Options_Type}_oi"]

                Data = pd.DataFrame(right_Data["Success"])
                Data['datetime'] = Data['datetime'].apply(lambda x: parser.parse(x).strftime('%d-%m-%Y %H:%M'))
                Data['expiry_date'] = Data['expiry_date'].apply(lambda x: parser.parse(x).strftime("%d-%m-%Y"))
                Data = Data.rename(columns={"open": f"{Options_Type}_open", "high": f"{Options_Type}_high", "low": f"{Options_Type}_low","close": f"{Options_Type}_close", "open_interest": f"{Options_Type}_oi", "volume": f"{Options_Type}_volume"})
                Data = Data[Column]
            else:
                if Expiry_Date not in fetch_Futures_Data_Error:
                  fetch_Futures_Data_Error[Expiry_Date] = []
                fetch_Futures_Data_Error[Expiry_Date].append(str(start_date))
                Data = None
            if Data is not None:
                Datas_List.append(Data)

        Analysis_Data = pd.concat(Datas_List)
        Analysis_Data["datetime"] = pd.to_datetime(Analysis_Data["datetime"], format="%d-%m-%Y %H:%M")
        Analysis_Data["expiry_date"] = pd.to_datetime(Analysis_Data["expiry_date"], format="%d-%m-%Y")
        Analysis_Data.sort_values(by="datetime", ascending=True, inplace=True)
        Analysis_Data.reset_index(drop=True, inplace=True)
        Analysis_Data["datetime"] = Analysis_Data["datetime"].dt.strftime('%d-%m-%Y %H:%M')
        Analysis_Data["expiry_date"] = Analysis_Data["expiry_date"].dt.strftime('%d-%m-%Y')
        return Analysis_Data
    except Exception as e:
      print(f"Fetch_MCX_Data Function Error: {e}")
      return None

# # Example usage
# exchange_code = "MCX"
# stock_code    = "CRUDE"      # CRUDE  "NATGAS"
# product_type  = "futures"    # "options" , "futures"
# right         = "others"     # "others" , "call" , "put"
# strike_price  = '0'
# interval      = "1minute"    # "1second" "1minute"
# Expiry_Date   = '19-03-2025'
# past_day      = 5
# Data = Fetch_MCX_Data ( exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)
# print(tabulate(Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
#___________________________________________________________________________________________________________________________________________________________

# fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data   fetch_Merged_Data
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
#______________________________________________________________________________________________________________________________
#  Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data   Fetch_Historical_Data    Fetch_Historical_Data  Fetch_Historical_Data
def Fetch_Historical_Data ( breeze, exchange_code, stock_code, strike_price, interval, Expiry_Date, past_day):
    try:
        if strike_price == '0':
          product_type  = "futures"
          right         = "others"
          Data = Fetch_MCX_Data ( breeze, exchange_code, stock_code, product_type, right, strike_price, interval, Expiry_Date, past_day)
        if strike_price != '0':
          product_type  = "options"
          Data_call = Fetch_MCX_Data ( breeze, exchange_code, stock_code, product_type, "call", strike_price, interval, Expiry_Date, past_day)
          Data_put  = Fetch_MCX_Data ( breeze, exchange_code, stock_code, product_type, "put",  strike_price, interval, Expiry_Date, past_day)
          if Data_call is not None and Data_put is not None:
              Data = fetch_Merged_Data(Data_call, Data_put)
        return Data
    except Exception as e:
        print(f"Fetch_Historical_Data Function Error: {e}")
        return None

# # Example usage
# exchange_code = "MCX"
# stock_code    = "CRUDE"      # CRUDE  "NATGAS"
# strike_price  = '0'
# interval      = "1minute"
# Expiry_Date   = '21-04-2025'
# past_day      = 5
# Data = Fetch_Historical_Data ( exchange_code, stock_code, strike_price, interval, Expiry_Date, past_day)
# print(tabulate(Data.head(5), headers='keys', tablefmt='pretty', showindex=False))
# print(Data)
#_______________________________________________________________________________________________________________________________________________

# fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  fetch_Strike_Range  
def fetch_Strike_Range(Data, Expiry_Date):
    try:
        filtered_data = [entry for entry in Data if entry['Options_Expiry'] == Expiry_Date]
        if filtered_data:
            return filtered_data[0]
        else:
            print("No data found for Expiry_Date:", Expiry_Date)
            return None  # Return None if no matching data is found
    except Exception as e:
        print(f"fetch_Strike_Range Function Error: {e}")
        return None
#_______________________________________________________________________________________________________________________________________________

# Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File   Downlod_File  
def Downlod_File(FilePath, FileName, fileType, Data):
    try:
        file_path = f'{FilePath}{FileName}.{fileType}'

        if fileType == 'csv':
            Data.to_csv(file_path, index=False)
        elif fileType == 'excel':
            Data.to_excel(file_path, index=False)
        elif fileType == 'json':
            Data.to_json(file_path, orient='records')
        else:
            print("Unsupported file type")
    except Exception as e:
        print(f"Downlod_File Function Error: {e}")

#_______________________________________________________________________________________________________________________________________________



# MCX_Data
Crude_Futures_Expiry_List = ['19-01-2023', '17-02-2023', '20-03-2023', '19-04-2023', '19-05-2023', '16-06-2023', '19-07-2023', '21-08-2023', '19-09-2023', '19-10-2023', '17-11-2023', '18-12-2023', '19-01-2024', '16-02-2024', '19-03-2024', '19-04-2024', '20-05-2024', '18-06-2024', '19-07-2024', '19-08-2024', '19-09-2024', '21-10-2024', '19-11-2024', '18-12-2024', '17-01-2025', '19-02-2025', '19-03-2025', '21-04-2025', '19-05-2025', '18-06-2025']
Crude_Options_Expiry_List = ['17-01-2023', '15-02-2023', '16-03-2023', '17-04-2023', '17-05-2023', '14-06-2023', '17-07-2023', '17-08-2023', '15-09-2023', '17-10-2023', '15-11-2023', '14-12-2023', '17-01-2024', '14-02-2024', '15-03-2024', '17-04-2024', '16-05-2024', '14-06-2024', '17-07-2024', '14-08-2024', '17-09-2024', '17-10-2024', '15-11-2024', '16-12-2024', '15-01-2025', '17-02-2025', '17-03-2025', '16-04-2025', '15-05-2025', '16-06-2025']
Crude_Expiry_List = [{"Futures_Expiry":"19-01-2023","Options_Expiry":"17-01-2023","Min_strike":5600,"Max_strike":7600},{"Futures_Expiry":"17-02-2023","Options_Expiry":"15-02-2023","Min_strike":5000,"Max_strike":7650},{"Futures_Expiry":"20-03-2023","Options_Expiry":"16-03-2023","Min_strike":4300,"Max_strike":7700},{"Futures_Expiry":"19-04-2023","Options_Expiry":"17-04-2023","Min_strike":4350,"Max_strike":7850},{"Futures_Expiry":"19-05-2023","Options_Expiry":"17-05-2023","Min_strike":4400,"Max_strike":7850},{"Futures_Expiry":"16-06-2023","Options_Expiry":"14-06-2023","Min_strike":4550,"Max_strike":7800},
                     {"Futures_Expiry":"19-07-2023","Options_Expiry":"17-07-2023","Min_strike":4550,"Max_strike":7300},{"Futures_Expiry":"21-08-2023","Options_Expiry":"17-08-2023","Min_strike":4550,"Max_strike":8050},{"Futures_Expiry":"19-09-2023","Options_Expiry":"15-09-2023","Min_strike":5250,"Max_strike":8800},{"Futures_Expiry":"19-10-2023","Options_Expiry":"17-10-2023","Min_strike":5450,"Max_strike":8900},{"Futures_Expiry":"17-11-2023","Options_Expiry":"15-11-2023","Min_strike":5000,"Max_strike":8700},{"Futures_Expiry":"18-12-2023","Options_Expiry":"14-12-2023","Min_strike":4650,"Max_strike":8400},
                     {"Futures_Expiry":"19-01-2024","Options_Expiry":"17-01-2024","Min_strike":4700,"Max_strike":7650},{"Futures_Expiry":"16-02-2024","Options_Expiry":"14-02-2024","Min_strike":4850,"Max_strike":7600},{"Futures_Expiry":"19-03-2024","Options_Expiry":"15-03-2024","Min_strike":5000,"Max_strike":7950},{"Futures_Expiry":"19-04-2024","Options_Expiry":"17-04-2024","Min_strike":5300,"Max_strike":8300},{"Futures_Expiry":"20-05-2024","Options_Expiry":"16-05-2024","Min_strike":5400,"Max_strike":8300},{"Futures_Expiry":"18-06-2024","Options_Expiry":"14-06-2024","Min_strike":5050,"Max_strike":8050},
                     {"Futures_Expiry":"19-07-2024","Options_Expiry":"17-07-2024","Min_strike":5100,"Max_strike":8050},{"Futures_Expiry":"19-08-2024","Options_Expiry":"14-08-2024","Min_strike":5000,"Max_strike":8000},{"Futures_Expiry":"19-09-2024","Options_Expiry":"17-09-2024","Min_strike":4500,"Max_strike":7600},{"Futures_Expiry":"21-10-2024","Options_Expiry":"17-10-2024","Min_strike":4500,"Max_strike":7500},{"Futures_Expiry":"19-11-2024","Options_Expiry":"15-11-2024","Min_strike":4600,"Max_strike":7450},{"Futures_Expiry":"18-12-2024","Options_Expiry":"16-12-2024","Min_strike":4600,"Max_strike":7100},
                     {"Futures_Expiry":"17-01-2025","Options_Expiry":"15-01-2025","Min_strike":4650,"Max_strike":7950},{"Futures_Expiry":"19-02-2025","Options_Expiry":"17-02-2025","Min_strike":4850,"Max_strike":7850},{"Futures_Expiry":"19-03-2025","Options_Expiry":"17-03-2025","Min_strike":4700,"Max_strike":7650},{"Futures_Expiry":"21-04-2025","Options_Expiry":"16-04-2025","Min_strike":4700,"Max_strike":7500},{"Futures_Expiry":"19-05-2025","Options_Expiry":"15-05-2025","Min_strike":4700,"Max_strike":7150},{"Futures_Expiry":"18-06-2025","Options_Expiry":"16-06-2025","Min_strike":4850,"Max_strike":6900}]

