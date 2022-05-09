import os

class FiltroDatos:
 
    ruta_archivo = "datos.txt"
    @classmethod
    def obtenerCSOTT(cls):
        lista = []
        busquedaCS = "10000"
        busquedaOTT = "7210"
        BuquedaInterface= "0/0/0"
        busquedaMonitoreo='10.2'
        with open( cls.ruta_archivo, 'r', encoding="ASCII" ) as datos:
            datosLista = datos.read().split(' ')
            
            filtroCS = [s for s in datosLista if busquedaCS in s]
            filtroListaCS=filtroCS[0].split('_')
            filtroCS = [s for s in filtroListaCS if busquedaCS in s]
     
            filtroOTT= [s for s in datosLista if busquedaOTT in s]
            filtroListaOTT=filtroOTT[0].split(':')
            filtroOTT= [s for s in filtroListaOTT if busquedaOTT in s]
                    
            filtroInterface= [s for s in datosLista if BuquedaInterface in s]
            filtroListaINT=filtroInterface[0].split(' ')
            filtroInterface= [s for s in filtroListaINT if BuquedaInterface in s]      
            
            filtroMonitoreo= [s for s in datosLista if busquedaMonitoreo in s]
            filtroListaMON=filtroMonitoreo[0].split(' ')
            filtroMonitoreo= [s for s in filtroListaMON if busquedaMonitoreo in s]
                   
            lista.append(filtroOTT[0])
            lista.append(filtroCS[0])
            lista.append(filtroMonitoreo[0])
            lista.append(filtroInterface[0])
                        
            return lista
            
        
if __name__ == '__main__':
    FiltroDatos.obtenerCSOTT()
     
    
    