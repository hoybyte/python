import pandas as pd
import os
import openpyxl
from pandas import ExcelWriter

os.chdir('C:\\Backup\\New Folder')
excel_file_path = 'Test.xlsx'

df = pd.read_excel(excel_file_path)
#print(df)

df['Pickup Location'] = df['Pickup Location'].str.lower()
df['Pickup Location'] = df['Pickup Location'].str.rstrip()
#print(df['Pickup Location'])

split_values = df['Pickup Location'].unique()
#print(split_values)

for value in split_values:
    df1 = df[df['Pickup Location'] == value]
    output_file_name = str(value) + ".xlsx"
    df1.to_excel(output_file_name, index=False)