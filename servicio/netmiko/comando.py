import netmiko

from servicio.netmiko.tipoConexion import TipoConexion



class Comando:
    @classmethod
    def enviarComando(cls,comando,ip):
    
        try:
            cisco_router_telnet=TipoConexion.conexionTelnet(ip)
            ssh = netmiko.ConnectHandler(**cisco_router_telnet)
            ssh.enable()
            result = ssh.send_command(comando, delay_factor=2)
            comandoList=result.split('\n')
            ssh.exit_enable_mode()
            print("CONEXION TELNET OK")
            return comandoList
        except Exception as e:  
            print("ERROR TELNET")   
        try:
            cisco_router_ssh=TipoConexion.conexionSSH(ip)
            ssh = netmiko.ConnectHandler(**cisco_router_ssh)
            ssh.enable()
            result = ssh.send_command(comando,delay_factor=1)
            comandoList=result.split('\n')
            ssh.disconnect()
          
            print("CONEXION SSH OK")
            return comandoList
        except Exception as e:
                print("ERROR SSH")
