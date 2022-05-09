import pandas as pd
import openpyxl



df = pd.read_fwf(
    'datos.txt', sep='\t',header=None)
print(df)




''' df = pd.read_csv('datos.txt', sep='\t')
df.to_excel('dat.xlsx', 'Sheet1',index=False,header=False,startrow=5) '''






