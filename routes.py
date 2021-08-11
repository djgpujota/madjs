from flask import Flask 
from flask import render_template,request,redirect
from datetime import datetime
from random import randint





app=Flask(__name__)

# index 
@app.route('/')
def index():
    
    return render_template('index.html')

# users 
@app.route('/users/login')
def loguin():
   return render_template('users/login.html')

@app.route('/users/registrar')
def registrar():
   return render_template('users/registrar.html')


# admin
@app.route('/panel')
def panel():
   return render_template('index_admin.html')

@app.route('/modulo/clientes')
def mClientes():
   return render_template('admin/clientes_registrados.html')

@app.route('/modulo/productosIngresados')
def mProductosI():
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












if __name__=='__main__':
    app.run(debug=True)
