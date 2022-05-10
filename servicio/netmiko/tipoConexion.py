class TipoConexion:
    
    @classmethod
    def conexionTelnet(cls,ip):
        
        cisco_router_telnet = {
            'device_type': 'cisco_ios_telnet',
            'host': ip,
            'username': 'franco',
            'password': 'cisco',
            'port': 23
        }    
        return  cisco_router_telnet  
    
    
    
    @classmethod
    def conexionSSH(cls, ip):
      
        cisco_router_ssh = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': 'franco',
            'password': 'cisco',
            'port': 22
        }    
        return  cisco_router_ssh