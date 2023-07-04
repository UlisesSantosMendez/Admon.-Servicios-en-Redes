
import rrdtool

# Leer los datos del archivo ADIF
adif_file = 'archivo.adif'
qso_list = pyadif.parse(adif_file)

# Crear una lista con los tiempos y las frecuencias de los QSOs
times = []
frequencies = []
for qso in qso_list:
    times.append(int(qso['qso_date']) + int(qso['time_on']))
    frequencies.append(float(qso['freq']))

# Crear el archivo RRD
rrd_file = 'datos.rrd'
rrdtool.create(rrd_file,
               '--start', str(min(times)),
               '--step', '300',
               'DS:frecuencia:GAUGE:600:0:1000',
               'RRA:AVERAGE:0.5:1:288',
               'RRA:MAX:0.5:1:288')

# Almacenar los datos en el archivo RRD
for i in range(len(times)):
    rrdtool.update(rrd_file, '{}:{}'.format(times[i], frequencies[i]))

# Generar un gráfico con los datos
rrdtool.graph('grafico.png',
              '--start', str(min(times)),
              '--end', str(max(times)),
              '--width', '800',
              '--height', '200',
              '--title', 'Frecuencia vs Tiempo',
              '--vertical-label', 'Frecuencia (MHz)',
              'DEF:frecuencia={}:frecuencia:AVERAGE'.format(rrd_file),
              'LINE1:frecuencia#FF0000')
