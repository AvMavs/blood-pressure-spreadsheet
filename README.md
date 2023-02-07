# blood-pressure-spreadsheet
A script to convert OfflineBPLog CSVs to Spreadsheets.

## Steps to use this script
- You must have python installed on your computer. (https://www.python.org/downloads/)
- Download `pandas`. You can do this by running the command `pip install pandas`
- Download the given python file.
- Make another file called `data.csv` in the same folder.
- Paste the CSV data exported from the app. You do not have to include the apostrophe or headers.
- Open the directory in which the file is located in your CLI client of choice.
- Run `python bp.py`
- When you run the script, it will automatically generate a `spreadsheet.xlsx` with the data neatly categorised into Date/Time/Systiolic/Diastolic/Pulse/Remarks columns. 

####### Note: This program converts dates from the ISO8601 standard to the DD-MM-YYYY and HH-MM-SS standards to make it easy for doctors to read.
