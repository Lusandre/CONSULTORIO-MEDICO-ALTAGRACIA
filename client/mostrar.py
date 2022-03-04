import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
from client.db.db import Sqlite
import os, sys

class Mostrar(tk.Toplevel):

	def resolver_ruta(self, ruta_relativa):
		if hasattr(sys, '_MEIPASS'):
			return os.path.join(sys._MEIPASS, ruta_relativa)
		return os.path.join(os.path.abspath('.'), ruta_relativa)

	db_log = Sqlite()

	def __init__(self, menu = None, dia="", ci=""):
		super().__init__(menu, width = 600, height =380)
		self.dia = dia
		self.ci = ci
		self.menu = menu
		self.config(bg="DeepSkyBlue4")
		self.resizable(False,False)
		self.gui()


	def gui (self):
		
		fra=tk.Frame(self,bg="DeepSkyBlue4",height=340,width=500)
		fra.place(x=50,y=30)

		info = tk.Label(fra,text="Registro de Nueva Historia Clinica",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")).place(x=10,y=0)
		self.date = tk.Label(fra,text="",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",9,"bold"))
		self.date.place(x=10,y=36)
		cedula = tk.Label(fra,text="Cedula",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		cedula.place(x=10,y=60)
		self.cedula_label = tk.Label(fra, text="", bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.cedula_label.place(x=13,y=80)
		ced_line=tk.Frame(fra,height=2,width=150)
		ced_line.place(x=13,y=105)

		nombre = tk.Label(fra,text="Nombre",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		nombre.place(x=170,y=60)
		self.nombre_label = tk.Label(fra, text="", bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.nombre_label.place(x=170,y=80)
		nombre_line=tk.Frame(fra,height=2,width=150)
		nombre_line.place(x=170,y=105)

		apellido = tk.Label(fra,text="Apellido",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		apellido.place(x=328,y=60)
		self.apellido_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.apellido_label.place(x=328,y=80)
		ape_line=tk.Frame(fra,height=2,width=150)
		ape_line.place(x=328,y=105)

		direccion = tk.Label(fra,text="Dirección",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		direccion.place(x=10,y=120)
		self.direccion_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.direccion_label.place(x=13,y=140)
		dir_line=tk.Frame(fra,height=2,width=150)
		dir_line.place(x=13,y=165)

		correo = tk.Label(fra,text="Correo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		correo.place(x=170,y=120)
		self.correo_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.correo_label.place(x=170,y=140)
		ape_line=tk.Frame(fra,height=2,width=150)
		ape_line.place(x=170,y=165)

		telefono = tk.Label(fra,text="Telefono",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		telefono.place(x=328,y=120)
		self.telefono_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.telefono_label.place(x=328,y=140)
		tlf_line=tk.Frame(fra,height=2,width=150)
		tlf_line.place(x=328,y=165)

		ante = tk.Label(fra,text="Antecedentes del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		ante.place(x=10,y=175)
		self.ante_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.ante_label.place(x=13,y=200)
		tlf_line=tk.Frame(fra,height=2,width=450)
		tlf_line.place(x=13,y=225)

		eva = tk.Label(fra,text="Evaluacion del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		eva.place(x=10,y=230)
		self.eva_label = tk.Label(fra, text="",bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.eva_label.place(x=13,y=255)
		tlf_line=tk.Frame(fra,height=2,width=450)
		tlf_line.place(x=13,y=280)

		self.boton_registrar = tk.PhotoImage(file= self.resolver_ruta("imag/volver.png"))
		self.boton_cacelar =  tk.PhotoImage(file= self.resolver_ruta("imag/exportar.png"))

		self.cargar()

		BTN_R = tk.Button(fra, image=self.boton_registrar,command=self.destroy,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		BTN_R.place(x=70,y=300)

		BTN_C = tk.Button(fra,image=self.boton_cacelar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		BTN_C.place(x=300,y=300)
	
	 # Get Products from Database

	def cargar(self):
				
		db_rows = self.db_log.rellenar((self.ci,))
		# filling data
		for row in db_rows:
			self.cedula_label.config(text=row[0])
			self.nombre_label.config(text=row[1])
			self.apellido_label.config(text=row[2])
			self.direccion_label.config(text=row[3])
			self.correo_label.config(text=row[4])
			self.telefono_label.config(text=row[5])
		db_rowsd = self.db_log.rellenar_diag((self.ci,self.dia))
		for row in db_rowsd:
			self.date.config(text=row[1])
			self.ante_label.config(text=row[2])
			self.eva_label.config(text=row[3])

	

	def carga(self):				#Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
		usuario=self.usuario_label.get()		#Obtenemos el valor de la 'caja1' (usuario)
		contr=self.clave_label.get()		#Obtenemos el valor de la 'caja2' (contraseña)
		
		if self.db_log.login((usuario, contr)):
			mb.showinfo(parent = self,title="Datos Correctos",message="Modifique el usuario")		#Mostramos 'Login Correcto'
			self.control()
		else:
			mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")

	def control(self):
		self.new_usuario_Label.config(state="normal")
		self.new_usuario_entry.focus()
		self.new_clave_entry.config(state="normal")
		self.btn_inicio.config(state="normal")
		self.usuario_entry.config(state="disable")
		self.clave_entry.config(state="disable")
		self.btn_comprobar.config(state="disable")

	def actualizar(self):
		usuario = self.usuario_entry.get()
		new_usuario = self.new_usuario_entry.get()
		contr = self.new_clave_entry.get()
		self.db_log.actualizar((new_usuario,contr,usuario))
		mb.showinfo(parent = self,title="Actualización Correcta",message="Se modifico con exito el usuario")
		self.destroy()