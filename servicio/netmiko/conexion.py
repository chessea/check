import netmiko

from tipoConexion import TipoConexion


class Comando:
    @classmethod
    def enviarComando(cls,comando):
    
        try:
            cisco_router_telnet=TipoConexion.conexionTelnet()
            ssh = netmiko.ConnectHandler(**cisco_router_telnet)
            ssh.enable()
            result = ssh.send_command(comando)
            comandoList=result.split('\n')
            ssh.exit_enable_mode()
            print("CONEXION TELNET OK")
            return comandoList
        except Exception as e:     
            try:
                cisco_router_ssh=TipoConexion.conexionSSH()
                ssh = netmiko.ConnectHandler(**cisco_router_ssh)
                ssh.enable()
                result = ssh.send_command(comando)
                comandoList=result.split('\n')
                ssh.exit_enable_mode()
                print("CONEXION SSH OK")
                return comandoList
            except Exception as e:
                print(f"Error de conexion {e}")
if __name__ == '__main__':
    print(Comando.enviarComando("sh ip int brief"))