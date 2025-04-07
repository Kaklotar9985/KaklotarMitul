from IPython.display import clear_output
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime
import pandas as pd
import statistics
import importlib
import zipfile
import gspread


banknifty_monthly_expiry = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '27-03-2024', '24-04-2024', '29-05-2024', '26-06-2024', '31-07-2024', '28-08-2024', '25-09-2024', '30-10-2024', '27-11-2024', '24-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025',  ]

nifty_monthly_expiry     = ['28-01-2021', '25-02-2021', '25-03-2021', '29-04-2021', '27-05-2021', '24-06-2021', '29-07-2021', '26-08-2021', '30-09-2021', '28-10-2021', '25-11-2021', '30-12-2021',
                            '27-01-2022', '24-02-2022', '31-03-2022', '28-04-2022', '26-05-2022', '30-06-2022', '28-07-2022', '25-08-2022', '29-09-2022', '27-10-2022', '24-11-2022', '29-12-2022',
                            '25-01-2023', '23-02-2023', '29-03-2023', '27-04-2023', '25-05-2023', '28-06-2023', '27-07-2023', '31-08-2023', '28-09-2023', '26-10-2023', '30-11-2023', '28-12-2023',
                            '25-01-2024', '29-02-2024', '28-03-2024', '25-04-2024', '30-05-2024', '27-06-2024', '25-07-2024', '29-08-2024', '26-09-2024', '31-10-2024', '28-11-2024', '26-12-2024',
                            '30-01-2025', '27-02-2025', '27-03-2025', '24-04-2025', ]

nifty_weekly_expiry      = ['07-01-2021', '14-01-2021', '21-01-2021', '28-01-2021', '04-02-2021', '11-02-2021', '18-02-2021', '25-02-2021', '04-03-2021', '10-03-2021', '18-03-2021', '25-03-2021', '01-04-2021', '08-04-2021', '15-04-2021', '22-04-2021', '29-04-2021', '06-05-2021', '12-05-2021', '20-05-2021', '27-05-2021', '03-06-2021', '10-06-2021', '17-06-2021', '24-06-2021', '01-07-2021', '08-07-2021', '15-07-2021', '22-07-2021', '29-07-2021', '05-08-2021', '12-08-2021', '18-08-2021', '26-08-2021', '02-09-2021', '09-09-2021', '16-09-2021', '23-09-2021', '30-09-2021', '07-10-2021', '14-10-2021', '21-10-2021', '28-10-2021', '03-11-2021', '11-11-2021', '18-11-2021', '25-11-2021', '02-12-2021', '09-12-2021', '16-12-2021', '23-12-2021', '30-12-2021',
                            '06-01-2022', '13-01-2022', '20-01-2022', '27-01-2022', '03-02-2022', '10-02-2022', '17-02-2022', '24-02-2022', '03-03-2022', '10-03-2022', '17-03-2022', '24-03-2022', '31-03-2022', '07-04-2022', '13-04-2022', '21-04-2022', '28-04-2022', '05-05-2022', '12-05-2022', '19-05-2022', '26-05-2022', '02-06-2022', '09-06-2022', '16-06-2022', '23-06-2022', '30-06-2022', '07-07-2022', '14-07-2022', '21-07-2022', '28-07-2022', '04-08-2022', '11-08-2022', '18-08-2022', '25-08-2022', '01-09-2022', '08-09-2022', '15-09-2022', '22-09-2022', '29-09-2022', '06-10-2022', '13-10-2022', '20-10-2022', '27-10-2022', '03-11-2022', '10-11-2022', '17-11-2022', '24-11-2022', '01-12-2022', '08-12-2022', '15-12-2022', '22-12-2022', '29-12-2022',
                            '05-01-2023', '12-01-2023', '19-01-2023', '25-01-2023', '02-02-2023', '09-02-2023', '16-02-2023', '23-02-2023', '02-03-2023', '09-03-2023', '16-03-2023', '23-03-2023', '29-03-2023', '06-04-2023', '13-04-2023', '20-04-2023', '27-04-2023', '04-05-2023', '11-05-2023', '18-05-2023', '25-05-2023', '01-06-2023', '08-06-2023', '15-06-2023', '22-06-2023', '28-06-2023', '06-07-2023', '13-07-2023', '20-07-2023', '27-07-2023', '03-08-2023', '10-08-2023', '17-08-2023', '24-08-2023', '31-08-2023', '07-09-2023', '14-09-2023', '21-09-2023', '28-09-2023', '05-10-2023', '12-10-2023', '19-10-2023', '26-10-2023', '02-11-2023', '09-11-2023', '16-11-2023', '23-11-2023', '30-11-2023', '07-12-2023', '14-12-2023', '21-12-2023', '28-12-2023',
                            '04-01-2024', '11-01-2024', '18-01-2024', '25-01-2024', '01-02-2024', '08-02-2024', '15-02-2024', '22-02-2024', '29-02-2024', '07-03-2024', '14-03-2024', '21-03-2024', '28-03-2024', '04-04-2024', '10-04-2024', '18-04-2024', '25-04-2024', '02-05-2024', '09-05-2024', '16-05-2024', '23-05-2024', '30-05-2024', '06-06-2024', '13-06-2024', '20-06-2024', '27-06-2024', '04-07-2024', '11-07-2024', '18-07-2024', '25-07-2024', '01-08-2024', '08-08-2024', '14-08-2024', '22-08-2024', '29-08-2024', '05-09-2024', '12-09-2024', '19-09-2024', '26-09-2024', '03-10-2024', '10-10-2024', '17-10-2024', '24-10-2024', '31-10-2024', '07-11-2024', '14-11-2024', '21-11-2024', '28-11-2024', '05-12-2024', '12-12-2024', '19-12-2024', '26-12-2024',
                            '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025' ]

market_open_dates        = ['01-01-2021', '04-01-2021', '05-01-2021', '06-01-2021', '07-01-2021', '08-01-2021', '11-01-2021', '12-01-2021', '13-01-2021', '14-01-2021', '15-01-2021', '18-01-2021', '19-01-2021', '20-01-2021', '21-01-2021', '22-01-2021', '25-01-2021', '27-01-2021', '28-01-2021', '29-01-2021', '01-02-2021', '02-02-2021', '03-02-2021', '04-02-2021', '05-02-2021', '08-02-2021', '09-02-2021', '10-02-2021', '11-02-2021', '12-02-2021', '15-02-2021', '16-02-2021', '17-02-2021', '18-02-2021', '19-02-2021', '22-02-2021', '23-02-2021', '24-02-2021', '25-02-2021', '26-02-2021', '01-03-2021', '02-03-2021', '03-03-2021', '04-03-2021', '05-03-2021', '08-03-2021', '09-03-2021', '10-03-2021', '12-03-2021', '15-03-2021', '16-03-2021', '17-03-2021', '18-03-2021', '19-03-2021', '22-03-2021', '23-03-2021', '24-03-2021', '25-03-2021', '26-03-2021', '30-03-2021', '31-03-2021', '01-04-2021', '05-04-2021', '06-04-2021', '07-04-2021', '08-04-2021', '09-04-2021', '12-04-2021', '13-04-2021', '15-04-2021', '16-04-2021', '19-04-2021', '20-04-2021', '22-04-2021', '23-04-2021', '26-04-2021', '27-04-2021', '28-04-2021', '29-04-2021', '30-04-2021', '03-05-2021', '04-05-2021', '05-05-2021', '06-05-2021', '07-05-2021', '10-05-2021', '11-05-2021', '12-05-2021', '14-05-2021', '17-05-2021', '18-05-2021', '19-05-2021', '20-05-2021', '21-05-2021', '24-05-2021', '25-05-2021', '26-05-2021', '27-05-2021', '28-05-2021', '31-05-2021', '01-06-2021', '02-06-2021', '03-06-2021', '04-06-2021', '07-06-2021', '08-06-2021', '09-06-2021', '10-06-2021', '11-06-2021', '14-06-2021', '15-06-2021', '16-06-2021', '17-06-2021', '18-06-2021', '21-06-2021', '22-06-2021', '23-06-2021', '24-06-2021', '25-06-2021', '28-06-2021', '29-06-2021', '30-06-2021', '01-07-2021', '02-07-2021', '05-07-2021', '06-07-2021', '07-07-2021', '08-07-2021', '09-07-2021', '12-07-2021', '13-07-2021', '14-07-2021', '15-07-2021', '16-07-2021', '19-07-2021', '20-07-2021', '22-07-2021', '23-07-2021', '26-07-2021', '27-07-2021', '28-07-2021', '29-07-2021', '30-07-2021', '02-08-2021', '03-08-2021', '04-08-2021', '05-08-2021', '06-08-2021', '09-08-2021', '10-08-2021', '11-08-2021', '12-08-2021', '13-08-2021', '16-08-2021', '17-08-2021', '18-08-2021', '20-08-2021', '23-08-2021', '24-08-2021', '25-08-2021', '26-08-2021', '27-08-2021', '30-08-2021', '31-08-2021', '01-09-2021', '02-09-2021', '03-09-2021', '06-09-2021', '07-09-2021', '08-09-2021', '09-09-2021', '13-09-2021', '14-09-2021', '15-09-2021', '16-09-2021', '17-09-2021', '20-09-2021', '21-09-2021', '22-09-2021', '23-09-2021', '24-09-2021', '27-09-2021', '28-09-2021', '29-09-2021', '30-09-2021', '01-10-2021', '04-10-2021', '05-10-2021', '06-10-2021', '07-10-2021', '08-10-2021', '11-10-2021', '12-10-2021', '13-10-2021', '14-10-2021', '18-10-2021', '19-10-2021', '20-10-2021', '21-10-2021', '22-10-2021', '25-10-2021', '26-10-2021', '27-10-2021', '28-10-2021', '29-10-2021', '01-11-2021', '02-11-2021', '03-11-2021', '04-11-2021', '08-11-2021', '09-11-2021', '10-11-2021', '11-11-2021', '12-11-2021', '15-11-2021', '16-11-2021', '17-11-2021', '18-11-2021', '22-11-2021', '23-11-2021', '24-11-2021', '25-11-2021', '26-11-2021', '29-11-2021', '30-11-2021', '01-12-2021', '02-12-2021', '03-12-2021', '06-12-2021', '07-12-2021', '08-12-2021', '09-12-2021', '10-12-2021', '13-12-2021', '14-12-2021', '15-12-2021', '16-12-2021', '17-12-2021', '20-12-2021', '21-12-2021', '22-12-2021', '23-12-2021', '24-12-2021', '27-12-2021', '28-12-2021', '29-12-2021', '30-12-2021', '31-12-2021',
                            '03-01-2022', '04-01-2022', '05-01-2022', '06-01-2022', '07-01-2022', '10-01-2022', '11-01-2022', '12-01-2022', '13-01-2022', '14-01-2022', '17-01-2022', '18-01-2022', '19-01-2022', '20-01-2022', '21-01-2022', '24-01-2022', '25-01-2022', '27-01-2022', '28-01-2022', '31-01-2022', '01-02-2022', '02-02-2022', '03-02-2022', '04-02-2022', '07-02-2022', '08-02-2022', '09-02-2022', '10-02-2022', '11-02-2022', '14-02-2022', '15-02-2022', '16-02-2022', '17-02-2022', '18-02-2022', '21-02-2022', '22-02-2022', '23-02-2022', '24-02-2022', '25-02-2022', '28-02-2022', '02-03-2022', '03-03-2022', '04-03-2022', '07-03-2022', '08-03-2022', '09-03-2022', '10-03-2022', '11-03-2022', '14-03-2022', '15-03-2022', '16-03-2022', '17-03-2022', '21-03-2022', '22-03-2022', '23-03-2022', '24-03-2022', '25-03-2022', '28-03-2022', '29-03-2022', '30-03-2022', '31-03-2022', '01-04-2022', '04-04-2022', '05-04-2022', '06-04-2022', '07-04-2022', '08-04-2022', '11-04-2022', '12-04-2022', '13-04-2022', '18-04-2022', '19-04-2022', '20-04-2022', '21-04-2022', '22-04-2022', '25-04-2022', '26-04-2022', '27-04-2022', '28-04-2022', '29-04-2022', '02-05-2022', '04-05-2022', '05-05-2022', '06-05-2022', '09-05-2022', '10-05-2022', '11-05-2022', '12-05-2022', '13-05-2022', '16-05-2022', '17-05-2022', '18-05-2022', '19-05-2022', '20-05-2022', '23-05-2022', '24-05-2022', '25-05-2022', '26-05-2022', '27-05-2022', '30-05-2022', '31-05-2022', '01-06-2022', '02-06-2022', '03-06-2022', '06-06-2022', '07-06-2022', '08-06-2022', '09-06-2022', '10-06-2022', '13-06-2022', '14-06-2022', '15-06-2022', '16-06-2022', '17-06-2022', '20-06-2022', '21-06-2022', '22-06-2022', '23-06-2022', '24-06-2022', '27-06-2022', '28-06-2022', '29-06-2022', '30-06-2022', '01-07-2022', '04-07-2022', '05-07-2022', '06-07-2022', '07-07-2022', '08-07-2022', '11-07-2022', '12-07-2022', '13-07-2022', '14-07-2022', '15-07-2022', '18-07-2022', '19-07-2022', '20-07-2022', '21-07-2022', '22-07-2022', '25-07-2022', '26-07-2022', '27-07-2022', '28-07-2022', '29-07-2022', '01-08-2022', '02-08-2022', '03-08-2022', '04-08-2022', '05-08-2022', '08-08-2022', '10-08-2022', '11-08-2022', '12-08-2022', '16-08-2022', '17-08-2022', '18-08-2022', '19-08-2022', '22-08-2022', '23-08-2022', '24-08-2022', '25-08-2022', '26-08-2022', '29-08-2022', '30-08-2022', '01-09-2022', '02-09-2022', '05-09-2022', '06-09-2022', '07-09-2022', '08-09-2022', '09-09-2022', '12-09-2022', '13-09-2022', '14-09-2022', '15-09-2022', '16-09-2022', '19-09-2022', '20-09-2022', '21-09-2022', '22-09-2022', '23-09-2022', '26-09-2022', '27-09-2022', '28-09-2022', '29-09-2022', '30-09-2022', '03-10-2022', '04-10-2022', '06-10-2022', '07-10-2022', '10-10-2022', '11-10-2022', '12-10-2022', '13-10-2022', '14-10-2022', '17-10-2022', '18-10-2022', '19-10-2022', '20-10-2022', '21-10-2022', '24-10-2022', '25-10-2022', '27-10-2022', '28-10-2022', '31-10-2022', '01-11-2022', '02-11-2022', '03-11-2022', '04-11-2022', '07-11-2022', '09-11-2022', '10-11-2022', '11-11-2022', '14-11-2022', '15-11-2022', '16-11-2022', '17-11-2022', '18-11-2022', '21-11-2022', '22-11-2022', '23-11-2022', '24-11-2022', '25-11-2022', '28-11-2022', '29-11-2022', '30-11-2022', '01-12-2022', '02-12-2022', '05-12-2022', '06-12-2022', '07-12-2022', '08-12-2022', '09-12-2022', '12-12-2022', '13-12-2022', '14-12-2022', '15-12-2022', '16-12-2022', '19-12-2022', '20-12-2022', '21-12-2022', '22-12-2022', '23-12-2022', '26-12-2022', '27-12-2022', '28-12-2022', '29-12-2022', '30-12-2022',
                            '02-01-2023', '03-01-2023', '04-01-2023', '05-01-2023', '06-01-2023', '09-01-2023', '10-01-2023', '11-01-2023', '12-01-2023', '13-01-2023', '16-01-2023', '17-01-2023', '18-01-2023', '19-01-2023', '20-01-2023', '23-01-2023', '24-01-2023', '25-01-2023', '27-01-2023', '30-01-2023', '31-01-2023', '01-02-2023', '02-02-2023', '03-02-2023', '06-02-2023', '07-02-2023', '08-02-2023', '09-02-2023', '10-02-2023', '13-02-2023', '14-02-2023', '15-02-2023', '16-02-2023', '17-02-2023', '20-02-2023', '21-02-2023', '22-02-2023', '23-02-2023', '24-02-2023', '27-02-2023', '28-02-2023', '01-03-2023', '02-03-2023', '03-03-2023', '06-03-2023', '08-03-2023', '09-03-2023', '10-03-2023', '13-03-2023', '14-03-2023', '15-03-2023', '16-03-2023', '17-03-2023', '20-03-2023', '21-03-2023', '22-03-2023', '23-03-2023', '24-03-2023', '27-03-2023', '28-03-2023', '29-03-2023', '31-03-2023', '03-04-2023', '05-04-2023', '06-04-2023', '10-04-2023', '11-04-2023', '12-04-2023', '13-04-2023', '17-04-2023', '18-04-2023', '19-04-2023', '20-04-2023', '21-04-2023', '24-04-2023', '25-04-2023', '26-04-2023', '27-04-2023', '28-04-2023', '02-05-2023', '03-05-2023', '04-05-2023', '05-05-2023', '08-05-2023', '09-05-2023', '10-05-2023', '11-05-2023', '12-05-2023', '15-05-2023', '16-05-2023', '17-05-2023', '18-05-2023', '19-05-2023', '22-05-2023', '23-05-2023', '24-05-2023', '25-05-2023', '26-05-2023', '29-05-2023', '30-05-2023', '31-05-2023', '01-06-2023', '02-06-2023', '05-06-2023', '06-06-2023', '07-06-2023', '08-06-2023', '09-06-2023', '12-06-2023', '13-06-2023', '14-06-2023', '15-06-2023', '16-06-2023', '19-06-2023', '20-06-2023', '21-06-2023', '22-06-2023', '23-06-2023', '26-06-2023', '27-06-2023', '28-06-2023', '30-06-2023', '03-07-2023', '04-07-2023', '05-07-2023', '06-07-2023', '07-07-2023', '10-07-2023', '11-07-2023', '12-07-2023', '13-07-2023', '14-07-2023', '17-07-2023', '18-07-2023', '19-07-2023', '20-07-2023', '21-07-2023', '24-07-2023', '25-07-2023', '26-07-2023', '27-07-2023', '28-07-2023', '31-07-2023', '01-08-2023', '02-08-2023', '03-08-2023', '04-08-2023', '07-08-2023', '08-08-2023', '09-08-2023', '10-08-2023', '11-08-2023', '14-08-2023', '16-08-2023', '17-08-2023', '18-08-2023', '21-08-2023', '22-08-2023', '23-08-2023', '24-08-2023', '25-08-2023', '28-08-2023', '29-08-2023', '30-08-2023', '31-08-2023', '01-09-2023', '04-09-2023', '05-09-2023', '06-09-2023', '07-09-2023', '08-09-2023', '11-09-2023', '12-09-2023', '13-09-2023', '14-09-2023', '15-09-2023', '18-09-2023', '20-09-2023', '21-09-2023', '22-09-2023', '25-09-2023', '26-09-2023', '27-09-2023', '28-09-2023', '29-09-2023', '03-10-2023', '04-10-2023', '05-10-2023', '06-10-2023', '09-10-2023', '10-10-2023', '11-10-2023', '12-10-2023', '13-10-2023', '16-10-2023', '17-10-2023', '18-10-2023', '19-10-2023', '20-10-2023', '23-10-2023', '25-10-2023', '26-10-2023', '27-10-2023', '30-10-2023', '31-10-2023', '01-11-2023', '02-11-2023', '03-11-2023', '06-11-2023', '07-11-2023', '08-11-2023', '09-11-2023', '10-11-2023', '12-11-2023', '13-11-2023', '15-11-2023', '16-11-2023', '17-11-2023', '20-11-2023', '21-11-2023', '22-11-2023', '23-11-2023', '24-11-2023', '28-11-2023', '29-11-2023', '30-11-2023', '01-12-2023', '04-12-2023', '05-12-2023', '06-12-2023', '07-12-2023', '08-12-2023', '11-12-2023', '12-12-2023', '13-12-2023', '14-12-2023', '15-12-2023', '18-12-2023', '19-12-2023', '20-12-2023', '21-12-2023', '22-12-2023', '26-12-2023', '27-12-2023', '28-12-2023', '29-12-2023',
                            '01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '29-01-2024', '30-01-2024', '31-01-2024', '01-02-2024', '02-02-2024', '05-02-2024', '06-02-2024', '07-02-2024', '08-02-2024', '09-02-2024', '12-02-2024', '13-02-2024', '14-02-2024', '15-02-2024', '16-02-2024', '19-02-2024', '20-02-2024', '21-02-2024', '22-02-2024', '23-02-2024', '26-02-2024', '27-02-2024', '28-02-2024', '29-02-2024', '01-03-2024', '02-03-2024', '04-03-2024', '05-03-2024', '06-03-2024', '07-03-2024', '11-03-2024', '12-03-2024', '13-03-2024', '14-03-2024', '15-03-2024', '18-03-2024', '19-03-2024', '20-03-2024', '21-03-2024', '22-03-2024', '26-03-2024', '27-03-2024', '28-03-2024', '01-04-2024', '02-04-2024', '03-04-2024', '04-04-2024', '05-04-2024', '08-04-2024', '09-04-2024', '10-04-2024', '12-04-2024', '15-04-2024', '16-04-2024', '18-04-2024', '19-04-2024', '22-04-2024', '23-04-2024', '24-04-2024', '25-04-2024', '26-04-2024', '29-04-2024', '30-04-2024', '02-05-2024', '03-05-2024', '06-05-2024', '07-05-2024', '08-05-2024', '09-05-2024', '10-05-2024', '13-05-2024', '14-05-2024', '15-05-2024', '16-05-2024', '17-05-2024', '18-05-2024', '21-05-2024', '22-05-2024', '23-05-2024', '24-05-2024', '27-05-2024', '28-05-2024', '29-05-2024', '30-05-2024', '31-05-2024', '03-06-2024', '04-06-2024', '05-06-2024', '06-06-2024', '07-06-2024', '10-06-2024', '11-06-2024', '12-06-2024', '13-06-2024', '14-06-2024', '18-06-2024', '19-06-2024', '20-06-2024', '21-06-2024', '24-06-2024', '25-06-2024', '26-06-2024', '27-06-2024', '28-06-2024', '01-07-2024', '02-07-2024', '03-07-2024', '04-07-2024', '05-07-2024', '08-07-2024', '09-07-2024', '10-07-2024', '11-07-2024', '12-07-2024', '15-07-2024', '16-07-2024', '18-07-2024', '19-07-2024', '22-07-2024', '23-07-2024', '24-07-2024', '25-07-2024', '26-07-2024', '29-07-2024', '30-07-2024', '31-07-2024', '01-08-2024', '02-08-2024', '05-08-2024', '06-08-2024', '07-08-2024', '08-08-2024', '09-08-2024', '12-08-2024', '13-08-2024', '14-08-2024', '16-08-2024', '19-08-2024', '20-08-2024', '21-08-2024', '22-08-2024', '23-08-2024', '26-08-2024', '27-08-2024', '28-08-2024', '29-08-2024', '30-08-2024', '02-09-2024', '03-09-2024', '04-09-2024', '05-09-2024', '06-09-2024', '09-09-2024', '10-09-2024', '11-09-2024', '12-09-2024', '13-09-2024', '16-09-2024', '17-09-2024', '18-09-2024', '19-09-2024', '20-09-2024', '23-09-2024', '24-09-2024', '25-09-2024', '26-09-2024', '27-09-2024', '30-09-2024', '01-10-2024', '03-10-2024', '04-10-2024', '07-10-2024', '08-10-2024', '09-10-2024', '10-10-2024', '11-10-2024', '14-10-2024', '15-10-2024', '16-10-2024', '17-10-2024', '18-10-2024', '21-10-2024', '22-10-2024', '23-10-2024', '24-10-2024', '25-10-2024', '28-10-2024', '29-10-2024', '30-10-2024', '31-10-2024', '01-11-2024', '04-11-2024', '05-11-2024', '06-11-2024', '07-11-2024', '08-11-2024', '11-11-2024', '12-11-2024', '13-11-2024', '14-11-2024', '18-11-2024', '19-11-2024', '21-11-2024', '22-11-2024', '25-11-2024', '26-11-2024', '27-11-2024', '28-11-2024', '29-11-2024', '02-12-2024', '03-12-2024', '04-12-2024', '05-12-2024', '06-12-2024', '09-12-2024', '10-12-2024', '11-12-2024', '12-12-2024', '13-12-2024', '16-12-2024', '17-12-2024', '18-12-2024', '19-12-2024', '20-12-2024', '23-12-2024', '24-12-2024', '26-12-2024', '27-12-2024', '30-12-2024', '31-12-2024',
                            '01-01-2025', '02-01-2025', '03-01-2025', '06-01-2025', '07-01-2025', '08-01-2025', '09-01-2025', '10-01-2025', '13-01-2025', '14-01-2025', '15-01-2025', '16-01-2025', '17-01-2025', '20-01-2025', '21-01-2025', '22-01-2025', '23-01-2025', '24-01-2025', '27-01-2025', '28-01-2025', '29-01-2025', '30-01-2025', '31-01-2025', '01-02-2025', '03-02-2025', '04-02-2025', '05-02-2025', '06-02-2025', '07-02-2025', '10-02-2025', '11-02-2025', '12-02-2025', '13-02-2025', '14-02-2025', '17-02-2025', '18-02-2025', '19-02-2025', '20-02-2025', '21-02-2025', '24-02-2025', '25-02-2025', '27-02-2025', '28-02-2025', '03-03-2025', '04-03-2025', '05-03-2025', '06-03-2025', '07-03-2025', '10-03-2025', '11-03-2025', '12-03-2025', '13-03-2025', '17-03-2025', '18-03-2025', '19-03-2025', '20-03-2025', '21-03-2025', '24-03-2025', '25-03-2025', '26-03-2025', '27-03-2025', '28-03-2025', '01-04-2025', '02-04-2025', '03-04-2025', '04-04-2025', '07-04-2025', '08-04-2025', '09-04-2025', '10-04-2025', '11-04-2025', '15-04-2025', '16-04-2025', '17-04-2025', '21-04-2025', '22-04-2025', '23-04-2025', '24-04-2025', '25-04-2025', '28-04-2025', '29-04-2025', '30-04-2025', '02-01-2025', '09-01-2025', '16-01-2025', '23-01-2025', '30-01-2025', '06-02-2025', '13-02-2025', '20-02-2025', '27-02-2025', '06-03-2025', '13-03-2025', '20-03-2025', '27-03-2025', '03-04-2025', '09-04-2025', '17-04-2025', '24-04-2025', '30-04-2025' ]

Strike_Gep_List          = {"nifty" : 50, "banknifty" : 100, }



# Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip   Extract_Zip
Options_Data = {}
Futures_Data = {}
def Extract_Zip(Expiry_Date, Symbol, Options_Type = "op"):
    global Options_Data, Futures_Data
    # Agar Options ka Data Extract karna ho
    if Options_Type.lower() == "op":
      zip_path = f"/content/drive/MyDrive/Downlod_Options_Data/Options_Chain_Data/{Symbol.lower()}_Options_Chain_Data.zip"
      if Symbol not in Options_Data:
         Options_Data[Symbol] = {}
      target_file = f"{Expiry_Date}.csv"
      with zipfile.ZipFile(zip_path, 'r') as zip_ref:
          csv_files = zip_ref.namelist()
          if target_file in csv_files:
              with zip_ref.open(target_file) as file:
                  data = pd.read_csv(file)
                  data.columns = [col.lower() for col in data.columns]
                  data['datetime'] = pd.to_datetime(data['datetime'], format="%d-%m-%Y %H:%M")
                  data['expiry_date'] = pd.to_datetime(data['expiry_date'], format="%d-%m-%Y")
                  data = data.sort_values(by=['datetime', 'strike_price'], ascending=[True, True] ).reset_index(drop=True)
                  Options_Data[Symbol][Expiry_Date] = data
          else:
              print(f"{target_file} not found in ZIP")
    # Agar Futures ka Data Extract karna ho
    if Options_Type.lower() == "fu":
       if Symbol not in Futures_Data:
          Futures_Data[Symbol] = {}
       zip_path = f"/content/drive/MyDrive/Downlod_Options_Data/Futures/{Symbol.lower()}_Futures.zip"
       with zipfile.ZipFile(zip_path, 'r') as zip_ref:   # ✅ Yaha galti sahi ki hai
            csv_file = [file for file in zip_ref.namelist() if file.startswith(Expiry_Date)]
            if csv_file:
              with zip_ref.open(csv_file[0]) as file:
                    Futures_Data[Symbol][Expiry_Date] = pd.read_csv(file)
            else:
                print(f"❌ No Data Found for {Expiry_Date}")

# # Example usage
# Expiry_Date = '28-01-2021'
# Symbol      = "nifty"    # nifty  banknifty
# Options_Type = "fu"          # "op"  "fu"
# Extract_Zip(Expiry_Date, Symbol, Options_Type)
# if Options_Type.lower() == "op":
#   print(Options_Data)
#   # print(Options_Data[Expiry_Date].head())
# if Options_Type.lower() == "fu":
#   print(Futures_Data)
#   # print(Futures_Data[Expiry_Date].head())
#__________________________________________________________________________________________________________________________________

#  Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data    Read_Strike_Data
def Read_Strike_Data(Symbol, Expiry, Strike, Date_Time="01-01-2000"):
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
          if Symbol not in Options_Data or Expiry not in Options_Data[Symbol]:
             Extract_Zip(Expiry, Symbol, "op")
          Strike_Data = Options_Data[Symbol][Expiry].copy()
          Strike_Data["expiry_date"] = pd.to_datetime(Strike_Data["expiry_date"], format="%d-%m-%Y")
          target_expiry = pd.to_datetime(Expiry, format="%d-%m-%Y")
          filtered_Strike = Strike_Data[ (Strike_Data['expiry_date']  == target_expiry) &
                                        (Strike_Data['strike_price'] == int(Strike))   ].copy()
          Strike_Data = pd.DataFrame(filtered_Strike)
        if int(Strike) == 0 :
           if Symbol not in Futures_Data or Expiry not in Futures_Data[Symbol]:
              Extract_Zip(Expiry, Symbol,"fu")
           Strike_Data = Futures_Data[Symbol][Expiry].copy()
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
# Expiry    = '28-01-2021'
# Strike    =  0  # 13800  30300
# Date_Time = "01-01-2021"
# Symbol    = "banknifty"    # nifty  banknifty
# ATM_Data  = Read_Strike_Data(Symbol, Expiry, Strike, Date_Time)
# print(ATM_Data)
#____________________________________________________________________________________________________________________________________________

# get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep  get_Strike_Gep
def get_Strike_Gep(Symbol):
    global Strike_Gep_List
    try:
       return Strike_Gep_List[Symbol.lower()]
    except Exception as e:
       print(f"get_Strike_Gep Function Error: {e}")
       return None
# Symbol = "nifty"  #  nifty , banknifty
# Strike_Gep = get_Strike_Gep(Symbol)
# print(Strike_Gep)
#_____________________________________________________________________________________________________________________________________________________

# get_Options_Chain   get_Options_Chain   get_Options_Chain   get_Options_Chain   get_Options_Chain   get_Options_Chain   get_Options_Chain
def get_Options_Chain(Symbol, DateTime, Expiry, ATM, Strike_No, Face_values=None, column_Type = "close" ):
    global Options_Data
    try:
        if Symbol not in Options_Data or Expiry not in Options_Data[Symbol]:
           Extract_Zip(Expiry, Symbol, "op")
        DateTime = pd.to_datetime(DateTime, format="%d-%m-%Y %H:%M")
        Strike_Gep = get_Strike_Gep(Symbol)

        Max_Strike = ATM + (Strike_Gep * Strike_No)
        Min_Strike = ATM - (Strike_Gep * Strike_No)
        data = Options_Data[Symbol][Expiry]
        filtered_Time   = data[data['datetime'] == DateTime]
        filtered_Strike = filtered_Time[(filtered_Time['strike_price'] >= Min_Strike) & (filtered_Time['strike_price'] <= Max_Strike)]
        filtered_Strike = filtered_Strike.sort_values(by=['strike_price'], ascending=[True]).reset_index(drop=True)
        filtered_Strike["datetime"]    = filtered_Strike["datetime"].dt.strftime('%d-%m-%Y %H:%M')
        filtered_Strike["expiry_date"] = filtered_Strike["expiry_date"].dt.strftime('%d-%m-%Y')
        Columns           = ["expiry_date", "datetime", "call_volume", "call_oi", f"call_{column_Type}", "strike_price", f"put_{column_Type}", "put_oi", "put_volume"]
        Options_Chain     = filtered_Strike[Columns]
        Total_Call_Volume = filtered_Strike["call_volume"].sum()
        Total_Put_Volume  = filtered_Strike["put_volume"].sum()
        Total_Call_OI     = filtered_Strike["call_oi"].sum()
        Total_Put_OI      = filtered_Strike["put_oi"].sum()
        PCR_Volume        = float(round(Total_Put_Volume / Total_Call_Volume, 2) if Total_Call_Volume != 0 else 0)
        PCR_OI            = float(round(Total_Put_OI / Total_Call_OI, 2) if Total_Call_OI != 0 else 0)

        Atm_Data      = Options_Chain[Options_Chain["strike_price"] == ATM].copy()
        call_price    = float(Atm_Data[f"call_{column_Type}"].iloc[0])
        put_price     = float(Atm_Data[f"put_{column_Type}"].iloc[0])
        Synth_Premium = call_price - put_price
        Synth_Fut     = ATM + Synth_Premium
        Synth_ATM     = round(Synth_Fut / Strike_Gep) * Strike_Gep

        if Face_values is None:
            return {"Options_Chain": Options_Chain, "PCR_Volume": PCR_Volume, "PCR_OI": PCR_OI, "Synth_Fut" : Synth_Fut , "Synth_ATM" : Synth_ATM  }
        else:
            face_val_lower = Face_values.lower()
            if face_val_lower   == "options_chain":
                return Options_Chain
            elif face_val_lower == "pcr_volume":
                return PCR_Volume
            elif face_val_lower == "pcr_oi":
                return PCR_OI
            elif face_val_lower == "pcr":
                return {"PCR_Volume": PCR_Volume, "PCR_OI": PCR_OI,}
            elif face_val_lower == "synth_fut":
                return Synth_Fut
            elif face_val_lower == "synth_atm":
                return Synth_ATM
            else:
                raise ValueError(f"Invalid Face_values parameter: {Face_values}")

    except Exception as e:
           print(f"get_Options_Chain Function Error : {e}")
           return None
# # Example usage:
# Symbol      = "banknifty"              # nifty  banknifty
# DateTime    = "25-01-2024 9:20"
# Expiry      = "25-01-2024"
# ATM         = 44900                # 21300  44900
# Strike_No   = 5
# Face_values = None  # options_chain, pcr_volume, pcr_oi, Synth_Fut, Synth_ATM
# column_Type = "open"  # close
# pcr_data = get_Options_Chain(Symbol, DateTime, Expiry, ATM, Strike_No, Face_values, column_Type)
# print(pcr_data)
# print(tabulate(pcr_data["Options_Chain"], headers="keys", tablefmt="pretty", showindex=False))
#___________________________________________________________________________________________________________________________

# get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data   get_Symbol_Data
def get_Symbol_Data(Symbol, Start_Date, End_Date):
    try:
        Path = f"/content/drive/MyDrive/Downlod_Options_Data/Index/{Symbol}_BackTest_Data.csv"
        Data = pd.read_csv(Path)
        try:
          Start_Date = pd.to_datetime(Start_Date, format="%d-%m-%Y %H:%M")
        except:
          Start_Date = pd.to_datetime(Start_Date, format="%d-%m-%Y")
        try:
          End_Date = pd.to_datetime(End_Date, format="%d-%m-%Y %H:%M")
        except:
          End_Date = pd.to_datetime(End_Date, format="%d-%m-%Y")
        Data["Date_Time"] = pd.to_datetime(Data["Date_Time"], format="%d-%m-%Y %H:%M")
        Data = Data[(Data["Date_Time"] >= Start_Date) & (Data["Date_Time"] <= End_Date)].copy()
        Data.reset_index(drop=True, inplace=True)
        Data["Date_Time"] = Data["Date_Time"].dt.strftime("%d-%m-%Y %H:%M")
        return Data
    except Exception as e:
        print(f"get_Symbol_Data Function Error: {e}")
        return None

# # Example usage:
# Symbol = "banknifty"
# Start_Date = "01-01-2022  09:00"
# End_Date   = "30-04-2025  15:30"
# Symbol_Data = get_Symbol_Data(Symbol, Start_Date, End_Date)
# print(Symbol_Data)
#________________________________________________________________________________________________________________

#  Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate   Brokerage_Calculate
def Brokerage_Calculate(buy_price, sell_price, quantity, Options_Type="OP", Min_Brokerage = 20):
    try:
        turnover = (buy_price + sell_price) * quantity               # **Turnover Calculation**
        if Options_Type.lower() == "fu":  # **Futures Calculation**
            brokerage = min(0.0003 * turnover, Min_Brokerage) * 2    # ₹20 प्रति ऑर्डर, दोनों ओर के लिए ₹40
            stt = 0.0002 * sell_price * quantity                     # 0.02% केवल Sell Side
            transaction_charges = 0.0000183 * turnover               # 0.00183% NSE Transaction Charges
            sebi_charges = (10 / 10000000) * turnover                # ₹10 प्रति करोड़
            stamp_duty = round((0.00002 * buy_price * quantity),0)   # 0.002% (₹200/Crore) on Buy Side
        elif Options_Type.lower() == "call" or Options_Type.lower() == "put" : # **Options Calculation**
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

# # **Example Calculation for Futures**
# futures_result = Brokerage_Calculate(buy_price=25000, sell_price=25000, quantity=300, segment="FU")
# print(f"Futures Charges: {futures_result:.2f}")
# # **Example Calculation for Options**
# options_result = Brokerage_Calculate(buy_price=200, sell_price=200, quantity=300 , segment="OP")
# print(f"Options Charges: {options_result:.2f}")
#_______________________________________________________________________________________________________________________________________________________________

# Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date  Get_BTST_Date
def Get_BTST_Date(Date, Get_Day_No = 1):
    global market_open_dates
    try :
        Date = pd.to_datetime(Date, format="%d-%m-%Y")
        market_open_dates = pd.to_datetime(pd.Series(market_open_dates), format="%d-%m-%Y")
        filtered_dates = market_open_dates[market_open_dates > Date].sort_values()
        filtered_dates = filtered_dates.dt.strftime("%d-%m-%Y").tolist()
        get_Date = filtered_dates[(int(Get_Day_No) - 1)]
        return get_Date
    except Exception as e:
        print(f"Get_BTST_Date Function Error: {e}")
# # Example usage
# Date = "05-01-2025"
# Get_Day_No = 1
# BTST_Date = Get_BTST_Date(Date)
# print(BTST_Date)
#________________________________________________________________________________________________________________________________

# get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice   get_StrikePrice
def get_StrikePrice(Symbol, Options_Type, ATM, Target_Strike, DateTime, Expiry, column_Type = "open", Strike_No = 20,):
    try:
        Strike_Gep = get_Strike_Gep(Symbol)
        Target_Type = type(Target_Strike)
        if Target_Type in [int,float]:
          Face_values = "options_chain"
          DATA = get_Options_Chain(Symbol, DateTime, Expiry, ATM, Strike_No, Face_values, "open")
          Prim_List = DATA[f"{Options_Type.lower()}_{column_Type.lower()}"].tolist() if hasattr(DATA["call_open"], 'tolist') else list(DATA["call_open"])
          nearest_Prim = min(Prim_List, key=lambda x: abs(x - Target_Strike))
          filtered_data = DATA[DATA[f"{Options_Type.lower()}_{column_Type.lower()}"] == nearest_Prim]
          if not filtered_data.empty:
              strike_price =  filtered_data["strike_price"].iloc[0]
              Strike_Data = {"Strike": int(strike_price), "Premium": float(nearest_Prim)}
          else:
                Strike_Data = {"Strike": None, "Premium": None}
          return Strike_Data

        elif Target_Type == str:
          parts = Target_Strike.split('-')
          letters = str(parts[0])
          number = int(parts[1])
          if Options_Type.lower() == "call":
              Value = ATM - (number * Strike_Gep) if letters.lower() == "itm" else ATM + (number * Strike_Gep) if letters.lower() == "otm" else ATM
          elif Options_Type.lower() == "put":
              Value = ATM + (number * Strike_Gep) if letters.lower() == "itm" else ATM - (number * Strike_Gep) if letters.lower() == "otm" else ATM
          return {"Strike": Value, "Premium": None}
    except Exception as e:
        print(f"get_StrikePrice Function Error: {e}")
        return {"Strike": None, "Premium": None}

# Example usage:
# Symbol = "nifty"
# DateTime = "26-12-2024 09:30"
# Expiry = "26-12-2024"
# ATM = 23800
# Options_Type = "call"
# Target_Strike = "ATM-00"  #  "otm-2"
# Strike_Data = get_StrikePrice(Symbol,Options_Type, ATM, Target_Strike, DateTime, Expiry, column_Type = "open", Strike_No = 20, Strike_Gep = 50)
# print(Strike_Data)
#___________________________________________________________________________________________________________________________________________________________________


# calculate_drawdown  calculate_drawdown  calculate_drawdown  calculate_drawdown  calculate_drawdown  calculate_drawdown  calculate_drawdown  calculate_drawdown
def calculate_drawdown(data, trade_no):
    if isinstance(trade_no, str) and trade_no.lower() == "all":
        trade_data = data.copy()
    else:
        trade_data = data[data["Trade_No"] == trade_no].copy()

    trade_data = trade_data.sort_values(by="Entry_DateTime")
    trade_data.reset_index(drop=True, inplace=True)
    drawdown_col = f"Drawdown_{trade_no}"
    trade_data[drawdown_col] = 0.0
    for i in range(1, len(trade_data)):
        running_total = trade_data.loc[i - 1, drawdown_col] + trade_data.loc[i, "PNL"]
        trade_data.loc[i, drawdown_col] = round((running_total if running_total < 0 else 0.0), 2)
    return trade_data[["Trade_No","Entry_DateTime", drawdown_col]]

#  get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data   get_Analysis_Data
def get_Analysis_Data(trade_log):
    try:
        Analysis_Data = pd.DataFrame(trade_log)
        Analysis_Data["Entry_DateTime"] = pd.to_datetime(Analysis_Data["Entry_DateTime"], format="%d-%m-%Y %H:%M")
        Analysis_Data["Exit_DateTime"] = pd.to_datetime(Analysis_Data["Exit_DateTime"], format="%d-%m-%Y %H:%M")
        Analysis_Data.sort_values(by="Entry_DateTime", ascending=True, inplace=True)
        All_drawdown_Data = calculate_drawdown(Analysis_Data, "ALL")
        Analysis_Data = Analysis_Data.merge(All_drawdown_Data,on=['Trade_No', 'Entry_DateTime'], how='left' )
        TradeNo_List = sorted(Analysis_Data["Trade_No"].unique().astype(int))
        for TradeNo in TradeNo_List:
            drawdown_Data = calculate_drawdown(Analysis_Data, TradeNo)
            drawdown_col_name = f"Drawdown_{TradeNo}"
            if drawdown_col_name not in Analysis_Data.columns:
              Analysis_Data = Analysis_Data.merge(drawdown_Data,on=['Trade_No', 'Entry_DateTime'], how='left' )
        drawdown_cols = [f"Drawdown_{no}" for no in TradeNo_List]
        Analysis_Data[drawdown_cols] = Analysis_Data[drawdown_cols].fillna(0)
        Analysis_Data["Month"] = Analysis_Data["Entry_DateTime"].dt.month
        Analysis_Data["Year"] = Analysis_Data["Entry_DateTime"].dt.year
        Analysis_Data["Entry_DateTime"] = pd.to_datetime(Analysis_Data["Entry_DateTime"], format="%d-%m-%Y %H:%M").dt.strftime('%d-%m-%Y %H:%M')
        Analysis_Data["Exit_DateTime"]  = pd.to_datetime(Analysis_Data["Exit_DateTime"], format="%d-%m-%Y %H:%M").dt.strftime('%d-%m-%Y %H:%M')
        return Analysis_Data
    except Exception as e:
        print(f"get_Analysis_Data Function Error : {e}")
        return None
#________________________________________________________________________________________________________________________________________________________________

#  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction  Backtest_Fanfunction
def Backtest_Positional_Function(Trade_No, DATA, Trade_Detail, DateTime_Detail, Tradeing_Time, Exit_Logic, Note1 = None, Note2 = None):
    Trade_List = []

    Options_Type      = Trade_Detail["Options_Type"]
    Transaction_Type  = Trade_Detail["Transaction_Type"]
    Quantity          = Trade_Detail["Quantity"]
    Entry_DateTime    = DateTime_Detail["Entry_DateTime"]
    Exit_DateTime     = DateTime_Detail["Exit_DateTime"]
    Trading_StartTime = Tradeing_Time["Start_Time"]
    Trading_EndTime   = Tradeing_Time["End_Time"]
    Entry_DateTime    = pd.to_datetime(Entry_DateTime, format="%Y-%m-%d %H:%M:%S")
    Entry_Date        = Entry_DateTime.strftime("%d-%m-%Y")
    Entry_Price       = None
    StopLoss_Percent  = Exit_Logic["StopLoss"]
    Target_Percent    = Exit_Logic["Target"]
    TSL_Percent       = Exit_Logic["TSL"]

    StopLoss_condition = ( int(StopLoss_Percent) != 0 )
    Target_condition   = ( int(Target_Percent)   != 0 )
    TSL_condition      = ( int(TSL_Percent)      != 0 )


    Max_ReEntry = int(max(Exit_Logic["Re_Entry"], 1))
    ReEntry = 0

    while ReEntry < Max_ReEntry:
        DATA.columns = [col.lower() for col in DATA.columns]
        DATA['datetime'] = pd.to_datetime(DATA['datetime'], format="%d-%m-%Y %H:%M")
        DATA = DATA[DATA['datetime'] >= Entry_DateTime].copy()
        if Entry_Price is None:
           Entry_Price = DATA[f'{Options_Type.lower()}_open'].iloc[0]    #round(float(Entry_Price),2)

        # Calculate StopLoss, Target, and TSL_Point based on Exit_Logic
        if Transaction_Type.lower() == "sell":
            if StopLoss_condition:
               StopLoss  = round(Entry_Price * (1 + StopLoss_Percent/100), 2)
            if Target_condition:
               Target    = round(Entry_Price * (1 - Target_Percent/100), 2)
            if TSL_condition:
               TSL_Point = round(Entry_Price * (TSL_Percent/100), 2)
        elif Transaction_Type.lower() == "buy":
            if StopLoss_condition:
               StopLoss = round(Entry_Price * (1 - StopLoss_Percent/100), 2)
            if Target_condition:
               Target = round(Entry_Price * (1 + Target_Percent/100), 2)
            if TSL_condition:
               TSL_Point = round(Entry_Price * (TSL_Percent/100), 2)

        if StopLoss_condition:
           Exit_Value = StopLoss
           Exit_Type  = "StopLoss"
        TSL_No     = 1
        Exit_Time  = None

        for i in range(len(DATA)):
            datetime     = pd.to_datetime(str(DATA['datetime'].iloc[i]), format="%Y-%m-%d %H:%M:%S")
            date         = datetime.strftime("%d-%m-%Y")
            time         = datetime.strftime("%H:%M")
            Expiry_Date  = pd.to_datetime(str(DATA['expiry_date'].iloc[i]), format="%d-%m-%Y").strftime("%d-%m-%Y")
            open     = float(DATA[f'{Options_Type}_open' ].iloc[i])
            high     = float(DATA[f'{Options_Type}_high' ].iloc[i])
            low      = float(DATA[f'{Options_Type}_low'  ].iloc[i])
            close    = float(DATA[f'{Options_Type}_close'].iloc[i])
            try:
              Strike_Price = int(DATA['strike_price'].iloc[i])
            except:
              Strike_Price = 0

            Expiry_Exit_Time = pd.to_datetime(Exit_DateTime, format="%d-%m-%Y %H:%M") if Exit_DateTime else pd.to_datetime(f"{Expiry_Date} 15:28", format="%d-%m-%Y %H:%M")
            Trading_Start_Time     = pd.to_datetime(f"{date} {Trading_StartTime}", format="%d-%m-%Y %H:%M")
            Trading_End_Time       = pd.to_datetime(f"{date} {Trading_EndTime}", format="%d-%m-%Y %H:%M")
            Trading_Time_condition = (datetime >= Trading_Start_Time) & (datetime <= Trading_End_Time)


            if Transaction_Type.lower() == "sell":
                exit_condition = (datetime >= Expiry_Exit_Time) or \
                                 (StopLoss_condition and (high >= Exit_Value)) or \
                                 (Target_condition and (low  <= Target))
                TSL_condition  = (TSL_condition and (Exit_Value - (TSL_Point * 2)) >= low)
            elif Transaction_Type.lower() == "buy":
                exit_condition = (datetime >= Expiry_Exit_Time) or \
                                 (StopLoss_condition and (low <= Exit_Value)) or \
                                 (Target_condition and (high >= Target) )
                TSL_condition  = (TSL_condition and (Exit_Value + (TSL_Point * 2)) <= high)

            # print(datetime,TSL_condition)
            if Exit_Time is None and exit_condition and Trading_Time_condition :
                Exit_Time = datetime

                Morning_condition_Target   = ( Exit_Time == Trading_Start_Time ) and (
                                             (Target_condition and Transaction_Type.lower() == "sell" and open <= Target) or
                                             (Target_condition and Transaction_Type.lower() == "buy"  and open >= Target) )

                Morning_condition_StopLoss = ( Exit_Time == Trading_Start_Time ) and (
                                             (StopLoss_condition and Transaction_Type.lower() == "sell" and open >= StopLoss) or
                                             (StopLoss_condition and Transaction_Type.lower() == "buy"  and open <= StopLoss) )

                if Morning_condition_StopLoss:
                    Exit_Value = open
                    Exit_Type  = "Morning_StopLoss"
                elif Morning_condition_Target:
                    Exit_Value = open
                    Exit_Type  = "Morning_Target"

                if not (Morning_condition_StopLoss or Morning_condition_Target):
                   if Target_condition and Transaction_Type.lower() == "sell" and low <= Target:
                      Exit_Type  = "Target"
                      Exit_Value = Target
                   elif Target_condition and Transaction_Type.lower() == "buy" and high >= Target:
                      Exit_Type  = "Target"
                      Exit_Value = Target

                if datetime == Expiry_Exit_Time:
                    Exit_Type = "DateTime"
                    Exit_Value = close
                    if Exit_Time == pd.to_datetime(f"{Expiry_Date} 15:25", format="%d-%m-%Y %H:%M"):
                       Exit_Type = "Expiry"

                if Entry_Price is not None and Exit_Value is not None:
                    if Transaction_Type.lower() == "buy":
                        Net_PNL = round((float(Exit_Value) - float(Entry_Price)) * Quantity, 2)
                        Brokerage = Brokerage_Calculate(float(Entry_Price), float(Exit_Value), Quantity, Options_Type)
                    elif Transaction_Type.lower() == "sell":
                        Net_PNL = round((float(Entry_Price) - float(Exit_Value)) * Quantity, 2)
                        Brokerage = Brokerage_Calculate(float(Exit_Value), float(Entry_Price), Quantity, Options_Type)
                    else:
                        raise ValueError("Invalid Transaction_Type. Use 'buy' or 'sell'.")

                PNL = round(Net_PNL - Brokerage, 2)


                Trade_Data = {"Trade_No" : Trade_No, "Expiry_Date" : Expiry_Date, "Strike" : Strike_Price,"Options_Type" : Options_Type, "Transaction_Type": Transaction_Type,
                              "Entry_DateTime" : Entry_DateTime.strftime("%d-%m-%Y %H:%M"), "Exit_DateTime" : datetime.strftime("%d-%m-%Y %H:%M"),
                              "Entry_Price" : round(Entry_Price,2), "Exit_Price" : round(Exit_Value,2), "Quantity" : int(Quantity), "Net_PNL" : round(Net_PNL,2),
                              "Brokerage" : round(Brokerage,2), "PNL" : round(PNL,2), "Note1" : Exit_Type, "Note2": Note2 }

                Trade_List.append(Trade_Data)
                break  # Exit the loop as trade is closed

            elif TSL_condition:
                if Transaction_Type.lower() == "sell":
                    Exit_Value = round(Exit_Value - TSL_Point, 2)
                elif Transaction_Type.lower() == "buy":
                    Exit_Value = round(Exit_Value + TSL_Point, 2)
                Exit_Type = f"TSL_{TSL_No}"
                TSL_No += 1

        # Re-entry logic after exit
        if Trade_List:
           last_trade = Trade_List[-1]
           Re_Entry_DateTime = pd.to_datetime(last_trade["Exit_DateTime"], format="%d-%m-%Y %H:%M")
           Re_Entry_EndTime  = pd.to_datetime(f"{Entry_Date} 15:30", format="%d-%m-%Y %H:%M")

           if Re_Entry_DateTime.strftime("%d-%m-%Y") == Entry_Date:
              DATA_reentry = DATA[(DATA['datetime'] > Re_Entry_DateTime) & (DATA['datetime'] <= Re_Entry_EndTime)]
              for i in range(len(DATA_reentry)):
                  Re_high = DATA_reentry[f'{Options_Type}_high'].iloc[i]
                  Re_low = DATA_reentry[f'{Options_Type}_low'].iloc[i]
                  Re_datetime = DATA_reentry['datetime'].iloc[i]

                    # Check if price crosses original entry price
                  if (Transaction_Type == "sell" and Re_high >= Entry_Price and Re_low  <= Entry_Price) or \
                     (Transaction_Type == "buy"  and Re_low  <= Entry_Price and Re_high >= Entry_Price) :
                     Entry_DateTime = Re_datetime
                     ReEntry += 1
                     break
                  elif Re_datetime == Re_Entry_EndTime:
                       ReEntry = Max_ReEntry
                       break
              else:
                  ReEntry = Max_ReEntry
           else:
               ReEntry = Max_ReEntry
        else:
            ReEntry = Max_ReEntry

    return Trade_List
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi   Heikin_Ashi  
def get_Heikin_Ashi(prev_ha_open, prev_ha_close, current_open, current_high, current_low, current_close):
    try:
        def custom_round(num, decimals):
            return Decimal(str(num)).quantize(Decimal(f'1.{"0" * decimals}'), rounding=ROUND_HALF_UP)
        ha_close = custom_round((Decimal(current_open) + Decimal(current_high)  + Decimal(current_low)  + Decimal(current_close) ) / 4, 2)
        ha_open  = custom_round((Decimal(prev_ha_open) + Decimal(prev_ha_close)) / 2, 2)
        ha_high  = custom_round(max(Decimal(current_high), ha_open, ha_close), 2)
        ha_low   = custom_round(min(Decimal(current_low), ha_open, ha_close), 2)
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
# Heikin_Ashi = Heikin_Ashi(prev_ha_open, prev_ha_close, current_open, current_high, current_low, current_close)
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
def get_Candle_Price(DATA, DateTime, Round_Minute):
    try:
      DATA = pd.DataFrame(DATA)
      DATA.columns = [col.lower() for col in DATA.columns]
      Candle_time_Data   = get_Candle_time(DateTime, Round_Minute)
      current_open_Time  = pd.to_datetime(Candle_time_Data["current_Candle"]["open_time"], format="%d-%m-%Y %H:%M")
      current_close_Time = pd.to_datetime(Candle_time_Data["current_Candle"]["close_time"], format="%d-%m-%Y %H:%M")
      prev_open_Time     = pd.to_datetime(Candle_time_Data["prev_Candle"]["open_time"], format="%d-%m-%Y %H:%M")
      prev_close_Time    = pd.to_datetime(Candle_time_Data["prev_Candle"]["close_time"], format="%d-%m-%Y %H:%M")
      current_data = DATA[(DATA['datetime'] >= current_open_Time) & (DATA['datetime'] <= current_close_Time)].copy()
      current_data.reset_index(drop=True, inplace=True)
      if len(current_data) != 0:
        current_Data = {"open" : float(current_data['fu_open'].iloc[0]), "high" : float(current_data['fu_high'].max()),
                        "low" : float(current_data['fu_low'].min()), "close" : float(current_data['fu_close'].iloc[-1])}
      else:
        current_Data = {"open" : None, "high" : None, "low" : None, "close" : None}
      prev_data = DATA[(DATA['datetime'] >= prev_open_Time) & (DATA['datetime'] <= prev_close_Time)].copy()
      prev_data.reset_index(drop=True, inplace=True)
      if len(prev_data) != 0:
        prev_Data  = {"open" : float(prev_data['fu_open'].iloc[0]), "high" : float(prev_data['fu_high'].max()),
                      "low" : float(prev_data['fu_low'].min()), "close" : float(prev_data['fu_close'].iloc[-1])}
      else:
        prev_Data  = {"open" : None, "high" : None, "low" : None, "close" : None}
      return {"current_Data" : current_Data, "prev_Data" : prev_Data }
    except Exception as e:
      print(f"Candle_Price Function Error : {e}")
      return None

# Example usage
# DATA = Data.copy()
# DateTime = "01-04-2025 09:05"
# Round_Minute = 5
# Candle_Price_Data = Candle_Price(DATA, DateTime, Round_Minute)
# current_Data = Candle_Price_Data["current_Data"]
# prev_Data = Candle_Price_Data["prev_Data"]
# print(current_Data)
# print(prev_Data)
#________________________________________________________________________________________________________________________
# get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns    get_HeikinAshi_Columns   
def get_HeikinAshi_Columns(DATA, Round_Minute):
    try:
        ha_open_list = []
        ha_high_list = []
        ha_low_list = []
        ha_close_list = []
        ha_color_list = []
        prev_ha_open = None
        prev_ha_close = None

        for i in range(len(DATA)):
            DateTime = pd.to_datetime(DATA["datetime"].iloc[i], format="%d-%m-%Y %H:%M").strftime("%d-%m-%Y %H:%M")
            Candle_Price_Data = get_Candle_Price(DATA, DateTime, Round_Minute)
            try:
                if prev_ha_open is None or prev_ha_close is None:
                  prev_ha_open  = Candle_Price_Data["prev_Data"]["open"]
                  prev_ha_close = Candle_Price_Data["prev_Data"]["close"]
                current_open     = Candle_Price_Data["current_Data"]["open"]
                current_high     = Candle_Price_Data["current_Data"]["high"]
                current_low      = Candle_Price_Data["current_Data"]["low"]
                current_close    = Candle_Price_Data["current_Data"]["close"]

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

        # Add Heikin-Ashi columns to the DataFrame
        DATA[f"ha_{Round_Minute}_open"] = ha_open_list
        DATA[f"ha_{Round_Minute}_high"] = ha_high_list
        DATA[f"ha_{Round_Minute}_low"] = ha_low_list
        DATA[f"ha_{Round_Minute}_close"] = ha_close_list
        DATA[f"ha_{Round_Minute}_color"] = ha_color_list
        return DATA
    except Exception as e:
        print(f"get_HeikinAshi_Columns Function Error : {e}")
        return None

# Example usage
# DATA = Data.copy()
# Round_Minute = 5
# Datas = get_HeikinAshi_Columns(DATA, Round_Minute)
# print(tabulate(Datas, headers="keys", tablefmt="pretty", showindex=False))
#_________________________________________________________________________________________________________________






