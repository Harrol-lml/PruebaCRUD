from flask import Flask, request, render_template
from manejador_bd import manejador_bd
import smtplib 
from flask import Markup 

app = Flask(__name__)

man=manejador_bd()
tit="Prueba CRUD"

@app.route("/")
def home():
	return render_template("index2.html",tit=tit)
	
@app.route("/buscar")
def buscar():
	bus=request.args['busqueda']
	#return man.buscarCategoriaId(bus) 
	return man.buscarProductoId(bus)
	
	
@app.route("/buscarc")
def buscarc():
	bus=request.args['busqueda']
	return man.buscarCategoriaId(bus) 
	#return man.buscarProductoId(bus)
	
@app.route("/agregarCategoria")
def addCategoria():
	nombre=request.args['Nombre']
	codigo=request.args['Codigo']
	descripcion=request.args['descr']
	i=request.args['id']
	#actv=request.args['actvo']
	print(nombre, codigo,str(i), descripcion)

	return render_template("index2.html",tit=tit) + man.addCategoria(i,codigo,nombre,descripcion, 'True')
	
@app.route("/agregarProducto")
def addProducto():
	nombre=request.args['Nombre']
	codigo=request.args['Codigo']
	descripcion=request.args['descr']
	i=request.args['id']
	marca=request.args['marca']
	idcate=request.args['idCate']
	precio=request.args['precio']
	#actv=request.args['actvo']
	print(nombre, codigo,str(i), descripcion)

	return render_template("index2.html",tit=tit) + man.addProducto(i,codigo,nombre,descripcion,marca,idcate,precio)
	
@app.route("/listarProductos")
def listarP():
	return man.listarProd()
	
@app.route("/listarCategorias")
def listarC():
	return man.listarCategoria()
	
@app.route("/actuCategoria")
def updCategoria():
	nombre=request.args['Nombre']
	codigo=request.args['Codigo']
	descripcion=request.args['descr']
	i=request.args['ida']
	idnuevo=request.args['id']
	#actv=request.args['actvo']
	print(nombre, codigo,str(i), descripcion)

	return render_template("index2.html",tit=tit) + man.updateCategoria(i,idnuevo,codigo,nombre,descripcion, 'True')
	
@app.route("/actuaizarProducto")
def updProducto():
	nombre=request.args['Nombre']
	codigo=request.args['Codigo']
	descripcion=request.args['descr']
	i=request.args['ida']
	idnuevo=request.args['id']
	marca=request.args['marca']
	idcate=request.args['idCate']
	precio=request.args['Precio']
	print(nombre, codigo,str(i), descripcion)
#def updateProducto(self,idv, idp, cod, name,desc,marca, cateid, precio):
	return render_template("index2.html",tit=tit) + man.updateCategoria(i,idnuevo,codigo,nombre,descripcion, marca, idcate,precio)
	
@app.route("/eliminarProducto")
def deletePro():
	ideliminar=request.args['eliminar']
	return man.deleteProducto(ideliminar)#man.buscar(i,ps)
	
@app.route("/eliminarCategoria")
def deleteCate():
	ideliminar=request.args['eliminar']
	return man.deleteCategoria(ideliminar)#man.buscar(i,ps)
	
@app.route("/prueba")
def prueba():
	tit="Hospital Pr1"
	nombre=request.args['Nombre']
	ps=request.args['pass']
	t=request.args['Tipo']
	i=request.args['id']
	e=request.args['Email']
	tel=request.args['Tel']
	#print(nombre, ps, t,str(i), e, str(tel))
	if int(man.validador(i,t,nombre,e,str(tel),ps))==0:	
		return render_template("index.html",tit=tit)+'El id ya se encuentra regstrado, intente con otro id...'
	else:
		return render_template("index.html",tit=tit)+' valide su correo... '
	return render_template("index.html",tit=tit)
	
@app.route("/iniciar")
def iniciar():
	i=request.args['nombre']
	ps=request.args['ps']
	return man.buscar(i,ps)

	
@app.route("/consultar")
def consultar():
	return man.consultar_todo()

if __name__ == "__main__":
	app.run("0.0.0.0")

