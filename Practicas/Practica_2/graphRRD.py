import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 400
img1 = rrdtool.graph( "paqmulticast.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Mensajes/s",
                     "--title=Mensajes ICMP echo \n que ha enviado el agente",
                     "DEF:traficoEntrada=Bloque3.rrd:paqsendin:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Mensajes ICMP echo enviados")

img1 = rrdtool.graph( "paqip.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Paquetes/s",
                     "--title=Paquetes IP que los protocolos locales (incluyendo ICMP) \n suministraron a IP en las solicitudes de transmisión",
                     "DEF:traficoEntrada=Bloque3.rrd:paqip:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Paquetes IP suministrados")

img1 = rrdtool.graph( "msgICMP.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Mensajes ICMP/s",
                     "--title=Mensajes ICMP que ha recibido el agente",
                     "DEF:traficoEntrada=Bloque3.rrd:msgICMPrcv:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Mensajes ICMP recibidos")

img1 = rrdtool.graph( "segmret.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Segmentos/s",
                     "--title=Segmentos retransmitidos",
                     "DEF:traficoEntrada=Bloque3.rrd:sgmretransmitidos:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Segmentos Retransmitidos")

img1 = rrdtool.graph( "datagramasenv.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Datagramas/s",
                     "--title=Datagramas enviados por el dispositivo",
                     "DEF:traficoEntrada=Bloque3.rrd:datagramassend:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "LINE5:escalaIn#FF0000:Datagramas enviados")

#paso 1 : create
#paso 2 : update
#paso 3 : graph