from flask import Flask 
from flask import render_template,request,redirect,flash,url_for
from datetime import datetime
from random import randint
from modules.users import users,Persona
from flask.helpers import url_for
from modules.backCliente.modulo_reserva_cliente import ints,alm,eliminar,buscar

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

#cliente
@app.route('/cliente/almacenados')
def almacenados():
   formulario=alm.almacenados()
   print(formulario)
   return render_template('cliente/almacenados.html',formulario=formulario)

# almacenados()

@app.route('/destroy/<int:cedula>')
def destroy(cedula):
    el=eliminar.dest([cedula])

    return redirect('/cliente/almacenados')



## comentar o descomentar almacenaje
# def almacena():
#    formulario=alm.almacenados()
#    #print(formulario)
#    return formulario

# almacena()
## comentar o descomentar  el insert into

@app.route('/cliente/reservar/',methods=['POST','GET'])
def reservar():
 if request.method=='POST':
  busqueda=request.form['producto']
  consulta=buscar.busquedaProducto(busqueda)
  return render_template('cliente/reservar.html', consulta=consulta)
 return render_template('cliente/reservar.html')

@app.route('/reservar', methods=['POST'])
def reser():
   nombre=request.form['txtNombre']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('reservar'))

   ints.resr(nombre , cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/reservar/')

#ejemplo

# @app.route('/ejemplo')
# def ejemplo():
#    ver = insert()
#    pw=resiva()
#    print(pw)
#    i=into()
#    print(i)
#    return ver, pw
# ejemplo()


#@app.route('/reservar/busqueda',methods=['POST'])
#def busqueda():
 #if request.method=='POST':
  #busqueda=request.form['producto']
 #buscar.busquedaProducto(busqueda)
 #return redirect(url_for('reservar'))



if __name__=='__main__':
    app.run(debug=True)
