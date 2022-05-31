class FuncionesFiltro:
    
    @classmethod    
    def  filtroCS(cls,comandoShRun):
        busquedaCS =  ["6888","66882","6926","7860","6695","6687","6689","6696","100000","10000","7880","7879","66678","717020","6688","7806","6691"]
        for litadoBusqueda in busquedaCS:
            filtroCS = [s for s in comandoShRun if litadoBusqueda in s]
            
            if len(filtroCS)>0:
                filtroListaCS=filtroCS[0].split(' ')
                filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split(':')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]  
                if len(filtroCS)<10:
                    filtroListaCS=filtroCS[0].split('_')
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s] 
                else:
                    datos=filtroCS
                    return datos
                return filtroCS[0]
              
        
    @classmethod
    def  filtroOTT(cls,comandoShRun):
        busquedaOTT = ["71701","712008","7200","7210","7180","7170","7190", "717020", "7160" ,"7150"]
        for litadoBusqueda in busquedaOTT:
            filtroOTT = [s for s in comandoShRun if litadoBusqueda in s]
            
            if len(filtroOTT)>0:
                filtroListaOTT=filtroOTT[0].split(' ')
                filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split(':')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]  
                if len(filtroOTT)<10:
                    filtroListaOTT=filtroOTT[0].split('_')
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s] 
                else:
                    datos=filtroOTT
                    return datos
                return filtroOTT[0]
