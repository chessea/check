class User:
    def __init__(self, nombreITP, usuarioServ, passwordServ):
        self._nombreITP = nombreITP
        self._usuarioServ = usuarioServ
        self._passwordServ = passwordServ
    def __str__(self):
        return f'User: {self._nombreITP}, {self._usuarioServ}, {self._passwordServ}'
        
    @property
    def nombreITP(self):
        return self._nombreITP

    @nombreITP.setter
    def nombreITP(self, nombreITP):
        self._nombreITP = nombreITP      
    
    @property
    def usuarioServ(self):
        return self._usuarioServ
    
    @usuarioServ.setter
    def usuarioServ(self, usuarioServ):
        self._usuarioServ = usuarioServ    
    
    @property
    def passwordServ(self):
        return self.passwordServ
    
    @passwordServ.setter
    def passwordServ(self, passwordServ):
        self._passwordServ = passwordServ        