from time import time
from models.DatosChecklist import DatosChecklist
from models.User import User
from models.Equipo import Equipo

from servicio.netmiko.comando import Comando
from servicio.toExcel.listaToExcel import  ListaToExcel
from servicio.filtro.filtroNetmiko import  FiltroNetmiko
from bullet import VerticalPrompt, Input, Password



print("Inicio")
cli= VerticalPrompt([
    Input(prompt="Ingrese usuario: "),
    Password(prompt="Ingrese password : ", hidden="*")],spacing=0)
result=cli.launch()

x=result[0][1]
y=result[1][1]


with open("/home/Python/Test/CAJ-telnet-hosts", "r") as datos:
    valores=[]
    for ip in datos:
      valores.append(ip)
       


#listaIp=[ "10.252.127.126", "10.236.15.134","10.236.94.86", "10.236.15.46","10.235.233.30","10.235.230.222","10.234.47.230"]

for ip in valores:
    try:
    
        listaComandos=['sh run | exclude !', 
                       'sh ip int brief',
                       'sh ver', 
                       'sh run | include hostname',
                       'sh inventory | include "Chassis|chassis"',
                       "sh run | include snmp-server community"]
    
        comandos=Comando.enviarComando(listaComandos,ip,x,y)
    

        shRun, brief, shVer, shRunHost, shModel, snmpcomando = comandos

        lista=FiltroNetmiko.obtenerCSOTT(shRun)
        hostname=FiltroNetmiko.obtenerHostName(shRunHost)
        model=FiltroNetmiko.obtenerModelo(shModel)
        snmp=FiltroNetmiko.obtenerSNMP(snmpcomando)
        interface=FiltroNetmiko.filtroInterface(shRun)

    
        lista.append(hostname)
        lista.append(model)
        lista.append(ip.strip())
        lista.append(snmp)
        lista.append(interface)
        lista.append(brief)
        lista.append(shVer)
        lista.append(shRun)
    
        ListaToExcel.datosToExcel(lista)
    except Exception as e:
        print(f"ERROR GENERAL {ip}")    
