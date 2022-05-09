from openpyxl import Workbook
from openpyxl.styles import Font
import time



book = Workbook()
sheet= book.active
sheet['A1']=2
sheet['A2']=3

sheet2= book.create_sheet('hoja2')
sheet2['A1']=2
sheet2['A2']=3
fecha= time.strftime('%x')
sheet2['A3']=fecha


book.save('prueba.xlsx')


