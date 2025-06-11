from tabulate import tabulate
import pandas as pd
import os

def Brokerage_Calculate(buy_price, sell_price, quantity, Options_Type="OP", Min_Brokerage = 20):
    try:
        turnover = (buy_price + sell_price) * quantity               # **Turnover Calculation**
        if Options_Type.lower() == "fu":  # **Futures Calculation**
            brokerage = min(0.0003 * turnover, Min_Brokerage) * 2    # ₹20 प्रति ऑर्डर, दोनों ओर के लिए ₹40
            stt = 0.0002 * sell_price * quantity                     # 0.02% केवल Sell Side
            transaction_charges = 0.0000183 * turnover               # 0.00183% NSE Transaction Charges
            sebi_charges = (10 / 10000000) * turnover                # ₹10 प्रति करोड़
            stamp_duty = round((0.00002 * buy_price * quantity),0)   # 0.002% (₹200/Crore) on Buy Side
        elif Options_Type.lower() == "call" or Options_Type.lower() == "put" or Options_Type.lower() == "op" : # **Options Calculation**
            option_premium = (buy_price + sell_price)
            turnover = option_premium * quantity
            brokerage = Min_Brokerage * 2                             # ₹20 प्रति ऑर्डर, दोनों ओर के लिए ₹40
            stt = 0.0005 * option_premium * quantity                  # 0.05% STT केवल Sell Side
            transaction_charges = 0.0003553 * turnover                # 0.03603% NSE Transaction Charges
            sebi_charges = (10 / 10000000) * turnover                 # ₹10 प्रति करोड़
            stamp_duty = round((0.00003 * buy_price * quantity),0)    # 0.003% (₹300/Crore) on Buy Side
        gst = 0.18 * (brokerage + transaction_charges + sebi_charges) # GST Calculation
        total_charges = brokerage + stt + transaction_charges + gst + sebi_charges + stamp_duty
        return round(total_charges, 2)
    except Exception as e:
        print(f"Brokerage_Calculate Function Error: {e}")
        return 0

def Streak_Merge_CSV (directory_path):
    # directory_path = '/content/'
    csv_All_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
    New_Quantity = 0
    Data_List = []
    for file in csv_All_files:
        file_path = os.path.join(directory_path, file)
        Data = pd.read_csv(file_path)
        for i in range(len(Data)):
            Date         = pd.to_datetime(str(Data['Trigger Date'].iloc[i]), format="%d/%m/%Y").strftime('%d-%m-%Y')
            Time         = pd.to_datetime(str(Data[' Trigger Time'].iloc[i]), format="%H:%M:%S").strftime('%H:%M')
            Instrument   = Data[' Instrument'].iloc[i]
            BuySell      = Data['Buy/Sell'].iloc[i]
            Quantity     = Data['Quantity'].iloc[i]
            Price        = Data['Price'].iloc[i]
            Trigger_type = Data['Trigger type'].iloc[i]

            P_Date         = pd.to_datetime(str(Data['Trigger Date'].iloc[i-1]), format="%d/%m/%Y").strftime('%d-%m-%Y')
            P_Time         = pd.to_datetime(str(Data[' Trigger Time'].iloc[i-1]), format="%H:%M:%S").strftime('%H:%M')
            P_Instrument   = Data[' Instrument'].iloc[i-1]
            P_BuySell      = Data['Buy/Sell'].iloc[i-1]
            P_Quantity     = Data['Quantity'].iloc[i-1]
            P_Price        = Data['Price'].iloc[i-1]
            P_Trigger_type = Data['Trigger type'].iloc[i-1]
            Strike = Instrument[-7:-2]
            option = Instrument[-2:]
            if Instrument == P_Instrument and P_BuySell == "SELL" and BuySell == "BUY" :
              QTY = New_Quantity if New_Quantity != 0 else Quantity
              Entry_Price = round(float(P_Price),2)
              Exit_Price = round(float(Price),2)
              Brokerage = Brokerage_Calculate(buy_price=Exit_Price, sell_price=Entry_Price, quantity=QTY, Options_Type="OP")
              Net_PNL = round((float(Entry_Price) - float(Exit_Price))*QTY,2)
              PNL = round(Net_PNL - Brokerage,2)

              Datas = {"Entry_DateTime": P_Date+" "+P_Time,
                      "Exit_DateTime" : Date+" "+Time,
                      "Instrument"    : Instrument,
                      "Strike"        : Strike ,
                      "option"        : option,
                      "BuySell"       : P_BuySell,
                      "Quantity"      : QTY, 
                      "Entry_Price"   : Entry_Price,
                      "Exit_Price"    : Exit_Price,
                      "Net_PNL"       : Net_PNL,
                      "Brokerage"     : Brokerage  ,
                      "PNL"           : PNL, 
                      "Trigger_type"  : Trigger_type,}
              
              Data_List.append(Datas)

    # Convert Data_List to DataFrame
    Analysis_Data = pd.DataFrame(Data_List)
    Analysis_Data.drop_duplicates(inplace=True)
    # Convert DateTime columns to proper format
    Analysis_Data["Entry_DateTime"] = pd.to_datetime(Analysis_Data["Entry_DateTime"], format="%d-%m-%Y %H:%M")
    Analysis_Data["Exit_DateTime"]  = pd.to_datetime(Analysis_Data["Exit_DateTime"], format="%d-%m-%Y %H:%M")
    Analysis_Data.sort_values(by=["Entry_DateTime", "option"], ascending=True, inplace=True)
    Analysis_Data.reset_index(drop=True, inplace=True)
    Analysis_Data["drawdown"] = 0.0
    for i in range(1, len(Analysis_Data)):
        running_total = Analysis_Data.loc[i - 1, "drawdown"] + Analysis_Data.loc[i, "PNL"]
        Analysis_Data.loc[i, "drawdown"] = round((running_total if running_total < 0 else 0.0), 2)
    # Extract Month and Year
    Analysis_Data["Month"]   = Analysis_Data["Entry_DateTime"].dt.month
    Analysis_Data["Quarter"] = Analysis_Data["Entry_DateTime"].dt.quarter
    Analysis_Data["Year"]    = Analysis_Data["Entry_DateTime"].dt.year
    Analysis_Data["Entry_DateTime"] = Analysis_Data["Entry_DateTime"].dt.strftime('%d-%m-%Y %H:%M')
    Analysis_Data["Exit_DateTime"]  = Analysis_Data["Exit_DateTime"].dt.strftime('%d-%m-%Y %H:%M')
    return Analysis_Data

# directory_path = '/content/'
# Analysis_Data = Streak_Merge_CSV(directory_path)
# # Save cleaned file
# File_Name = "Data_List_Cleaned.csv"
# Analysis_Data.to_csv(File_Name, index=False)
# # Download file in Google Colab
# from google.colab import files
# files.download(File_Name)
# # Display updated table
# print("\nUpdated Analysis Data with Drawdowns (Duplicates Removed):")
# print(tabulate(Analysis_Data.head(20), headers="keys", tablefmt="pretty", showindex=False))
