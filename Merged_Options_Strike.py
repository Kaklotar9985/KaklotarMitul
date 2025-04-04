import pandas as pd
import zipfile
import os
# Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry   Extract_Expiry
def Extract_Expiry(expiry_date, Symbol):
    try:
        year = expiry_date.split("-")[-1]
        zip_path = f"/content/drive/MyDrive/Downlod_Options_Data/ALL_Data/{Symbol.lower()}_All_Strike_Data.zip"
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

bank_nifty_expiry = [ '28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                      '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                      '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                      '25-01-2024', '29-02-2024', '27-03-2024', '24-04-2024', '29-05-2024', '26-06-2024', '31-07-2024', '28-08-2024', '25-09-2024', '30-10-2024', '27-11-2024', '24-12-2024',
                      '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025',  ]

nifty_weekly_expiry = ['07-01-2021', '14-01-2021', '21-01-2021', '28-01-2021', '04-02-2021', '11-02-2021', '18-02-2021', '25-02-2021', '04-03-2021', '10-03-2021', '18-03-2021', '25-03-2021', '01-04-2021', '08-04-2021', '15-04-2021', '22-04-2021', '29-04-2021', '06-05-2021', '12-05-2021', '20-05-2021', '27-05-2021', '03-06-2021', '10-06-2021', '17-06-2021', '24-06-2021', '01-07-2021', '08-07-2021', '15-07-2021', '22-07-2021', '29-07-2021', '05-08-2021', '12-08-2021', '18-08-2021', '26-08-2021', '02-09-2021', '09-09-2021', '16-09-2021', '23-09-2021', '30-09-2021', '07-10-2021', '14-10-2021', '21-10-2021', '28-10-2021', '03-11-2021', '11-11-2021', '18-11-2021', '25-11-2021', '02-12-2021', '09-12-2021', '16-12-2021', '23-12-2021', '30-12-2021', 
                       '06-01-2022', '13-01-2022', '20-01-2022', '27-01-2022', '03-02-2022', '10-02-2022', '17-02-2022', '24-02-2022', '03-03-2022', '10-03-2022', '17-03-2022', '24-03-2022', '31-03-2022', '07-04-2022', '13-04-2022', '21-04-2022', '28-04-2022', '05-05-2022', '12-05-2022', '19-05-2022', '26-05-2022', '02-06-2022', '09-06-2022', '16-06-2022', '23-06-2022', '30-06-2022', '07-07-2022', '14-07-2022', '21-07-2022', '28-07-2022', '04-08-2022', '11-08-2022', '18-08-2022', '25-08-2022', '01-09-2022', '08-09-2022', '15-09-2022', '22-09-2022', '29-09-2022', '06-10-2022', '13-10-2022', '20-10-2022', '27-10-2022', '03-11-2022', '10-11-2022', '17-11-2022', '24-11-2022', '01-12-2022', '08-12-2022', '15-12-2022', '22-12-2022', '29-12-2022', 
                       '05-01-2023', '12-01-2023', '19-01-2023', '25-01-2023', '02-02-2023', '09-02-2023', '16-02-2023', '23-02-2023', '02-03-2023', '09-03-2023', '16-03-2023', '23-03-2023', '29-03-2023', '06-04-2023', '13-04-2023', '20-04-2023', '27-04-2023', '04-05-2023', '11-05-2023', '18-05-2023', '25-05-2023', '01-06-2023', '08-06-2023', '15-06-2023', '22-06-2023', '28-06-2023', '06-07-2023', '13-07-2023', '20-07-2023', '27-07-2023', '03-08-2023', '10-08-2023', '17-08-2023', '24-08-2023', '31-08-2023', '07-09-2023', '14-09-2023', '21-09-2023', '28-09-2023', '05-10-2023', '12-10-2023', '19-10-2023', '26-10-2023', '02-11-2023', '09-11-2023', '16-11-2023', '23-11-2023', '30-11-2023', '07-12-2023', '14-12-2023', '21-12-2023', '28-12-2023', 
                       '04-01-2024', '11-01-2024', '18-01-2024', '25-01-2024', '01-02-2024', '08-02-2024', '15-02-2024', '22-02-2024', '29-02-2024', '07-03-2024', '14-03-2024', '21-03-2024', '28-03-2024', '04-04-2024', '10-04-2024', '18-04-2024', '25-04-2024', '02-05-2024', '09-05-2024', '16-05-2024', '23-05-2024', '30-05-2024', '06-06-2024', '13-06-2024', '20-06-2024', '27-06-2024', '04-07-2024', '11-07-2024', '18-07-2024', '25-07-2024', '01-08-2024', '08-08-2024', '14-08-2024', '22-08-2024', '29-08-2024', '05-09-2024', '12-09-2024', '19-09-2024', '26-09-2024', '03-10-2024', '10-10-2024', '17-10-2024', '24-10-2024', '31-10-2024', '07-11-2024', '14-11-2024', '21-11-2024', '28-11-2024', '05-12-2024', '12-12-2024', '19-12-2024', '26-12-2024', 
                       '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025' ]

