class Snmp:
    def __init__(self, versionSNMP, comunidad, encripSNMP,passwordSNMP):
    
        self._versionSNMP = versionSNMP
        self._comunidad= comunidad
        self._encripSNMP = encripSNMP
        self._passwordSNMP = passwordSNMP
    
    
    def __str__(self):
            return f'SNMP { self._versionSNMP}, {self._comunidad}, { self._encripSNMP}, {self._passwordSNMP}'    


    @property
    def versionSNMP(self):
        return self._versionSNMP

    @versionSNMP.setter
    def vrf(self, versionSNMP):
        self._versionSNMP= versionSNMP      
        
    @property
    def comunidad(self):
        return self.comunidad

    @comunidad.setter
    def comunidad(self, comunidad):
        self._comunidad= comunidad    
     
    @property
    def encripSNMP(self):
        return self.encripSNMP

    @encripSNMP.setter
    def vrf(self, encripSNMP):
        self._encripSNMP= encripSNMP       
        
    @property
    def passwordSNMP(self):
        return self.passwordSNMP

    @passwordSNMP.setter
    def vrf(self, passwordSNMP):
        self._passwordSNMP= passwordSNMP        
        