from flask import Flask 
from flask import render_template,request,redirect,flash,url_for
from datetime import datetime
from random import randint
from modules.backCliente.modulo_reserva_cliente import ints,alm,eliminar,bebidas,carnes,vegetales,update,eed
#solo import aqui
from flask.helpers import url_for
# from de module aqui
from modules.users import users
#from modules.modulos import almaceje,edit,resiva
#from backCliente.modulo_reserva_cliente import ver
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
   formulario,elim=alm.almacenados()
   print(formulario)
   return render_template('cliente/almacenados.html',formulario=formulario,elim=elim)


## restaurar

@app.route('/restaurar/<int:id>')
def restaurar(id):
    alm.restaurar([id])
    return redirect(url_for('almacenados'))


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

@app.route('/cliente/reservar/')
def reservar():

   return render_template('cliente/reservar.html')

@app.route('/reservar', methods=['POST'])
def reser():
   nombre=request.form['txtNombre']
   cantidad=request.form['txtCantidad']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cantidad =='' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('reservar'))

   ints.resr(nombre , cantidad,cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/reservar/')

### limpieza 
@app.route('/cliente/limpieza/')
def resert():

   return render_template('cliente/limpieza.html')

@app.route('/reservar', methods=['POST'])
def resr():
   nombre=request.form['txtNombre']
   cantidad=request.form['txtCantidad']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cantidad == '' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('reservar'))

   ints.resr(nombre , cantidad,cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/limpieza/')




###  bebidas 

@app.route('/cliente/bebidas/')
def rese():

   return render_template('cliente/bebidas.html')

@app.route('/bebid', methods=['POST'])
def bbs():
   nombre=request.form['txtNombre']
   cantidad=request.form['txtCantidad']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cantidad == '' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('rese'))

   bebidas.beb(nombre ,cantidad, cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/bebidas/')


## carnes
@app.route('/cliente/carnes/')
def crn():

   return render_template('cliente/carnes.html')

@app.route('/carnes', methods=['POST'])
def crs():
   nombre=request.form['txtNombre']
   cantidad=request.form['txtCantidad']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cantidad == '' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('rese'))

   carnes.car(nombre ,cantidad, cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/carnes/')

## vegetales

@app.route('/cliente/vegetales/')
def veget():

   return render_template('cliente/vegetales.html')

@app.route('/vegetales', methods=['POST'])
def vgt():
   nombre=request.form['txtNombre']
   cantidad=request.form['txtCantidad']
   cedula=request.form['txtCedula']
   correo=request.form['txtCorreo']
   fecha=request.form['txtFecha']

   if(nombre=='' or cantidad == '' or cedula==''  or correo=='' or fecha=='' ):
      flash('Error existen Campos vacios')
      return redirect(url_for('rese'))

   vegetales.ve(nombre , cantidad,cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect('/cliente/vegetales/')
#
#
# editar 
@app.route('/cliente/editar/')
def actua():

   return render_template('cliente/edit.html')

@app.route('/update', methods=['POST'])
def act():
   if request.method== 'POST':
    nombre=request.form['txtNombre']
    cantidad=request.form['txtCantidad']
    cedula=request.form['txtCedula']
    correo=request.form['txtCorreo']
    fecha=request.form['txtFecha']

    if(nombre=='' or cantidad == '' or cedula==''  or correo=='' or fecha=='' ):
       flash('Error existen Campos vacios')
       return redirect(url_for('almacenados'))

   update.actualizar(nombre ,cantidad, cedula,correo,fecha)
   #print(nombre , cedula,correo,fecha)
   return redirect(url_for('almacenados'))


@app.route('/edit/<int:cedula>')
def editrs(cedula): 
    formulario=eed.editaa([cedula])
    return render_template('/cliente/edit.html',formulario=formulario)




### funciona pero no guarda correctamente y no muestra ver por que error en formulario si se cambia la cedula no vale

# @app.route('/cliente/almacenados')
# def almacenados():
#    formulario=alm.almacenados()
#    print(formulario)
#    return render_template('cliente/almacenados.html',formulario=formulario)

# # almacenados()

# @app.route('/destroy/<int:cedula>')
# def destroy(cedula):
#     el=eliminar.dest([cedula])

#     return redirect('/cliente/almacenados')

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

if __name__=='__main__':
    app.run(debug=True)
