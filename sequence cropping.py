import pandas as pd
import xlrd

xls = pd.read_csv('D:\Code Templates\Python Templates\Bioinformatics-Assignement\protein_tables.csv')
# print(xls)

# df1 = pd.read_excel(xls, 'DataPirates')

# pd.ExcelFile

for index, row in xls.iterrows():
    print(row['Species'])