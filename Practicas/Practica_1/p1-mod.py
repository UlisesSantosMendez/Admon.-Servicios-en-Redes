from reportlab.platypus import (Table, TableStyle)
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from getSNMP import consultaSNMP


def agregarAgente():
    print()
    comunidad = input("Comunidad: ")
    version = input("Version: ")
    puerto = input("Puerto: ")
    ip = input("IP: ")

    with open("Agentes.txt", "a") as file:
        file.write(comunidad + " " + version + " " + puerto + " " + ip + "\n")


def modificar():
    print()
    i = 1
    print("Dispositivos: ")
    with open("Agentes.txt", "r") as file:
        datos = file.readlines()

    with open("Agentes.txt", "r") as file:
        for line in file:
            print(str(i) + "\t" + line)
            i = i + 1

    borrar = int(input("Dispositivo a modificar: "))
    i = 1
    print()
    comunidad = input("Comunidad: ")
    version = input("Version: ")
    puerto = input("Puerto: ")
    ip = input("IP: ")
    print()

    with open("Agentes.txt", "w") as file:
        for line in datos:
            if i != borrar:
                file.write(line)
            else:
                file.write(comunidad + " " + version + " " + puerto + " " + ip + "\n")
            i = i + 1


def eliminarAgente():
    print()
    i = 1

    with open("Agentes.txt", "r") as file:
        datos = file.readlines()
    print("Dispositivos: ")
    with open("Agentes.txt", "r") as file:
        for line in file:
            print(str(i) + "\t" + line)
            i = i + 1

    borrar = int(input("Dispositivo a borrar: "))
    i = 1
    with open("Agentes.txt", "w") as file:
        for line in datos:
            if i != borrar:
                file.write(line)
            i = i + 1


def generarReporte():
    age = input("Seleccione el index de un agente para generar su reporte: ")
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
    datos = devices[numero - 1].split()

    comunidad = datos[0]
    version = datos[1]
    puerto = datos[2]
    ip = datos[3]

    datosSNMP = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.1.0", puerto)
    os = "hola"
    if datosSNMP.find("Linux") == 1:
        os = datosSNMP.split()[0]
    else:
        os = datosSNMP.split()[12]

    name = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.5.0", puerto)
    contact = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.4.0", puerto)
    ubi = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.6.0", puerto)
    numInter = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.1.0", puerto)

    i = 1
    interfaces = []
    while i <= 6:
        interfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.7." + str(i), puerto)
        interfaces.append(interfaz)
        i = i + 1
    if os.find("Linux") != -1:
        output = canvas.Canvas("reporteAgente_Linux.pdf")
    else:
        output = canvas.Canvas("reporteAgente_Windows")
    output.setTitle("SNMPReport")
    output.drawString(50, 800, "Administración de Servicios en Red")
    output.drawString(50, 775, "Práctica 1-Adquisición de información")
    output.drawString(50, 750, "Sántos Méndez Ulises Jesús  4CM14  2020630460")
    output.drawString(50, 720, "REPORTE AGENTE:")
    output.drawString(75, 700, "Nombre del dispositivo: " + name)
    output.drawString(75, 680, "S.O.: " + os)
    output.drawString(75, 655, "Contacto: " + contact)
    output.drawString(75, 640, "Ubicacion: " + ubi)
    output.drawString(75, 615, "No. de interfaces: " + numInter)
    output.drawString(75, 590, "1: UP   2:DOWN  3:TESTING")

    i = 1
    matriz = [["INTERFACE", "STATUS"]]
    while i <= 5:
        if os.find("Linux") != -1:
            output.drawImage('Linux.png', 450, 600, width=100, height=100)
            descrInterfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.2." + str(i), puerto)
        else:
            output.drawImage('Windows.png', 450, 600, width=100, height=100)
            res = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.2." + str(i), puerto)[3:]
            descrInterfaz = bytes.fromhex(res).decode('utf-8')

        estadoInterfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.7." + str(i), puerto)

        if estadoInterfaz == "1":
            matriz.append([descrInterfaz, estadoInterfaz])
        elif estadoInterfaz == "2":
            matriz.append([descrInterfaz, estadoInterfaz])
        else:
            matriz.append([descrInterfaz, estadoInterfaz])
        i = i + 1

    tabla = Table(matriz, colWidths=[200, 100])
    tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('FONTSIZE', (0, 0), (-1, 0), 14),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    width = 200
    height = 400
    x = 50
    y = 450
    tabla.wrapOn(output, width, height)
    tabla.drawOn(output, x, y)
    output.save()


def salir():
    print("Fin del programa...")


def menu():
    op = 0
    while op != 5:

        print("---------|Elige una opcion|---------")
        print("1-> Agregar             ")
        print("2-> Eliminar            ")
        print("3-> Modificar           ")
        print("4-> Generar reporte     ")
        print("5-> Salir               ")
        print("------------------------------------")
        op = int(input("Que desea hacer?:"))

        if op == 1:
            agregarAgente()
        elif op == 2:
            eliminarAgente()
        elif op == 3:
            modificar()
        elif op == 4:
            generarReporte()
        elif op == 5:
            salir()


print("\t  Sistema de Administración de red")
print("\tPractica 1 - Adquisición de información")
print("\tSantos Méndez Ulises Jesús \t 4CM14\t 2020630460")
menu()
