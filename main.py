from time import time
from models.DatosChecklist import DatosChecklist
from models.User import User
from models.Equipo import Equipo
from servicio.FiltroDatos import FiltroDatos
from servicio.netmiko.comando import Comando
from servicio.toExcel.toexcel import  toExcel
from servicio.filtro.filtroNetmiko import  FiltroNetmiko



listaIp=["10.0.0.1",]

for ip in listaIp:
  
    shRun=Comando.enviarComando("sh run | exclude !",ip)
    brief=Comando.enviarComando("sh ip int brief",ip)
    shVer=Comando.enviarComando("sh ver",ip)
    shRunHost=Comando.enviarComando("sh run | include hostname",ip)
    shModel=Comando.enviarComando('sh inventory | include "Chassis"',ip)
    snmpcomando=Comando.enviarComando("sh run | include snmp-server community",ip)
    
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
    


    toExcel.cargarEncabezado(lista)
    toExcel.cargarRun(shRun)
    toExcel.cargarBrief(brief)
    toExcel.cargarVersion(shVer)
   


''' 
x= range(0,len(brief))

contador=3
for todos in x:
    contador=contador+1
    book =openpyxl.load_workbook('/home/fr/Documentos/pythonEntel/servicio/store/datos.xlsx')
    sheet = book['interfaces']
    sheet[f'A{contador}']=brief[todos]
    book.save('/home/fr/Documentos/pythonEntel/servicio/store/datos.xlsx')
print('FIN')  '''





''' datos=FiltroDatos.obtenerCSOTT();
ott=datos[0]
cs=datos[1]
ipMonitoreo=datos[2]
interface=datos[3]


check = DatosChecklist(ott, cs, ipMonitoreo, interface,"N/A","JUNJI")
print(check)
 '''






















