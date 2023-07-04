#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("HWRPN.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:paqip:COUNTER:120:U:U",
                     "DS:msgICMPrcv:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:5:48",
                     "RRA:AVERAGE:0.5:1:288")


if ret:
    print (rrdtool.error())

rrdtool.dump("HWRPN.rrd", "HWRPN.xml")
#dump traduce el archivo binario a uno xml