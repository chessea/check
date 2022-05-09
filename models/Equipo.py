class Equipo:
    
    def __init__(self,tipoEquipo,tipoEnlace,  equipoMinsal,hostname,rotuloMinsal,marca, modelo,stack, core  ):
        self._tipoEquipo = tipoEquipo
        self._tipoEnlace = tipoEnlace
        self._equipoMinsal = equipoMinsal
        self._hostname = hostname
        self._rotuloMinsal = rotuloMinsal
        self._core = core
        self._stack = stack
        self._marca = marca
        self._modelo= modelo
        
        
    def __str__(self):
        return f'DatosCkecklist { self._tipoEquipo},{self._tipoEnlace}, {self._equipoMinsal}, {self._hostname}, {self._rotuloMinsal}, {self._core}, {self._stack}, {self._marca}, {self._modelo}'    

    @property
    def tipoEquipo(self):
        return self._tipoEquipo

    @tipoEquipo.setter
    def tipoEquipo(self, tipoEquipo):
        self._tipoEquipo = tipoEquipo         
    
    @property
    def tipoEnlace(self):
        return self._tipoEnlace

    @tipoEnlace.setter
    def tipoEnlace(self, tipoEnlace):
        self._tipoEnlace = tipoEnlace                               
        
    @property
    def equipoMinsal(self):
        return self._equipoMinsal

    @equipoMinsal.setter
    def equipoMinsal(self, equipoMinsal):
        self._equipoMinsal = equipoMinsal         
    
    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname      
    
    @property
    def rotuloMinsal(self):
        return self._rotuloMinsal

    @rotuloMinsal.setter
    def rotuloMinsal(self, rotuloMinsal):
        self._rotuloMinsal = rotuloMinsal  
    
    @property
    def core(self):
        return self._core

    @core.setter
    def core(self, core):
        self._core = core        
     
    @property
    def stack(self):
        return self._stack

    @stack.setter
    def stack(self, stack):
        self._stack = stack      
     
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def vmarcaf(self, marca):
        self._marca= marca         
     
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._marca= modelo          