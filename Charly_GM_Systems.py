import os
import pymysql

class BaseDeDatos:
	def init__(self):
		self.connection = pymysql.connect(
		host='localhost', #ip
		user='id17826437_prod_123',
		password='kB8VPudyeQIOL--(',
		db= 'id17826437_productos' 
		)
		
		#Muestra si la conexión fue exitosa
		self.cursor = self.connection.cursor() 
	
	def ingresar_productos(self, codigo, descripcion, cantidad, precio, total):
		insertar = "INSERT INTO Productos (Código, Descripción, Cantidad, Precio, Total) VALUES ('{}', '{}', {}, {})".format(codigo, descripcion, cantidad, precio, total)
		
		try:
			self.cursor.execute(insertar)
			self.connection.commit()
		except Exception as e:
			raise 
			
	def modificar_productos(self, codigo, descripcion, cantidad, precio, total):
		modificar = "UPDATE Productos SET Código='{}', Descripción= '{}', Cantidad= {}, Precio= {} WHERE Código= '{}'".format(codigo, descripcion, cantidad, precio, codigo)
		
		try:
			self.cursor.execute(modificar)
			self.connection.commit()
		except Exception as e:
			raise
	
	def mostrar_productos(self):
		mostrar = 'SELECT * FROM Productos'
		
		try:
			self.cursor.execute(mostrar)
			productos self.cursor.fetchall()
			
			for producto in productos:
				print("Código:", producto[0])
				print("Descripción:", producto[1])
				print("Cantidad:", producto[2])
				print("Precio: Q.", producto[3])
				print("Total: Q.", producto[4])
				print(" ______________________\\n")
		except Exception as e:
			raise 
			
	def mostrar_un_producto(self, codigo):
		mostrar = "SELECT * FROM Productos WHERE Código = '{}'".format(codigo)
		try:
			self.cursor.execute(mostrar) 
			mostrar = self.cursor.fetchone()
			
			print("Código:", mostrar[0])
			print("Descripción:", mostrar[1])
			print("Cantidad:", mostrar[2])
			print("Precio: Q.", mostrar[3])
			print("Total: Q.", mostrar[4])
		except Exception as e:
			raise
	
	def eliminar_producto(self, codigo):
		eliminar = "DELETE FROM Productos WHERE Código= '{}'".format(codigo)
		
		try:
			self.cursor.execute(eliminar)
			self.connection.commit()
		except Exception as e:
			raise
	
	def eliminar_productos(self):
		eliminar = 'DELETE FROM Productos'
		
		try:
			self.cursor.execute(eliminar)
			self.connection.commit()
		except Exception as e:
			raise 
	
	baseDeDatos = BaseDeDatos()

print(" \t\tBases de Datos")
print(" \n\tCharly GM Systems")
print("\n 1-Iniciar sesión")
print(" 2-Crear cuenta")
menu  = int(input("\n Elija una opción: ")) 

os.system("clear")

if menu == 1:
	print("\t\tIniciar sesión")
	usuario = input("\n Usuario: ")
	contrasena = input(" Contraseña: ")
	
	if usuario == 'Charly GM' and contrasena == '123': 
	baseDeDatos.mostrar_productos()
elif menu == 2:
	print("\t\tCrear cuenta")
	id = input("\n Id: ")
	usuario = input(" Usuario: ")
	contrasena = input(" Contraseña: ")
