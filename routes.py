from flask import Flask 
from flask import render_template,request,redirect,flash,url_for
from datetime import datetime
from random import randint

from flask.helpers import url_for
from werkzeug.datastructures import RequestCacheControl

from modules.users import users
from modules.backAdmin.modulo_productos_ingresados import productosIngresados
from wtforms import Form, BooleanField, StringField, validators

app=Flask(__name__)
app.secret_key="Develoteca"

# index 
@app.route('/')
def index():
    
    return render_template('index.html')

# users 
@app.route('/users/login')
def loguin():
   return render_template('users/login.html')

@app.route('/users/registrar/')
def registrar():

   return render_template('users/registrar.html')

@app.route('/registrar', methods=['POST'])
def registrer():
   name=request.form['txtNombre']
   dir=request.form['txtDireccion']
   telf=request.form['txtTelefono']
   email=request.form['txtEmail']
   clave1=request.form['txtClave1']
   clave2=request.form['txtClave2']


   if(name=='' or dir=='' or telf=='' or email=='' or clave1=='' or clave2==''):
      flash('Error existen Campos vacios')
      return redirect(url_for('registrar'))
      
   

   users.registro(name,dir,telf,email,clave1)
   # print(name,dir,telf,email,clave1,clave2)
   

   return redirect('/users/registrar/')
# admin
@app.route('/panel')
def panel():
   return render_template('index_admin.html')

@app.route('/modulo/clientes')
def mClientes():
   return render_template('admin/clientes_registrados.html')

@app.route('/modulo/productosIngresados' , methods=['POST','GET'])
def mProductosI():
   productos = productosIngresados.consulta()
   proveedores = productosIngresados.consultaProveedor()
   #if request.method=='POST':
   #   proveedor = request.form['proveedor']
   #   empresa = request.form['empresa']
   #   nombre = request.form['nombre']
   #   precio = request.form['precio']
   #   cantidad = request.form['cantidad']
   #   productosIngresados.registro(proveedor,empresa,nombre,precio,cantidad) 
   #   return redirect(url_for('mProductosI')) 
   return render_template('admin/productos_ingresados.html', productos=productos, proveedores=proveedores)

@app.route('/crearProveedor',  methods=['POST','GET'])
def crearProveedor():
   if request.method=='POST':
      nombre = request.form['nombre']
      ruc = request.form['ruc']
      direccion = request.form['direccion']
      telefono = request.form['telefono']
      email = request.form['email']
      productosIngresados.registroProveedor(nombre,ruc,direccion,telefono,email) 
      return redirect(url_for('mProductosI')) 
   return render_template('admin/productos_ingresados.html')

@app.route('/registrarProducto',  methods=['POST','GET'])
def registrarProducto():
    if request.method=='POST':
       proveedor = request.form['proveedores']
       nombre = request.form['nombre']
       precio = request.form['precio']
       cantidad = request.form['cantidad']
       _imagen = request.files['imagen']
       now = datetime.now()
       tiempo = now.strftime("%Y%H%M%S")
       if _imagen.filename != '' :
        nuevaImagen = tiempo + _imagen.filename
        _imagen.save("static/imagen/"+nuevaImagen) 
       # _imagen.save("../static/imagen"+nuevaImagen) 
        productosIngresados.registro(proveedor,nombre,precio,cantidad,nuevaImagen) 
        return redirect(url_for('mProductosI')) 
    return render_template('admin/productos_ingresados.html')


@app.route('/modulo/productosVendidos')
def mProductosV():
   return render_template('admin/productos_vendidos.html')

@app.route('/modulo/reservas')
def mReservas():
   return render_template('admin/reservas.html')

@app.route('/modulo/inventario')
def mInventario():
   return render_template('admin/inventario.html')

# cliente 
@app.route('/cliente/almacenados')
def almacenados():
   return render_template('cliente/almacenados.html')

@app.route('/cliente/reserva')
def reservaCliente():
   return render_template('cliente/productos_cliente.html')



# @app.route('/ejemplo')
# def ejemplo():
#    return render_template('aqui la ruta')








if __name__=='__main__':
    app.run(debug=True)
