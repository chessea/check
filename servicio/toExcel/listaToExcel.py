import openpyxl

class ListaToExcel:
    
    @classmethod
    def datosToExcel(cls,lista):
        book =openpyxl.load_workbook('/home/fr/Documentos/pythonEntel/servicio/store/datos.xlsx')
        sheet = book['encabezado']
        sheet['B3']=lista[0]
        sheet['B4']=lista[1]
        sheet['B11']=lista[2]
        sheet['B17']=lista[3]
        sheet['B22']=lista[4]
        sheet['B19']=lista[5]
        sheet['B23']=lista[6]
        print('FIN ENCABEZADO')
        
        
        x= range(0,len(lista[7]))
        contador=3
        for todos in x:
            contador=contador+1
            sheet2 = book['interfaces']
            sheet2[f'A{contador}']=lista[7][todos]
        print('FIN BRIEF') 
        
        
        y= range(0,len(lista[8]))
        contador=3
        for todos2 in y:
            contador=contador+1
            sheet3 = book['configuracion']
            sheet3[f'I{contador}']=lista[8][todos2]
        print('FIN VERSION')   
        
        
        x= range(0,len(lista[9]))
        contador=3
        for todos3 in x:
            contador=contador+1
            sheet3[f'A{contador}']=lista[9][todos3]
        book.save(f'/home/fr/Documentos/pythonEntel/servicio/store/check/CHECKLIST_ITP_{lista[0]}_{lista[1]}_{lista[2]}.xlsx')
        print('FIN SH RUN') 