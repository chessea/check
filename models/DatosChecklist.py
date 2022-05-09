
class DatosChecklist:
    
    def __init__(self, ott,cs, ipMonitoreo,interfaceMonitoreo1,interfaceMonitoreo2, vrf):
        
        self._ott = ott
        self._cs = cs
        self._vrf = vrf
        self._ipMonitoreo = ipMonitoreo
        self._interfaceMonitoreo1 = interfaceMonitoreo1
        self._interfaceMonitoreo2 = interfaceMonitoreo2
        
    
    def __str__(self):
        return f'DatosCkecklist: {self._ott}, {self._cs},  {self._ipMonitoreo}, {self._interfaceMonitoreo1},{self._interfaceMonitoreo2}, {self._vrf}'
    
    
    
    @property
    def ott(self):
        return self._ott

    @ott.setter
    def ott(self, ott):
        self._ott= ott       
    
    @property
    def cs(self):
        return self._cs

    @cs.setter
    def cs(self, cs):
        self._cs= cs                                  
                            
    @property
    def vrf(self):
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        self._vrf = vrf        
     
    @property
    def ipMonitoreo(self):
        return self.ipMonitoreo

    @ipMonitoreo.setter
    def ipMonitoreo(self, ipMonitoreo):
        self._ipMonitoreo= ipMonitoreo        
    
    @property
    def interfaceMonitoreo1(self):
        return self.interfaceMonitoreo1

    @interfaceMonitoreo1.setter
    def vrf(self, interfaceMonitoreo1):
        self._interfaceMonitoreo1= interfaceMonitoreo1        
    
    @property
    def interfaceMonitoreo2(self):
        return self.interfaceMonitoreo2

    @interfaceMonitoreo2.setter
    def vrf(self, interfaceMonitoreo2):
        self._interfaceMonitoreo2= interfaceMonitoreo2      