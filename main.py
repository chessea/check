from time import time
from models.DatosChecklist import DatosChecklist
from models.User import User
from models.Equipo import Equipo

from servicio.netmiko.comando import Comando
from servicio.toExcel.listaToExcel import  ListaToExcel
from servicio.filtro.filtroNetmiko import  FiltroNetmiko



print('Ingrese usuario:')
x = input()

print('Ingrese password:')
y = input()

listaIp=["10.0.0.1", "10.0.0.1"]

for ip in listaIp:
    
    listaComandos=['sh run | exclude !', 
                   'sh ip int brief',
                   'sh ver', 
                   'sh run | include hostname',
                   'sh inventory | include "Chassis"',
                   "sh run | include snmp-server community"]
  
    comandos=Comando.enviarComando(listaComandos,ip,x,y)
  
    '''   
    shRun=Comando.enviarComando("sh run | exclude !",ip)
    brief=Comando.enviarComando("sh ip int brief",ip)
    shVer=Comando.enviarComando("sh ver",ip)
    shRunHost=Comando.enviarComando("sh run | include hostname",ip)
    shModel=Comando.enviarComando('sh inventory | include "Chassis"',ip)
    snmpcomando=Comando.enviarComando("sh run | include snmp-server community",ip)
    '''
    
    shRun, brief, shVer, shRunHost, shModel, snmpcomando = comandos
    
    lista=FiltroNetmiko.obtenerCSOTT(shRun)
    hostname=FiltroNetmiko.obtenerHostName(shRunHost)
    model=FiltroNetmiko.obtenerModelo(shModel)
    snmp=FiltroNetmiko.obtenerSNMP(snmpcomando)
    interface=FiltroNetmiko.filtroInterface(shRun)
    
  
    lista.append(hostname)
    lista.append(model)
    lista.append(ip)
    lista.append(snmp)
    lista.append(interface)
    lista.append(brief)
    lista.append(shVer)
    lista.append(shRun)
  
    ListaToExcel.datosToExcel(lista)
    
    
    
''' 

    toExcel.cargarBrief(brief, lista)
    toExcel.cargarVersion(shVer, lista)
    toExcel.cargarEncabezado(lista)
    toExcel.cargarRun(shRun, lista)
   
 '''


















