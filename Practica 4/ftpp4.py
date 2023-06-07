from tkinter import *
import telnetlib
from ftplib import FTP
# import os

user="rcp"
password="rcp"

# ///////////////////////FUNCION GENERAR ARCHIVO /////////////////////////////////////
def generar_archivo():
    def btn_gen():
        host = ip_var.get()
        tn = telnetlib.Telnet()
        tn.open(host)
        tn.read_until(b"User: ")
        tn.write(user.encode("ascii") + b"\r\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\r\n")
        tn.write(b"en\r\n")
        tn.write(b"config\r\n")
        tn.write(b"copy run start\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.read_all()
        tn.close()
        genf_exitoso_label = Label(gen_screen, text="Creación Exitosa", fg="green", font=("calibri", 11))
        genf_exitoso_label.place(x=120, y=100)

    global gen_screen
    gen_screen = Toplevel(interfaz)
    gen_screen.title("Generar archivo")
    gen_screen.geometry("430x150")
    ip_label = Label(gen_screen, text="Ingresa IP del router:")
    ip_label.place(x=5, y=10)
    ip_var = StringVar()
    ip_entry = Entry(gen_screen, textvariable=ip_var)
    ip_entry.place(x=200, y=10)
    agregar_button = Button(gen_screen, text="GENERAR", command=btn_gen)
    agregar_button.place(x=180, y=60)
    return gen_screen

#///////////////////////FUNCION EXTRAER ARCHIVO///////////////////////////////////////
def extraer_archivo():
    def btn_extraer():
        host = ip_var.get()
        name = 'startpr4'
        tn = telnetlib.Telnet()
        tn.open(host)
        tn.read_until(b"User: ")
        tn.write(user.encode("ascii") + b"\r\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\r\n")
        tn.write(b"en\r\n")
        tn.write(b"config\r\n")
        tn.write(b"service ftp\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.read_all()
        tn.close()
        ftp = FTP(host)
        ftp.login(user, password)
        ftp.retrbinary('RETR startup-config', open(name, 'wb').write)
        ftp.quit()
        extf_exitoso_label = Label(ext_screen, text="Extracción Exitosa", fg="green", font=("calibri", 11))
        extf_exitoso_label.place(x=120, y=100)

    global ext_screen
    ext_screen = Toplevel(interfaz)
    ext_screen.title("Extraer archivo")
    ext_screen.geometry("430x150")
    ip_label = Label(ext_screen, text="Ingresa IP del router:")
    ip_label.place(x=5, y=10)
    ip_var = StringVar()
    ip_entry = Entry(ext_screen, textvariable=ip_var)
    ip_entry.place(x=200, y=10)
    agregar_button = Button(ext_screen, text="EXTRAER", command=btn_extraer)
    agregar_button.place(x=180, y=60)
    return ext_screen

#////////////////////////FUNCION IMPORTAR ARCHIVO/////////////////////////////////////
def importar_archivo():
    def btn_importar():
        host = ip_var.get()
        name = 'startpr4'
        tn = telnetlib.Telnet()
        tn.open(host)
        tn.read_until(b"User: ")
        tn.write(user.encode("ascii") + b"\r\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\r\n")
        tn.write(b"en\r\n")
        tn.write(b"config\r\n")
        tn.write(b"service ftp\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.write(b"exit\r\n")
        tn.read_all()
        tn.close()
        ftp = FTP(host)
        ftp.login(user, password)
        f = open(name, 'rb')
        ftp.storbinary('STOR startup-config', f)
        f.close()
        ftp.quit()
        impf_exitoso_label = Label(imp_screen, text="Importación Exitosa", fg="green", font=("calibri", 11))
        impf_exitoso_label.place(x=120, y=100)

    global imp_screen
    imp_screen = Toplevel(interfaz)
    imp_screen.title("Importar archivo")
    imp_screen.geometry("430x150")
    ip_label = Label(imp_screen, text="Ingresa IP del router:")
    ip_label.place(x=5, y=10)
    ip_var = StringVar()
    ip_entry = Entry(imp_screen, textvariable=ip_var)
    ip_entry.place(x=200, y=10)
    agregar_button = Button(imp_screen, text="IMPORTAR", command=btn_importar)
    agregar_button.place(x=180, y=60)
    return imp_screen
#/////////////////////FUNCION TERMINAR PROGRAMA//////////////////////////////
def salir():
    exit()

# /////////////////////////////////////INTERFAZ PRINCIPAL MENU /////////////////////////////////////////////
def main_menu():
    global interfaz
    interfaz = Tk()
    interfaz.geometry("600x400")
    interfaz.title('Practica 4')
    Label(interfaz, text=" Sistema de Administracion de Red").pack()
    Label(interfaz, text="").pack()
    Label(interfaz, text="Practica 4 - Administración de configuración").pack()
    Label(interfaz, text="").pack()
    Label(interfaz, text="Ulises Jesus Santos Mendez 4CM14  2020630460").pack()
    Label(interfaz, text="").pack()
    Label(interfaz, text="Elige una opcion:", ).pack(anchor=NW)
    Label(interfaz, text="").pack()
    Button(interfaz, text="Generar archivo", command=generar_archivo).pack()
    Label(interfaz, text="").pack()
    Button(interfaz, text="Extraer archivo", command=extraer_archivo).pack()
    Label(interfaz, text="").pack()
    Button(interfaz, text="Importar archivo", command=importar_archivo).pack()
    Label(interfaz, text="").pack()
    Button(interfaz, text="Salir", command=salir).pack()
    interfaz.mainloop()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

main_menu()