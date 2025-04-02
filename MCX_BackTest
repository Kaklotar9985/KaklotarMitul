from IPython.display import clear_output
import matplotlib.pyplot as plt
from tabulate import tabulate
import pandas as pd
import statistics
import zipfile
import gspread
from datetime import datetime

#=================================================================================================================================================================================================

# Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip
Options_Data = {}
Futures_Data = {}
def Extract_Zip(Expiry_Date, Symbol, Options_Type = "op"):
    global Options_Data, Futures_Data
    # Agar Options ka Data Extract karna ho
    if Options_Type.lower() == "op":
      Options_zip_path = "/content/drive/MyDrive/Downlod_Options_Data/Options_Chain.zip"
      Options_Chain_Data = {}
      target_file = f"{Expiry_Date}.csv"
      with zipfile.ZipFile(Options_zip_path, 'r') as zip_ref:
          csv_files = zip_ref.namelist()
          if target_file in csv_files:
              with zip_ref.open(target_file) as file:
                  data = pd.read_csv(file)
                  data.columns = [col.lower() for col in data.columns]
                  data['datetime'] = pd.to_datetime(data['datetime'], format="%d-%m-%Y %H:%M")
                  data['expiry_date'] = pd.to_datetime(data['expiry_date'], format="%d-%m-%Y")
                  data = data.sort_values(by=['datetime', 'strike_price'], ascending=[True, True] ).reset_index(drop=True)
                  Options_Data[Expiry_Date] = data
          else:
              print(f"{target_file} not found in ZIP")
    # Agar Futures ka Data Extract karna ho
    if Options_Type.lower() == "fu":
       Futures_Data = {}
       Futures_zip_path = f"/content/drive/MyDrive/Downlod_Options_Data/MCX/{Symbol}_Futures.zip"
       with zipfile.ZipFile(Futures_zip_path, 'r') as zip_ref:   # ✅ Yaha galti sahi ki hai
            csv_file = [file for file in zip_ref.namelist() if file.startswith(Expiry_Date)]
            if csv_file:
              with zip_ref.open(csv_file[0]) as file:
                    Futures_Data[Expiry_Date] = pd.read_csv(file)
            else:
                print(f"❌ No Data Found for {Expiry_Date}")

# Call Function
# Expiry_Date = "25-03-2021"
# Extract_Zip(Expiry_Date, "oc")
# print(Options_Chain_Data[Expiry_Date].head())
#__________________________________________________________________________________________________________________________________

#  Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data
def Read_Strike_Data(Expiry, Strike, Symbol, Date_Time="01-01-2000"):
    global Options_Data,Futures_Data
    try:
        Expiry = pd.to_datetime(Expiry, format="%d-%m-%Y").strftime("%d-%m-%Y")
        if Date_Time is not None:
            try:
                Date_Time = pd.to_datetime(Date_Time, format="%d-%m-%Y")
            except ValueError:
                try:
                    Date_Time = pd.to_datetime(Date_Time, format="%d-%m-%Y %H:%M")
                except ValueError:
                    Date_Time = pd.to_datetime(Date_Time, format="%d-%m-%Y %H:%M:%S")

        if int(Strike) != 0 :
          if Expiry not in Options_Data:
              Extract_Zip(Expiry, Symbol, "op")
          Strike_Data = Options_Data[Expiry].copy()
          Strike_Data["expiry_date"] = pd.to_datetime(Strike_Data["expiry_date"], format="%d-%m-%Y")
          target_expiry = pd.to_datetime(Expiry, format="%d-%m-%Y")
          filtered_Strike = Strike_Data[ (Strike_Data['expiry_date']  == target_expiry) &
                                        (Strike_Data['strike_price'] == int(Strike))   ].copy()
          Strike_Data = pd.DataFrame(filtered_Strike)
        if int(Strike) == 0 :
           if Expiry not in Futures_Data:
              Extract_Zip(Expiry, Symbol, "fu")
           Strike_Data = Futures_Data[Expiry].copy()
           Strike_Data = pd.DataFrame(Strike_Data)
        try:
           Strike_Data['datetime'] = pd.to_datetime(Strike_Data['datetime'], format="%d-%m-%Y %H:%M:%S")
        except:
           Strike_Data['datetime'] = pd.to_datetime(Strike_Data['datetime'], format="%d-%m-%Y %H:%M")
        filtered_data = Strike_Data[Strike_Data['datetime'] >= Date_Time].copy()
        filtered_data['datetime'] = filtered_data['datetime'].dt.strftime('%d-%m-%Y %H:%M')
        try:
           filtered_data['expiry_date'] = pd.to_datetime(filtered_data['expiry_date'], format='%d-%b-%Y').dt.strftime('%d-%m-%Y')
        except:
           filtered_data['expiry_date'] = pd.to_datetime(filtered_data['expiry_date'], format='%d-%m-%Y').dt.strftime('%d-%m-%Y')

        data_list =  filtered_data

        return data_list

    except Exception as e:
        print(f"Read_Strike_Data Function Error: {e}")
        return None


# # Example usage
# Expiry    = "26-12-2024"
# Strike    = 23800
# Date_Time = "25-11-2024"
# ATM_Data  = Read_Strike_Data(Expiry, Strike,Date_Time)
# print(ATM_Data)
#____________________________________________________________________________________________________________________________________________
