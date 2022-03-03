import sqlite3

class Sqlite:

	db_name = 'database.db'
	query = ''

	def __init__(self, parameters = {}):
		self.parameters = parameters
	# metodo que corre los query y devuelve el cursor 
	def run_query(self):
		with sqlite3.connect(self.db_name) as conn: 
			cursor = conn.cursor()
			result = cursor.execute(self.query, self.parameters)
			conn.commit()
		return result

	#recibe los parametro usuario y contraseña y devuelve los datos
	def login(self, parameters):
		self.query = 'SELECT * FROM usuario WHERE username = ? AND llave = ?'
		self.parameters = parameters
		result = self.run_query() # Se llama al metodo para correr el query
		return result.fetchall()

	def rellenar(self, parameters):
		self.query = 'SELECT * FROM paciente WHERE ci= ?'
		self.parameters = parameters
		result = self.run_query()
		return result

	def buscar(self, parameters):
		self.query = 'SELECT fecha, ci, nombre, apellido, telefono FROM diagnostico, paciente WHERE diagnostico.cipaciente=paciente.ci AND diagnostico.cipaciente= ?'
		self.parameters = parameters
		result = self.run_query()
		return result

	def existe(self, parameters):
		self.query = 'SELECT * FROM paciente WHERE ci = ?'
		self.parameters = parameters
		result = self.run_query() # Se llama al metodo para correr el query
		return result.fetchall()

	def reg_paciente(self, parameters):
		self.query = 'INSERT INTO paciente VALUES (?,?,?,?,?,?,?)'
		self.parameters = parameters
		self.run_query()

	def reg_diagnostico(self, parameters):
		self.query = 'INSERT INTO diagnostico VALUES (?,?,?,?)'
		self.parameters = parameters
		self.run_query()
	
	def get_historias(self):
		self.query = 'SELECT fecha, ci, nombre, apellido, telefono FROM diagnostico, paciente WHERE diagnostico.cipaciente=paciente.ci ORDER BY fecha DESC'
		self.parameters = {}
		result = self.run_query()
		return result

	def actualizar(self, parameters):
		self.query = "UPDATE usuario SET username = ?, llave = ? WHERE username = ?"
		self.parameters = parameters
		self.run_query()