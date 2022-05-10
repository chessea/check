class FuncionesFiltro:
    
    @classmethod    
    def  filtroCS(cls,comandoShRun):
        busquedaCS =  ["1000","7880","7879"]
        for litadoBusqueda in busquedaCS:
            filtroCS = [s for s in comandoShRun if litadoBusqueda in s]
            if filtroCS==[]:
                pass
            else:    
                filtroListaCS=filtroCS[0].split('_')
                if filtroListaCS != []:
                    filtroCS = [s for s in filtroListaCS if litadoBusqueda in s]
                if len(filtroCS)==1:
                    break  
        if filtroCS==[]:
            filtroCS = "Sin Datos"
            return filtroCS       
        return filtroCS[0]                    
        
    @classmethod
    def  filtroOTT(cls,comandoShRun):
        busquedaOTT = ["7200","7210","7180","7190", "7170", "7160" ,"7150"]
        for litadoBusqueda in busquedaOTT:
            filtroOTT = [s for s in comandoShRun if litadoBusqueda in s]
            if filtroOTT==[]:
                pass
            else:    
                filtroListaOTT=filtroOTT[0].split('_')
                if filtroListaOTT != []:
                    filtroOTT = [s for s in filtroListaOTT if litadoBusqueda in s]
                if len(filtroOTT)==1:
                    break  
        if filtroOTT==[]:
            filtroOTT = "Sin Datos"
            return filtroOTT      
        return filtroOTT[0]         
        
        
