import tkinter as tk 
from tkinter import ttk

class Modificar(tk.Toplevel):
	def __init__(self, menu = None):
		super().__init__(menu, width = 600, height =380)
		self.menu = menu
		self.gui()


	def gui (self):
		
		self.login_imagen = tk.PhotoImage(file= "imag/fond.png")
		self.main = tk.Label(self, image = self.login_imagen, bd=0)
		self.main.pack()


		self.login_info = tk.Label(self, text="MODIFICAR USUARIO",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")) 
		self.login_info.place(x=20,y=35)

		self.usuario_info = tk.Label(self, text="Usuario Antiguo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.usuario_info.place(x=20,y=105)
		self.usuario_string = tk.StringVar()
		self.usuario_entry = tk.Entry(self, textvariable = self.usuario_string)
		self.usuario_entry.focus() 
		self.usuario_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.usuario_entry.place(x=20,y=135)
		self.usuario_line=tk.Frame(self, height=2,width=200)
		self.usuario_line.place(x=20,y=165)

		self.clave_info = tk.Label(self, text="Contraseña Antigua",bg="DeepSkyBlue4",fg="white",font=("Arial",10,"bold")) 
		self.clave_info.place(x=20,y=175)
		self.clave_string = tk.StringVar()
		self.clave_entry = tk.Entry(self, textvariable = self.clave_string) 
		self.clave_entry.config( relief="flat",width=20,bg="DeepSkyBlue4",fg="white",show='*',font=("Arial",15,"bold"))
		self.clave_entry.place(x=20,y=205)
		self.clave_line=tk.Frame(self, height=2,width=200)
		self.clave_line.place(x=20,y=235)

		self.new_usuario_info = tk.Label(self, text="Usuario Nuevo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.new_usuario_info.place(x=330,y=105)
		self.new_usuario_string = tk.StringVar()
		self.new_usuario_entry = tk.Entry(self, textvariable = self.new_usuario_string)
		self.new_usuario_entry.focus() 
		self.new_usuario_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.new_usuario_entry.place(x=330,y=135)
		self.new_usuario_line=tk.Frame(self, height=2,width=200)
		self.new_usuario_line.place(x=330,y=165)

		self.new_clave_info = tk.Label(self, text="Contraseña Nueva",bg="DeepSkyBlue4",fg="white",font=("Arial",10,"bold")) 
		self.new_clave_info.place(x=330,y=175)
		self.new_clave_string = tk.StringVar()
		self.new_clave_entry = tk.Entry(self, textvariable = self.new_clave_string) 
		self.new_clave_entry.config( relief="flat",width=20,bg="DeepSkyBlue4",fg="white",show='*',font=("Arial",15,"bold"))
		self.new_clave_entry.place(x=330,y=205)
		self.new_clave_line=tk.Frame(self, height=2,width=200)
		self.new_clave_line.place(x=330,y=235)

		self.guardar = tk.PhotoImage(file="imag/guardar.png")
		self.btn_inicio = tk.Button(self, command = self.menu)
		self.btn_inicio.config( image = self.guardar, bg = "DeepSkyBlue4", activebackground = "DeepSkyBlue4", cursor = 'hand2', border = 0)
		self.btn_inicio.place(x="40",y="285")

		self.bonton_inicio = tk.PhotoImage(file="imag/modificarr.png")
		self.btn_inicio = tk.Button(self, command = self.menu)
		self.btn_inicio.config( image = self.bonton_inicio, bg = "DeepSkyBlue4", activebackground = "DeepSkyBlue4", cursor = 'hand2', border = 0)
		self.btn_inicio.place(x="350",y="285")

