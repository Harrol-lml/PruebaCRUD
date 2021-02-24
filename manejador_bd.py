import psycopg2

PSQL_HOST= "localhost"
PSQL_PORT= "5432"
PSQL_USER= "postgres"
PSQL_PASS= "password"
PSQL_DB= "prueba"

connection_address= """
host=%s  port=%s user=%s password=%s dbname=%s
"""%(PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_DB)




class manejador_bd:
	
	def limpiarFormato (self, cadena):
		cadena= cadena.replace("\'","")
		cadena= cadena.replace("[","")
		cadena= cadena.replace("]","")
		cadena= cadena.replace("(","")
		cadena= cadena.replace(")","")
		print (cadena)
		return cadena
	
	
	# LISTAR PRODUCTO / CATEGORIA 
	def listarProd(self):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		sql="SELECT *FROM Producto;"
		try:
			cursor.execute(sql)
		except:
			return "Error "
			
		else:
			all_values= cursor.fetchall()
			cursor.close()
			connection.close()
			if all_values:
				cont=0
				cadenalimpia=man.limpiarFormato(str(all_values))
				separa= cadenalimpia.split(sep=',')	
				cad='<center><table border="2">'
				cad=cad+"<tr><td>Id Producto</td><td>Codigo</td><td>Nombre</td><td>Descripcion</td><td>Marca</td><td>Categoria</td><td>Precio</td></tr><tr><td>"
				for elemt in separa:
					if cont<7:
						cad=cad+elemt+"</td><td>"						
						print (str(cont)+ elemt)
						
						
					if cont==7:
						cont=0
						cad=cad+"</td></tr><tr><td>"+elemt+"</td><td>"
						print (str(cont)+ elemt)
					cont=cont+1
					
				cad=cad+"</table></center>"
				print (len(separa))
				return cad
			else:
				return "Tabla vacia."
	
		
	def listarCategoria(self):

		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()

		SQL="SELECT * FROM CategoriaP;"
		try:
			cursor.execute(SQL)
		except:
			return "Error "
			
		else:
			all_values= cursor.fetchall()
			cursor.close()
			connection.close()
			if all_values:
				cont=0
				cadenalimpia=man.limpiarFormato(str(all_values))
				separa= cadenalimpia.split(sep=',')	
				print (type(separa))
				#cad=""
				cad='<center><table border="2">'
				cad=cad+"<tr><td>Id Categoria</td><td>Codigo</td><td>Nombre</td><td>Descripcion</td><td>Activo</td></tr><tr><td>"
				for elemt in separa:
					if cont<5:
						cad=cad+elemt+"</td><td>"
						print (str(cont)+ elemt)
						
						
					if cont==5:
						cont=0
						cad=cad+"</td></tr><tr><td>"+elemt+"</td><td>"
						print (str(cont)+ elemt)
					cont=cont+1
					
				cad=cad+"</table></center>"
				print (len(separa))
				return cad
			else:
				return "Tabla vacia."
		
	#Buscar por id -CATEGORIA / PRODUCTO
	
	def buscarProductoId (self, idCod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		SQL="SELECT * FROM Producto WHERE (idPro="+idCod+");"
		try:
			cursor.execute(SQL)
		except:
			print('Id {0} no encotrado, intente con otro')
			cursor.close()
			connection.close()
			return 'Id {0} no encotrado, intente con otro'.format(idCod)
		else:	
			
			all_values= cursor.fetchall()
			cursor.close()
			connection.close()
			if(all_values):
				cadenalimpia=man.limpiarFormato(str(all_values))
				separa= cadenalimpia.split(sep=',')
				cad='<center><table border="2">'
				cad=cad+"<tr><td>Id Producto</td><td>Codigo</td><td>Nombre</td><td>Descripcion</td><td>Marca</td><td>Categoria</td><td>Precio</td></tr>"
				cad=cad+"<tr><td>"+str(separa[0])+"</td><td>"+str(separa[1])+"</td><td>"+str(separa[2])+"</td><td>"+str(separa[3])+"</td><td>"+str(separa[4])+"</td><td>"+str(separa[5])+"</td><td>"+str(separa[6])+"</td></tr>"
				cad=cad+"</table></center>"

				return cad
			else:
				return 'Id {0} no encotrado, intente con otro'.format(idCod)	
	
		
		
		
	def buscarCategoriaId (self, idCod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		SQL="SELECT * FROM CategoriaP WHERE (id="+idCod+");"
		try:
			cursor.execute(SQL)
		except:
			print('Id {0} no encotrado, intente con otro')
			cursor.close()
			connection.close()
			return 'Id {0} no encotrado, intente con otro'.format(idCod)
		else:	
			
			all_values= cursor.fetchall()
			cursor.close()
			connection.close()
			if(all_values):
				cadenalimpia=man.limpiarFormato(str(all_values))
				separa= cadenalimpia.split(sep=',')
				cad='<center><table border="2">'
				cad=cad+"<tr><td>Id Categoria</td><td>Codigo</td><td>Nombre</td><td>Descripcion</td><td>Activo</td></tr>"
				cad=cad+"<tr><td>"+str(separa[0])+"</td><td>"+str(separa[1])+"</td><td>"+str(separa[2])+"</td><td>"+str(separa[3])+"</td><td>"+str(separa[4])+"</td></tr>"
				cad=cad+"</table></center>"
			
				return cad
			else:
				return 'Id {0} no encotrado, intente con otro'.format(idCod)	
	
		
		"""#SQL2="SELECT cod FROM CategoriaP WHERE (id="+idCod+");"
		cursor.execute(SQL1)		
		all_values1= cursor.fetchall()
		#cursor.execute(SQL2)
		#val2=cursor.fetchall()
		
		cursor.close()
		connection.close()
		n=str(all_values1)
		#c=str(val2)
		
		cadena=man.limpiarFormato(n)#+man.limpiarFormato(c)
		
		return n"""
		
		
	#Buscar por nombre - CATEGORIA / PRODUCTO
	def buscarProductoNom (self, nomCod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		nom="\'"+nomCod+"\'"
		SQL="SELECT * FROM Producto WHERE (nombrePro="+nom+");"
		cursor.execute(SQL)		
		all_values= cursor.fetchall()
		
		cursor.close()
		connection.close()
		return str(all_values)
		
		
	def buscarCategoriaNom (self, nomCod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		nom="\'"+nomCod+"\'"
		SQL="SELECT * FROM CategoriaP WHERE (nombre="+nom+");"
		cursor.execute(SQL)		
		all_values= cursor.fetchall()
		
		cursor.close()
		connection.close()
		return str(all_values)
		
	#Buscar por codigo - CATEGORIA / PRODUCTO
	def buscarProductoCod (self, cod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		codigo="\'"+cod+"\'"
		SQL="SELECT * FROM Producto WHERE (codPro="+codigo+");"
		cursor.execute(SQL)		
		all_values= cursor.fetchall()
		
		cursor.close()
		connection.close()
		return str(all_values)
		
	def buscarCategoriaCod (self, cod):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()
		
		codigo="\'"+cod+"\'"
		SQL="SELECT * FROM CategoriaP WHERE (cod="+codigo+");"
		cursor.execute(SQL)		
		all_values= cursor.fetchall()
		
		cursor.close()
		connection.close()
		return str(all_values)
		
		
	#AGREGAR CATEGORIA / PRODUCTO	
	
	
	def addCategoria(self, idc, cod, name,desc,actv):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		nombre=man.buscarCategoriaNom(name)
		codigo=man.buscarCategoriaCod(cod)
		if man.limpiarFormato(nombre) or man.limpiarFormato(codigo):
			print (nombre + codigo)
			return "El nombre "+name+" o codigo "+ cod+" de la categoria ya existen" 
			
		else:
			SQL="INSERT INTO CategoriaP (id, cod, nombre, decripcion, activo) VALUES ("+idc+","+"\'"+cod+"\'"+","+"\'"+name+"\'"+","+"\'"+desc+"\'"+","+"\'"+actv+"\'"+");"
			try:
				cursor.execute(SQL)
			except:
				print('Puede haber un valor duplicado..')
				cursor.close()
				connection.close()
				return 'Error: EL codigo: {0} puede estar registrado, revise bien'.format(idc)
			else:	
				connection.commit()
				cursor.close()
				connection.close()
				return 'Valor ingresado'
			
		
	def addProducto(self, idp, cod, name,desc,marca, cateid, precio):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		
		nombre=man.buscarProductoNom(name)
		codigo=man.buscarProductoCod(cod)
		
		if man.limpiarFormato(nombre) or man.limpiarFormato(codigo):
			return "El nombre "+name+" o codigo "+ cod+" del Prducto ya existen" 
		
		else:
			SQL="INSERT INTO Producto (idPro, codPro, nombrePro, descPro, marca, categoriaId, precio) VALUES ("+idp+","+"\'"+cod+"\'"+","+"\'"+name+"\'"+","+"\'"+desc+"\'"+","+"\'"+marca+"\'"+","+cateid+","+precio+");"
			try:
				cursor.execute(SQL)
			except:
				print('Puede haber un valor duplicado..')
				cursor.close()
				connection.close()
				return 'Error: EL codigo: {0} puede estar registrado, revise bien'.format(idp)
			else:	
				connection.commit()
				cursor.close()
				connection.close()
				return 'Valor ingresado'	
			
	#Actualizar por id -CATEGORIA / PRODUCTO
	
	def updateCategoria(self,idv, idc, cod, name,desc,actv):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		
		if man.buscarCategoriaId(idv):		
			
			#UPDATE Producto SET idPro = 1,nombrePro='Limpido' WHERE (idPro= '2');
			SQL="UPDATE CategoriaP SET id = "+idc+",cod="+"\'"+cod+"\', nombre =\'"+name+"\',decripcion=\'"+desc+"\',activo=\'"+actv+"\' WHERE (id="+idv+");"
			print(SQL)
			try:
				cursor.execute(SQL)
				
			except:
				print('Puede haber un valor duplicado..')
				cursor.close()
				connection.close()
				return 'Error: EL codigo: {0} puede estar registrado, revise bien'.format(idv)
			else:
				connection.commit()
				cursor.close()
				connection.close()
				return 'Valor Actualizado'
		else:
			return 'El id : {0} quiere modificar no esta registrado aun. '.format(idb)
			
	def updateProducto(self,idv, idp, cod, name,desc,marca, cateid, precio):
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		
		if man.buscarProductoId(idv):

			SQL="UPDATE Producto SET idPro = "+idc+",codPro="+"\'"+cod+"\',nombreCod =\'"+name+"\',descPro =\'"+desc+"\',marca=\'"+marca+"\',categoriaId = \'"+cateid+"\',precio=\'"+precio+"\' WHERE (id="+idv+");"
			try:
				cursor.execute(SQL)
			except:
				print('Puede haber un valor duplicado..')
				cursor.close()
				connection.close()
				return 'Error: EL codigo: {0} puede estar registrado, revise bien'.format(idv)
			else:
				connection.commit()
				cursor.close()
				connection.close()
				return 'Valor Actualizado'
		else:
			return 'El id : {0} quiere modificar no esta registrado aun. '.format(idb)
				
		
	#Eliminar por id -CATEGORIA / PRODUCTO	
		
	def deleteCategoria(self, ide):		
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		
		sql="DELETE FROM CategoriaP WHERE (id="+ide+");"
		
		try:
			cursor.execute(sql)
		except:
			print('Puede haber un valor duplicado..')
			cursor.close()
			connection.close()
			return 'Error al eliminar categoria con id: {0}'.format(ide)
		else:
			connection.commit()
			cursor.close()
			connection.close()
			return 'Categoria con Id {0} eliminada con exito.'.format(ide)
		
	def deleteProducto(self, ide):		
		connection = psycopg2.connect(connection_address)
		cursor= connection.cursor()	
		
		sql="DELETE FROM Producto WHERE (idPro="+ide+");"
		
		try:
			cursor.execute(sql)
		except:
			print('Puede haber un valor duplicado..')
			cursor.close()
			connection.close()
			return 'Error al eliminar el el producto id: {0}'.format(ide)
		else:
			connection.commit()
			cursor.close()
			connection.close()
			return 'Producto con Id {0} eliminado con exito.'.format(ide)
		
man=manejador_bd()	
