from flask import Flask 
from flask import render_template,request,redirect, flash, url_for
from datetime import datetime
from random import randint
from modules.users import users, Persona





app=Flask(__name__)
app.secret_key="Develoteca"
# index 
@app.route('/')
def index():
    
    return render_template('index.html')

# users 
@app.route('/users/login')
def login():
   users.admin()
   return render_template('users/login.html')

@app.route('/users/login_admin', methods=['GET', 'POST'])
def loguin():
   if request.method == 'POST':
      email=request.form['email']
      password= request.form['password']
      print(email,password)
      correcto = users.loguin(email, password)
      if (correcto==0):
         flash ("Usuario y contraseña no validos")
         return redirect(url_for('login'))
      if (correcto==1):
         if(email == 'MADJS@gmail.com'):
            return redirect(url_for('panel'))

         return redirect(url_for('index'))


@app.route('/users/registrar/', methods=['GET','POST'])
def registrar():
      form=Persona()

      if form.validate_on_submit():
         try:
            name=request.form['nombre']
            dir=request.form['direccion']
            telf=int(request.form['telefono'])
            email=request.form['correo']
            clave1=request.form['clave']
            print(type(name),dir,telf,email,clave1)
            
            if telf<0:
               flash('Error en el campo telefono')
               return redirect(url_for('registrar'))

            
            users.registro(name,dir,telf,email,clave1)
            return redirect('/users/registrar/')
         except ValueError:
            # Esta captura el error cuando se manda un string en el telefono
            flash('Esta ingresando datos erroneos')
            return redirect(url_for('registrar'))

      return render_template('users/registrar.html', form=form)


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
