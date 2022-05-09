
from ping3 import ping 
import os
from ipaddress import IPv4Address

with open('ipg.txt','r') as stop_words: 
    lista = [linea.strip() for linea in stop_words]

file = open('ping.txt', "w")
datos2=None
datos3=None
for ipAddress in lista:
    datos=ping(ipAddress)
    if datos != None:
         file.write(ipAddress+os.linesep)
         print(f'Guardado! {ipAddress}')
    if datos == None:     
        ipNueva= IPv4Address(ipAddress)+1
        datos2=ping(str(ipNueva))
    if datos2 != None :  
         file.write(str(ipNueva)+os.linesep)
         print(f'Guardado ip nueva! {ipNueva}')
    if datos == None:
        ipNueva2= IPv4Address(ipAddress)+2
        datos3=ping(str(ipNueva2))    
    if datos3 != None :    
        file.write(str(ipNueva2)+os.linesep)
        print(f'Guardado ip nueva! {ipNueva2}')      
    else:
        print("sin Datos")
file.close()    
