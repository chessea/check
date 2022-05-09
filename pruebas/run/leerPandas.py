import openpyxl
import pandas as pd

df = pd.read_csv('datos.txt', sep='\t')
datos=df.values.tolist()

x= range(0,len(datos))
contador=3
 



for todos in x:
    contador=contador+1
    book =openpyxl.load_workbook('d.xlsx')
    sheet = book['configuracion']
    sheet['A'+str(contador)]=datos[todos][0]
    book.save('d.xlsx')
print('FIN') 