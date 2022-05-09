import netmiko
from servicio.netmico.comando import Comando

brief=Comando.enviarComando("sh ip int brief")
print(brief)


