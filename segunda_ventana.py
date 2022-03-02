import tkinter 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 
import os

def ventana_inicio():
	global ventana_principal

	ventana_principal=Tk()
	ventana_principal.geometry("600x380")
	ventana_principal.title("CONSULTORIO MEDICO ALTAGRACIA")
	ventana_principal.resizable(False,False)
	ventana_principal.config(bg="DeepSkyBlue4")

	login_frame=Frame(ventana_principal,bg="DeepSkyBlue4",height=340,width=500)
	login_frame.place(x=50,y=30)

	info = Label(login_frame,text="Historia Clinica",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")).place(x=10,y=0 )

	nombre = Label(login_frame,text="Nombre",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	nombre.place(x=10,y=60)
	nombre_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	nombre_entry.place(x=13,y=80)
	nombre_line=Frame(login_frame,height=2,width=150)
	nombre_line.place(x=13,y=105)

	apellido = Label(login_frame,text="Apellido",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	apellido.place(x=170,y=60)
	apellido_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	apellido_entry.place(x=170,y=80)
	ape_line=Frame(login_frame,height=2,width=150)
	ape_line.place(x=170,y=105)

	cedula = Label(login_frame,text="Cedula",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	cedula.place(x=328,y=60)
	cedula_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	cedula_entry.place(x=328,y=80)
	ced_line=Frame(login_frame,height=2,width=150)
	ced_line.place(x=328,y=105)

	fecha = Label(login_frame,text="Fecha Dianostico",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	fecha.place(x=10,y=120)
	fecha_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	fecha_entry.place(x=13,y=140)
	fecha_line=Frame(login_frame,height=2,width=150)
	fecha_line.place(x=13,y=165)

	apellido = Label(login_frame,text="Correo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	apellido.place(x=170,y=120)
	apellido_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	apellido_entry.place(x=170,y=140)
	ape_line=Frame(login_frame,height=2,width=150)
	ape_line.place(x=170,y=165)

	cedula = Label(login_frame,text="Telefono",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	cedula.place(x=328,y=120)
	cedula_entry = Entry(login_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
	cedula_entry.place(x=328,y=140)
	ced_line=Frame(login_frame,height=2,width=150)
	ced_line.place(x=328,y=165)

	ante = Label(login_frame,text="Antecedentes del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	ante.place(x=10,y=175)
	ante_entry = Entry(login_frame,relief="flat",width=46,bg="white",fg="black",font=("Arial",11,"bold")) 
	ante_entry.place(x=13,y=200)

	eva = Label(login_frame,text="Evaluacion del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
	eva.place(x=10,y=230)
	eva_entry = Entry(login_frame,relief="flat",width=46,bg="white",fg="black",font=("Arial",11,"bold")) 
	eva_entry.place(x=13,y=255)

	boton_registrar = PhotoImage(file="imag/volver.PNG")
	boton_cacelar =  PhotoImage(file="imag/exportar.png")

	BTN_R = Button(login_frame,image=boton_registrar,bg="DeepSkyBlue4",border=0)
	BTN_R.place(x=70,y=300)

	BTN_C = Button(login_frame,image=boton_cacelar,bg="DeepSkyBlue4",border=0)
	BTN_C.place(x=300,y=300)

	ventana_principal.mainloop()




ventana_inicio()