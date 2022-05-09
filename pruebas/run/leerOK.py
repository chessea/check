import openpyxl
import pandas as pd
''' 
input_file = 'datos.txt'

wb= openpyxl.Workbook()
ws = wb.worksheets[0] '''

df = pd.read_csv('datos.txt', sep='\t')
datos=df.values.tolist()
lista=[datos]


contador=2
for d in lista:
    for t in d:
        for a in t:
            print(a)
    

    #df.to_excel('output.xlsx', 'Sheet1', index=False)
            contador=contador+1
            print(contador)
            book =openpyxl.load_workbook('d.xlsx')
            sheet = book['configuracion']
            sheet['A'+str(contador)]=a
            book.save('d.xlsx')
  