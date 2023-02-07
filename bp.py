import pandas as pd

def csv_to_spreadsheet(csv_data):
    df = pd.read_csv(csv_data, header=None, names=['Date_Time', 'Systolic', 'Diastolic', 'Pulse', 'Remarks'], 
                     parse_dates=['Date_Time'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%dT%H:%M:%S.%fZ'))
    df['Date'] = df['Date_Time'].dt.strftime('%d-%m-%Y')
    df['Time'] = df['Date_Time'].dt.strftime('%H:%M:%S')
    df.drop('Date_Time', axis=1, inplace=True)
    df = df[['Date', 'Time', 'Systolic', 'Diastolic', 'Pulse', 'Remarks']]
    return df

csv_data = "data.csv"
df = csv_to_spreadsheet(csv_data)
df.to_excel("spreadsheet.xlsx", index=False)
