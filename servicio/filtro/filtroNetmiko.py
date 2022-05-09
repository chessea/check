import os

from servicio.filtro.funcionesFiltros import FuncionesFiltro


class FiltroNetmiko:
    
    @classmethod
    def obtenerCSOTT(cls,comandoShRun):
     
        lista = []
        cs=FuncionesFiltro.filtroCS(comandoShRun)
        ott=FuncionesFiltro.filtroOTT(comandoShRun)   
        #interface=FuncionesFiltro.filtroInterface(comandoShRun) 
   
        lista.append(ott)
        lista.append(cs)
      #  lista.append(interface)
        #lista.append(filtroMonitoreo[0])
        #lista.append(filtroInterface[0])
       
        return lista
            
    @classmethod
    def obtenerHostName(cls, comandoShRun):
        hostname=comandoShRun[0].split(' ')
        del(hostname[0])
        if len(hostname)>0:
            return hostname[0]
        else:
            return 'Sin Datos'
     
     
    @classmethod
    def obtenerModelo(cls, comoandoModelo):
        modelo=comoandoModelo[0].split(' ')
        if len(modelo)>0:
            return modelo[4]
        else:
            return 'Sin Datos'
    
    @classmethod
    def obtenerSNMP(cls, comandoSnmp):
        snmp=comandoSnmp[0].split(' ')
        if len(snmp)>0:
            return snmp[2]
        else:
            return 'Sin Datos'    
        
    @classmethod
    def  filtroInterface(cls,comandoShRun):
        busquedaINT = ["0/0/0","0/0","0/4"]
        for litadoBusqueda in busquedaINT:
            filtroINT = [s for s in comandoShRun if litadoBusqueda in s]
            if filtroINT==[]:
                pass
            else:    
                filtroListaINT=filtroINT[0].split('_')
                if filtroListaINT != []:
                    filtroINT = [s for s in filtroListaINT if litadoBusqueda in s]
                if len(filtroINT)==1:
                    break  
        if filtroINT==[]:
            return "Sin datos"         
        return filtroINT[0]         
             
if __name__ == '__main__':
    FiltroNetmiko.obtenerCSOTT()
     
    
    