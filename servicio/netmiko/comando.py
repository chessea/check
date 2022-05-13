import netmiko

from servicio.netmiko.tipoConexion import TipoConexion



class Comando:
    @classmethod
    def enviarComando(cls,comando,ip, x , y ):
        lista= []
        try:
            cisco_router_telnet=TipoConexion.conexionTelnet(ip, x ,y)
            ssh = netmiko.ConnectHandler(**cisco_router_telnet)
            ssh.enable()
            
            shRun = ssh.send_command(comando[0], delay_factor=2)
            comandoListShRun=shRun.split('\n')
            shbrief = ssh.send_command(comando[1], delay_factor=2)
            comandoListBrief=shbrief.split('\n')
            shVer = ssh.send_command(comando[2], delay_factor=2)
            comandoListVer=shVer.split('\n')
            shHostname = ssh.send_command(comando[3], delay_factor=2)
            comandoLisHostname=shHostname.split('\n')
            shModel = ssh.send_command(comando[4], delay_factor=2)
            comandoListModel=shModel.split('\n')
            shSnmp = ssh.send_command(comando[5], delay_factor=2)
            comandoListSNMP=shSnmp.split('\n')
            
            ssh.exit_enable_mode()
            print(f"CONEXION TELNET OK {ip}")
            lista.append(comandoListShRun)
            lista.append(comandoListBrief)
            lista.append(comandoListVer)
            lista.append(comandoLisHostname)
            lista.append(comandoListModel)
            lista.append(comandoListSNMP)
            
            return lista
        except Exception as e:  
            print(f"ERROR TELNET {ip}")   
            try:
                cisco_router_ssh=TipoConexion.conexionSSH(ip , x ,y)
                ssh = netmiko.ConnectHandler(**cisco_router_ssh)
                ssh.enable()
                
                shRun = ssh.send_command(comando[0], delay_factor=2)
                comandoListShRun=shRun.split('\n')
                shbrief = ssh.send_command(comando[1], delay_factor=2)
                comandoListBrief=shbrief.split('\n')
                shVer = ssh.send_command(comando[2], delay_factor=2)
                comandoListVer=shVer.split('\n')
                shHostname = ssh.send_command(comando[3], delay_factor=2)
                comandoLisHostname=shHostname.split('\n')
                shModel = ssh.send_command(comando[4], delay_factor=2)
                comandoListModel=shModel.split('\n')
                shSnmp = ssh.send_command(comando[5], delay_factor=2)
                comandoListSNMP=shSnmp.split('\n')
                
                ssh.disconnect()
                print(f"CONEXION SSH OK {ip}")
                
                lista.append(comandoListShRun)
                lista.append(comandoListBrief)
                lista.append(comandoListVer)
                lista.append(comandoLisHostname)
                lista.append(comandoListModel)
                lista.append(comandoListSNMP)
                
                return lista
            except Exception as e:
                    print("ERROR SSH {ip}")
