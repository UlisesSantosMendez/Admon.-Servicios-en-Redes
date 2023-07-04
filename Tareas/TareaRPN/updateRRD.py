import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic1= 0
total_input_traffic2= 0

while True:
    # Paquetes IP que los protocolos locales (incluyendo ICMP) suministraron a IP en las solicitudes de transmisión.
    total_input_traffic1 = int(consultaSNMP('comunidadUJSM', 'localhost','1.3.6.1.2.1.4.9.0'))
    # Mensajes ICMP que ha recibido el agente.
    total_input_traffic2 = int(consultaSNMP('comunidadUJSM', 'localhost','1.3.6.1.2.1.5.1.0'))


    valor = "N:" + str(total_input_traffic1) + ':' + str(total_input_traffic2)
    print (valor)
    rrdtool.update('HWRPN.rrd', valor)
    #rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)