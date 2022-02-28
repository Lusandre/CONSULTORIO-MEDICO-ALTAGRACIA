import tkinter as tk 
from tkinter import ttk
import sqlite3
from tkinter import messagebox as mb
from datetime import datetime

class Frame(tk.Frame):

	db_name = 'database.db'

	def __init__(self, root = None):
		super().__init__(root, width = 480, height =320)
		self.root = root
		self.pack()
		
		
		self.inicio()
		#self.tabla()

	def run_query(self, query, parameters = {}):
		with sqlite3.connect(self.db_name) as conn: 
			cursor = conn.cursor()
			result = cursor.execute(query, parameters)
			conn.commit()
		return result



	def inicio (self):
		self.login_imagen = tk.PhotoImage(file= "fondo.png")
		self.main = tk.Label(self, image = self.login_imagen, bd=0)
		self.main.pack()

		self.login_info = tk.Label(self, text="INICIAR SESIÓN",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")) 
		self.login_info.place(x=20,y=45)

		self.usuario_info = tk.Label(self, text="Usuario",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.usuario_info.place(x=20,y=105)
		self.usuario_string = tk.StringVar()
		self.usuario_entry = tk.Entry(self, textvariable = self.usuario_string)
		self.usuario_entry.focus() 
		self.usuario_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.usuario_entry.place(x=20,y=135)
		self.usuario_line=tk.Frame(self, height=2,width=200)
		self.usuario_line.place(x=20,y=165)

		self.clave_info = tk.Label(self, text="Contraseña",bg="DeepSkyBlue4",fg="white",font=("Arial",10,"bold")) 
		self.clave_info.place(x=20,y=175)
		self.clave_string = tk.StringVar()
		self.clave_entry = tk.Entry(self, textvariable = self.clave_string) 
		self.clave_entry.config( relief="flat",width=20,bg="DeepSkyBlue4",fg="white",show='*',font=("Arial",15,"bold"))
		self.clave_entry.place(x=20,y=205)
		self.clave_line=tk.Frame(self, height=2,width=200)
		self.clave_line.place(x=20,y=235)

		self.bonton_inicio = tk.PhotoImage(file="Imagen1.png")
		self.btn_inicio = tk.Button(self, command = self.login)
		self.btn_inicio.config( image = self.bonton_inicio, bg = "DeepSkyBlue4", activebackground = "DeepSkyBlue4", cursor = 'hand2', border = 0)
		self.btn_inicio.place(x="40",y="285")

	def login(self):				#Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
		print('hi')
		usuario=self.usuario_entry.get()		#Obtenemos el valor de la 'caja1' (usuario)
		contr=self.clave_entry.get()		#Obtenemos el valor de la 'caja2' (contraseña)
		print('hi')
		query = 'SELECT * FROM usuario WHERE username = ? AND llave = ?'
		
		db_rows = self.run_query(query,(usuario,contr))

		if db_rows.fetchall():
			mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
			self.menu()
		else:
			mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
		#c.close()

	def vacio(self):
		self.textci.set('')
		self.textnom.set('')
		self.textape.set('')
		self.textdir.set('')
		self.texttlf.set('')
		self.textmail.set('')
		self.texteva.set('')
		self.textante.set('')
	
	def clearFrame(self):
    # destroy all widgets from frame
		for widget in self.winfo_children():
			widget.destroy()
		#self.tree.destroy
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
		#self.pack_forget()
		self.menu()

	def menu (self):
		for widget in self.winfo_children():
			widget.destroy()
		#self.tree.destroy
		self.menu = tk.PhotoImage(file= "fondo2.png")
		self.main = tk.Label(self,image = self.menu,bd=0)
		self.main.pack()
		#self.menu_frame=Frame(self.main,bg="white",height=300,width=300)
		#self.menu_frame.place(x=155,y=35)

		self.menu_info = tk.Label(self,text="BIENVENIDO",fg="DeepSkyBlue4",bg="white",font=("Bodoni MT",20,"bold")).place(x=205,y=45)
		self.menu_info1 = tk.Label(self,text="Escoja la tarea que desee realizar",fg="DeepSkyBlue4",bg="white",font=("Bodoni MT",10,"bold")).place(x=200,y=85)

		self.bonton_registro = tk.PhotoImage(file="botonR2.png")
		self.btn_registro= tk.Button(self,image=self.bonton_registro,command = self.registro, bg="white",border=0)
		self.btn_registro.place(x=195,y=135)

		self.bonton_consultar = tk.PhotoImage(file="botonR1.png")
		self.bnt_consultar= tk.Button(self,image=self.bonton_consultar,bg="white",border=0, command = self.tablad) 
		self.bnt_consultar.place(x=195,y=185)

		self.bonton_editar = tk.PhotoImage(file="botonR3.png")
		self.bnt_editar= tk.Button(self,command = self.modificar,image=self.bonton_editar,bg="white",border=0)
		self.bnt_editar.place(x=195,y=235)

		self.bonton_salir = tk.PhotoImage(file="botonR.png")
		self.bnt_salir= tk.Button(self,image=self.bonton_salir,bg="white",border=0)
		self.bnt_salir.place(x=225,y=305)

	

	def modificar (self):
		global pantalla_modificar 
		pantalla_modificar = tk.Toplevel(self)
		pantalla_modificar.config(bg="DeepSkyBlue4",width = 600, height =380)
		self.login_imagen = tk.PhotoImage(file= "fond.png")
		self.main = tk.Label(pantalla_modificar, image = self.login_imagen, bd=0)
		self.main.pack()


		self.login_info = tk.Label(pantalla_modificar, text="MODIFICAR USUARIO",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")) 
		self.login_info.place(x=20,y=35)

		self.usuario_info = tk.Label(pantalla_modificar, text="Usuario Antiguo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.usuario_info.place(x=20,y=105)
		self.usuario_string = tk.StringVar()
		self.usuario_entry = tk.Entry(pantalla_modificar, textvariable = self.usuario_string)
		self.usuario_entry.focus() 
		self.usuario_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.usuario_entry.place(x=20,y=135)
		self.usuario_line=tk.Frame(pantalla_modificar, height=2,width=200)
		self.usuario_line.place(x=20,y=165)

		self.clave_info = tk.Label(pantalla_modificar, text="Contraseña Antigua",bg="DeepSkyBlue4",fg="white",font=("Arial",10,"bold")) 
		self.clave_info.place(x=20,y=175)
		self.clave_string = tk.StringVar()
		self.clave_entry = tk.Entry(pantalla_modificar, textvariable = self.clave_string) 
		self.clave_entry.config( relief="flat",width=20,bg="DeepSkyBlue4",fg="white",show='*',font=("Arial",15,"bold"))
		self.clave_entry.place(x=20,y=205)
		self.clave_line=tk.Frame(pantalla_modificar, height=2,width=200)
		self.clave_line.place(x=20,y=235)

		self.new_usuario_info = tk.Label(pantalla_modificar, text="Usuario Nuevo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.new_usuario_info.place(x=330,y=105)
		self.new_usuario_string = tk.StringVar()
		self.new_usuario_entry = tk.Entry(pantalla_modificar, textvariable = self.new_usuario_string)
		self.new_usuario_entry.focus() 
		self.new_usuario_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.new_usuario_entry.place(x=330,y=135)
		self.new_usuario_line=tk.Frame(pantalla_modificar, height=2,width=200)
		self.new_usuario_line.place(x=330,y=165)

		self.new_clave_info = tk.Label(pantalla_modificar, text="Contraseña Nueva",bg="DeepSkyBlue4",fg="white",font=("Arial",10,"bold")) 
		self.new_clave_info.place(x=330,y=175)
		self.new_clave_string = tk.StringVar()
		self.new_clave_entry = tk.Entry(pantalla_modificar, textvariable = self.new_clave_string) 
		self.new_clave_entry.config( relief="flat",width=20,bg="DeepSkyBlue4",fg="white",show='*',font=("Arial",15,"bold"))
		self.new_clave_entry.place(x=330,y=205)
		self.new_clave_line=tk.Frame(pantalla_modificar, height=2,width=200)
		self.new_clave_line.place(x=330,y=235)

		self.guardar = tk.PhotoImage(file="guardar.png")
		self.btn_inicio = tk.Button(pantalla_modificar, command = self.menu)
		self.btn_inicio.config( image = self.guardar, bg = "DeepSkyBlue4", activebackground = "DeepSkyBlue4", cursor = 'hand2', border = 0)
		self.btn_inicio.place(x="40",y="285")

		self.bonton_inicio = tk.PhotoImage(file="modificarr.png")
		self.btn_inicio = tk.Button(pantalla_modificar, command = self.menu)
		self.btn_inicio.config( image = self.bonton_inicio, bg = "DeepSkyBlue4", activebackground = "DeepSkyBlue4", cursor = 'hand2', border = 0)
		self.btn_inicio.place(x="350",y="285")

	def tablad(self):
		global tabla 
		tabla = tk.Toplevel(self)
		tabla.config(bg="DeepSkyBlue4",width = 600, height =380)
		
		self.tabla_info = tk.Label(tabla,text="Consulta de Historias de Pacientes",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")).place(x=105,y=10)

		self.ci_info = tk.Label(tabla, text="CI del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		self.ci_info.place(x=20,y=50)
		self.ci_string = tk.StringVar()
		self.ci_entry = tk.Entry(tabla, textvariable = self.ci_string)
		self.ci_entry.focus() 
		self.ci_entry.config(relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold"))
		self.ci_entry.place(x=20,y=70)
		self.ci_line=tk.Frame(tabla, height=2,width=140)
		self.ci_line.place(x=20,y=95)

		self.bonton_buscar = tk.PhotoImage(file="buscar.png")
		self.bnt_salir= tk.Button(tabla, command=self.buscar,image=self.bonton_buscar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		self.bnt_salir.place(x=190,y=70)

		self.tree = ttk.Treeview(tabla, height = 10, columns = ('','','','',''))
		self.tree.place(x=10,y=110)
		#tree.grid(row = 0, column = 0, columnspan = 3)
		self.tree['show'] = 'headings'
		self.tree.heading('#1', text = 'Fecha')
		self.tree.heading('#2', text = 'Cedula')
		self.tree.heading('#3', text = 'Nombres')
		self.tree.heading('#4', text = 'Apellidos')
		self.tree.heading('#5', text = 'telefono')
		self.tree.column("#1", width=60, stretch=False)
		self.tree.column("#2", width=70, stretch=False)
		self.tree.column("#3", width=174, stretch=False)
		self.tree.column("#4", width=174, stretch=False)
		self.tree.column("#5", width=100, stretch=False)

		self.tree.insert('',0, values = ('12-01-22', '28349644', 'Lusandre', 'Marcano','04143958194'))

		self.bonton_mostrar = tk.PhotoImage(file="mostrar.png")
		self.bnt_mostrar= tk.Button(tabla,image=self.bonton_mostrar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		self.bnt_mostrar.place(x=125,y=345)	

		self.bonton_volver = tk.PhotoImage(file="volver.png")
		self.bnt_volver= tk.Button(tabla, command = tabla.destroy)
		self.bnt_volver.config(image=self.bonton_volver,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		self.bnt_volver.place(x=325,y=345)
		self.get_products()

	def buscar(self):
		
        # cleaning Table 
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		ci=self.ci_entry.get()
		print(ci)
        # getting data
		#query = 'SELECT * FROM paciente ORDER BY ci DESC'
		query = 'SELECT fecha, ci, nombre, apellido, telefono FROM diagnostico, paciente WHERE diagnostico.cipaciente=paciente.ci AND diagnostico.cipaciente= ?'
		
		db_rows = self.run_query(query,(ci,))
		# filling data
		print (db_rows)
		for row in db_rows:
			self.tree.insert('', 0, values = (row[0],row[1],row[2], row[3],row[4]))

	def registro(self):
		global ventana_registro

		ventana_registro = tk.Toplevel(self)
		ventana_registro.geometry("600x380")
		ventana_registro.title("CONSULTORIO MEDICO ALTAGRACIA")
		ventana_registro.resizable(False,False)
		ventana_registro.config(bg="DeepSkyBlue4")

		registro_frame=tk.Frame(ventana_registro,bg="DeepSkyBlue4",height=340,width=500)
		registro_frame.place(x=50,y=30)

		info = tk.Label(registro_frame,text="Registro de Nueva Historia Clinica",fg="white",bg="DeepSkyBlue4",font=("Bodoni MT",20,"bold")).place(x=10,y=0 )

		self.textci = tk.StringVar()
		self.textnom = tk.StringVar()
		self.textape = tk.StringVar()
		self.textdir = tk.StringVar()
		self.textmail = tk.StringVar()
		self.texttlf = tk.StringVar()
		self.texteva = tk.StringVar()
		self.textante = tk.StringVar()

		cedula = tk.Label(registro_frame,text="Cedula",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		cedula.place(x=10,y=60)
		self.cedula_entry = tk.Entry(registro_frame, textvariable=self.textci, relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.cedula_entry.place(x=13,y=80)
		ced_line=tk.Frame(registro_frame,height=2,width=150)
		ced_line.place(x=13,y=105)

		self.bnt_buscar = tk.PhotoImage(file="bus.png")
		self.bnt_bus= tk.Button(registro_frame, command=self.bus,image=self.bnt_buscar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		self.bnt_bus.place(x=135,y=80)

		
		#Este texto aparecera en la entry por defecto:
		#self.textnom.set('')

		nombre = tk.Label(registro_frame,text="Nombre",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		nombre.place(x=170,y=60)
		self.nombre_entry = tk.Entry(registro_frame, textvariable=self.textnom,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.nombre_entry.place(x=170,y=80)
		nombre_line=tk.Frame(registro_frame,height=2,width=150)
		nombre_line.place(x=170,y=105)

		apellido = tk.Label(registro_frame,text="Apellido",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		apellido.place(x=328,y=60)
		self.apellido_entry = tk.Entry(registro_frame, textvariable=self.textape,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.apellido_entry.place(x=328,y=80)
		ape_line=tk.Frame(registro_frame,height=2,width=150)
		ape_line.place(x=328,y=105)

		direccion = tk.Label(registro_frame,text="Dirección",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		direccion.place(x=10,y=120)
		self.direccion_entry = tk.Entry(registro_frame, textvariable=self.textdir,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.direccion_entry.place(x=13,y=140)
		dir_line=tk.Frame(registro_frame,height=2,width=150)
		dir_line.place(x=13,y=165)

		'''cedula = tk.Label(registro_frame,text="Cedula",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
										cedula.place(x=328,y=60)
										cedula_entry = tk.Entry(registro_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
										cedula_entry.place(x=328,y=80)
										ced_line=tk.Frame(registro_frame,height=2,width=150)
										ced_line.place(x=328,y=105)
								
										fecha = tk.Label(registro_frame,text="Fecha Dianostico",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
										fecha.place(x=10,y=120)
										fecha_entry = tk.Entry(registro_frame,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
										fecha_entry.place(x=13,y=140)
										fecha_line=tk.Frame(registro_frame,height=2,width=150)
										fecha_line.place(x=13,y=165)'''

		correo = tk.Label(registro_frame,text="Correo",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		correo.place(x=170,y=120)
		self.correo_entry = tk.Entry(registro_frame, textvariable=self.textmail,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.correo_entry.place(x=170,y=140)
		ape_line=tk.Frame(registro_frame,height=2,width=150)
		ape_line.place(x=170,y=165)

		telefono = tk.Label(registro_frame,text="Telefono",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		telefono.place(x=328,y=120)
		self.telefono_entry = tk.Entry(registro_frame, textvariable=self.texttlf,relief="flat",width=20,bg="DeepSkyBlue4",fg="white",font=("Arial",11,"bold")) 
		self.telefono_entry.place(x=328,y=140)
		tlf_line=tk.Frame(registro_frame,height=2,width=150)
		tlf_line.place(x=328,y=165)

		ante = tk.Label(registro_frame,text="Antecedentes del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		ante.place(x=10,y=175)
		self.ante_entry = tk.Entry(registro_frame, textvariable=self.textante,relief="flat",width=105,bg="white",fg="black",font=("Arial",11,"bold")) 
		self.ante_entry.place(x=13,y=200)

		eva = tk.Label(registro_frame,text="Evaluacion del Paciente",fg="white",bg="DeepSkyBlue4",font=("Arial",10,"bold")) 
		eva.place(x=10,y=230)
		self.eva_entry = tk.Entry(registro_frame, textvariable=self.texteva,relief="flat",width=105,bg="white",fg="black",font=("Arial",11,"bold")) 
		self.eva_entry.place(x=13,y=255)

		self.boton_registrar = tk.PhotoImage(file="BOTON1.png")
		self.boton_cacelar =  tk.PhotoImage(file="BOTON2.png")

		BTN_R = tk.Button(registro_frame, command = self.registra,image=self.boton_registrar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		BTN_R.place(x=70,y=300)

		BTN_C = tk.Button(registro_frame,command = ventana_registro.destroy ,image=self.boton_cacelar,bg="DeepSkyBlue4", activebackground = "DeepSkyBlue4",border=0)
		BTN_C.place(x=300,y=300)
	
	 # Get Products from Database

	def bus(self):

		ci=self.cedula_entry.get()
		print(ci)
        # getting data
		#query = 'SELECT * FROM paciente ORDER BY ci DESC'
		query = 'SELECT * FROM paciente WHERE ci= ?'
		
		db_rows = self.run_query(query,(ci,))
		# filling data
		print (db_rows)
		for row in db_rows:
			self.textnom.set(row[1])
			self.textape.set(row[2])
			self.textdir.set(row[3])
			self.textmail.set(row[4])
			self.texttlf.set(row[5])

	def registra(self):
		ci = self.cedula_entry.get()

		query = 'SELECT * FROM paciente WHERE ci = ?'
		
		db = self.run_query(query,(ci,))
		if not (db.fetchone()): 
			self.reg_paciente()

		self.reg_diagnostico()


	def reg_diagnostico(self):
		query = 'INSERT INTO diagnostico VALUES (?,?,?,?)'
		date = str(datetime.today().strftime('%Y-%m-%d'))	
		print(date)
		parameters = (self.cedula_entry.get(), date, self.ante_entry.get(), self.eva_entry.get())
		self.run_query(query,parameters)
		self.vacio()

	def reg_paciente(self):
		query = 'INSERT INTO paciente VALUES (?,?,?,?,?,?,?)'
		parameters = (self.cedula_entry.get(), self.nombre_entry.get(), self.apellido_entry.get(), self.direccion_entry.get(), self.correo_entry.get(), self.telefono_entry.get(),"28")
		self.run_query(query,parameters)

	def get_products(self):
        # cleaning Table 
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
        # getting data
		#query = 'SELECT * FROM paciente ORDER BY ci DESC'
		query = 'SELECT fecha, ci, nombre, apellido, telefono FROM diagnostico, paciente WHERE diagnostico.cipaciente=paciente.ci ORDER BY fecha DESC'
		
		db_rows = self.run_query(query)
		# filling data
		print (db_rows)
		for row in db_rows:
			self.tree.insert('', 0, values = (row[0],row[1],row[2], row[3],row[4]))