import pandas as pd
import zipfile
import os
# Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry
def Extract_Expiry(expiry_date):
    try:
        year = expiry_date.split("-")[-1]
        zip_path = f"/content/drive/MyDrive/Downlod_Options_Data/ALL_Data/BankNifty_Options.zip"
        extract_path = f"/content/Extract/{expiry_date}/"
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_files = zip_ref.namelist()
            # print(zip_files)
            matching_files = [file for file in zip_files if expiry_date in file]
            for file in matching_files:
                zip_ref.extract(file, extract_path)
        inner_zip_path = os.path.join(extract_path, matching_files[0])
        if os.path.exists(inner_zip_path):  # सुनिश्चित करें कि फाइल मौजूद है
            with zipfile.ZipFile(inner_zip_path, 'r') as inner_zip_ref:
                inner_zip_ref.extractall(extract_path)  # सभी फाइलें निकालें
            print(f"Successfully extracted: {inner_zip_path}")
        else:
            print(f"File not found: {inner_zip_path}")

    except Exception as e:
        print(f"extract_expiry Function Error: {e}")
        return None

# expiry_date = "5-12-2024"
# Extract_Expiry(expiry_date)
#_________________________________________________________________________________________________________________________________________

# Merged_csv_files   Merged_csv_files   Merged_csv_files   Merged_csv_files   Merged_csv_files   Merged_csv_files   Merged_csv_files  
def Merged_csv_files(expiry_date):
    try:
        Data_List = []
        path = f"/content/Extract/{expiry_date}"
        all_files = os.listdir(path)
        csv_files = [f for f in all_files if f.endswith('.csv') and "Futures" not in f]

        for file in csv_files:
            Data = pd.read_csv(f"{path}/{file}")
            Data["stock_code"] = Data["stock_code"].astype(str)
            try:
                Data["expiry_date"] = pd.to_datetime(Data["expiry_date"], format="%d-%m-%Y")
            except:
                Data["expiry_date"] = pd.to_datetime(Data["expiry_date"], format="%d-%b-%Y")
            try:
                Data["datetime"] = pd.to_datetime(Data["datetime"], format="%d-%m-%Y %H:%M:%S")
            except:
                Data['datetime'] = pd.to_datetime(Data['datetime'], format="%d-%m-%Y %H:%M")
            
            int_columns = ["strike_price", "call_OI", "call_volume", "put_OI", "put_volume"]
            for col in int_columns:
                Data[col] = pd.to_numeric(Data[col], errors='coerce').fillna(0).astype(int)
            float_columns = ["call_open", "call_high", "call_low", "call_close", "put_open", "put_high", "put_low", "put_close"]
            for col in float_columns:
                Data[col] = pd.to_numeric(Data[col], errors='coerce').fillna(0.0).astype(float)

            Data_List.append(Data)
        Data = pd.concat(Data_List, ignore_index=True)
        Data.sort_values(by=['datetime', 'strike_price'], ascending=[True, True] ).reset_index(drop=True)
        Data["expiry_date"] = Data["expiry_date"].dt.strftime("%d-%m-%Y")
        Data["datetime"] = Data["datetime"].dt.strftime("%d-%m-%Y %H:%M")
        return Data
    except Exception as e:
        print(f"Merged_csv_files Function Error: {e}")

# expiry_date = "27-02-2025"
# Data = Merged_csv_files(expiry_date)
# print(Data)
#_________________________________________________________________________________________________________________________________________
