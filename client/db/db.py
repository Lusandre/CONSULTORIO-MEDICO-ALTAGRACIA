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
		db_rows = self.run_query()
		return db_rows.fetchall()



