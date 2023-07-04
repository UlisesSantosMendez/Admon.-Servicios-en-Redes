import time
import rrdtool
from getSNMP import consultaSNMP
total_input_traffic = 0
total_input_traffic1= 0
total_input_traffic2= 0
total_input_traffic3= 0
total_input_traffic4= 0

age = input("Seleccione el index de un agente: ")
numero = int(age)
with open("Agentes.txt", "r") as file:
    devices = file.readlines()

    i = 1
    print("Dispositivos: ")
    with open("Agentes.txt", "r") as file:
        for line in file:
            print(str(i) + "\t" + line)
            i = i + 1
    # numero = 0
    datos = devices[numero-1].split()

    comunidad = datos[0]
    version = datos[1]
    puerto = datos[2]
    ip = datos[3]
while True:
    #Mensajes ICMP echo que ha enviado el agente
    total_input_traffic = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.5.8.0',puerto))
    # Paquetes multicast que ha enviado la interfaz de la interfaz de red de un agente
    #total_input_traffic = int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.2.1.12.3', puerto))
    # Paquetes IP que los protocolos locales (incluyendo ICMP) suministraron a IP en las solicitudes de transmisión.
    total_input_traffic1 = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.4.9.0',puerto))
    # Mensajes ICMP que ha recibido el agente.
    total_input_traffic2 = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.5.1.0', puerto))
    # Segmentos retransmitidos; es decir, el número de segmentos TCP transmitidos que contienen uno o más octetos transmitidos previamente
    total_input_traffic3 = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.6.12.0', puerto))
    # Datagramas enviados por el dispositivo
    total_input_traffic4 = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.4.3.0', puerto))


    valor = "N:" + str(total_input_traffic) + ':' + str(total_input_traffic1) + ':' + str(total_input_traffic2)+ ':' + str(total_input_traffic3) + ':' + str(total_input_traffic4)
    print (valor)
    rrdtool.update('Bloque3.rrd', valor)
    #rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)