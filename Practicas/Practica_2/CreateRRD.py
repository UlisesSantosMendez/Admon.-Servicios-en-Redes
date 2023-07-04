#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("Bloque3.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:paqsendin:COUNTER:120:U:U",
                     "DS:paqip:COUNTER:120:U:U",
                     "DS:msgICMPrcv:COUNTER:120:U:U",
                     "DS:sgmretransmitidos:COUNTER:120:U:U",
                     "DS:datagramassend:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:5:48",
                     "RRA:AVERAGE:0.5:1:288")


if ret:
    print (rrdtool.error())

rrdtool.dump("Bloque3.rrd", "Bloque3.xml")
#dump traduce el archivo binario a uno xml