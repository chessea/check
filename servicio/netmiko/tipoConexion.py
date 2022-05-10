class TipoConexion:
        
    
    @classmethod
    def conexionTelnet(cls,ip, x , y):
       
        
        cisco_router_telnet = {
            'device_type': 'cisco_ios_telnet',
            'host': ip,
            'username': x,
            'password': y,
            'port': 23
        }    
        return  cisco_router_telnet  
    
    
    
    @classmethod
    def conexionSSH(cls, ip, x , y):
    
        cisco_router_ssh = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': x,
            'password': y,
            'port': 22
        }    
        return  cisco_router_ssh