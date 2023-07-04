import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 1000

img1 = rrdtool.graph( "paqip.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Paquetes IP que los protocolos locales (incluyendo ICMP) \n suministraron a IP en las solicitudes de transmisión",
                     "DEF:traficoEntrada=HWRPN.rrd:paqip:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,1000,LT,10,UN,0,IF",
                     "LINE5:escalaIn#FF0000:Paquetes IP suministrados")

img1 = rrdtool.graph( "msgICMP.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Mensajes ICMP que ha recibido el agente",
                     "DEF:traficoEntrada=HWRPN.rrd:msgICMPrcv:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Mensajes ICMP recibidos")

#paso 1 : create
#paso 2 : update
#paso 3 : graph