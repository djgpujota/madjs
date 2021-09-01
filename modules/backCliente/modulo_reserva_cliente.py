import re
from ..database import abrirConexion ,cerrarConexion

conexion=abrirConexion()

def insert ():
  ls='hola'
  print(ls)
  return ls
# insert()


# def resiva():
#         cursor= conexion.cursor()
#         cursor.execute('SELECT * FROM rol')
#         form=cursor.fetchall()
#         print(form)
#         return form

# resiva()


#### ingresar la reserva 

class ints():

    def resr(nombre,cantidad,cedula,correo,fecha):
      nombre=nombre
      cantidad=cantidad
      cedula=cedula
      correo=correo
      fecha=fecha

      cursor=conexion.cursor()

      cursor.execute("select id_ordenes_clientes from ordenes_clientes")
      id = cursor.fetchall()

      if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_ordenes_clientes from ordenes_clientes")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("select id_personas from personas WHERE nombre_personas='{}'".format(nombre))
            b1 = cursor.fetchone()
            b1=b1[0]
            cursor.execute("select id_producto_ingresado from nombre_producto_ingresado='{}'".format())
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            
            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Productos de limpieza','{}',0)".format(a2,b1,c2,nombre,cantidad,cedula,correo,fecha))
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Productos de limpieza','{}',0)".format(value,value1,value2,nombre,cantidad,cedula,correo,fecha))

            conexion.commit()



##### productos de bebidas



class bebidas():

    def beb(nombre,cantidad,cedula,correo,fecha):
      nombre=nombre
      cantidad=cantidad
      cedula=cedula
      correo=correo
      fecha=fecha

      cursor=conexion.cursor()

      cursor.execute("select id_ordenes_clientes from ordenes_clientes")
      id = cursor.fetchall()

      if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_ordenes_clientes from ordenes_clientes")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("select id_personas from ordenes_clientes")
            b1 = cursor.fetchall()
            b2=(len(b1))+1
            cursor.execute("select id_producto_ingresado from ordenes_clientes")
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Bebidas','{}',0)".format(a2,b2,c2,nombre,cantidad,cedula,correo,fecha))
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Bebidas','{}',0)".format(value,value1,value2,nombre,cantidad,cedula,correo,fecha))

            conexion.commit()



###  narnes 

class carnes():

    def car(nombre,cantidad,cedula,correo,fecha):
      nombre=nombre
      cantidad=cantidad
      cedula=cedula
      correo=correo
      fecha=fecha

      cursor=conexion.cursor()

      cursor.execute("select id_ordenes_clientes from ordenes_clientes")
      id = cursor.fetchall()

      if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_ordenes_clientes from ordenes_clientes")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("select id_personas from ordenes_clientes")
            b1 = cursor.fetchall()
            b2=(len(b1))+1
            cursor.execute("select id_producto_ingresado from ordenes_clientes")
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Carnes','{}',0)".format(a2,b2,c2,nombre,cantidad,cedula,correo,fecha))
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Carnes','{}',0)".format(value,value1,value2,nombre,cantidad,cedula,correo,fecha))

            conexion.commit()




### vegetales
class vegetales():

    def ve(nombre,cantidad,cedula,correo,fecha):
      nombre=nombre
      cantidad=cantidad
      cedula=cedula
      correo=correo
      fecha=fecha

      cursor=conexion.cursor()

      cursor.execute("select id_ordenes_clientes from ordenes_clientes")
      id = cursor.fetchall()

      if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_ordenes_clientes from ordenes_clientes")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("select id_personas from ordenes_clientes")
            b1 = cursor.fetchall()
            b2=(len(b1))+1
            cursor.execute("select id_producto_ingresado from ordenes_clientes")
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Vegetales','{}',0)".format(a2,b2,c2,nombre,cantidad,cedula,correo,fecha))
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},{},'{}','Vegetales','{}',0)".format(value,value1,value2,nombre,cantidad,cedula,correo,fecha))

            conexion.commit()



#### aqui se muestran los datos de la reserva 

class alm():

  def almacenados():
    cursor=conexion.cursor()
    query="SELECT * FROM ordenes_clientes WHERE estado=0"
    cursor.execute(query)
    formulario=cursor.fetchall()
    formulario=formulario
    #print(formulario)
    que="SELECT * FROM ordenes_clientes WHERE estado=1"
    cursor.execute(que)
    elim=cursor.fetchall()
    elim=elim
    conexion.commit()
    return formulario,elim

####restaurar

  def restaurar(id):
        cursor=conexion.cursor()
        query=cursor.execute("UPDATE ordenes_clientes SET estado=0 WHERE id_ordenes_clientes=%s",(id))
      #   cursor.execute("SELECT * FROM ordenes_clientes WHERE cedula_ordenes_cliente=%s",(cedula))
      #   cursor.execute(query)
        conexion.commit()
      #   return query

### aqui se eliminan los atos de la reserva 

# class eliminar():

#  def dest(cedula):
#     cur=conexion.cursor()  
#     elm=cur.execute("DELETE FROM ordenes_clientes WHERE id_ordenes_clientes=%s",(cedula))
#     conexion.commit()
#     return elm


### aqui para editar las reservas 

class update():

    def actualizar(nombre,cantidad,cedula,correo,fecha):
      nombre=nombre
      cantidad=cantidad
      cedula=cedula
      correo=correo
      fecha=fecha

      cursor=conexion.cursor()

      cursor.execute("select id_ordenes_clientes from ordenes_clientes")
      id = cursor.fetchall()

      if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_ordenes_clientes from ordenes_clientes")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("select id_personas from ordenes_clientes")
            b1 = cursor.fetchall()
            b2=(len(b1))+1
            cursor.execute("select id_producto_ingresado from ordenes_clientes")
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            # cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},'{}','vegetales','{}')".format(a2,b2,c2,nombre,cedula,correo,fecha))
            query="UPDATE  ordenes_clientes SET nombre_ordenes_cliente=%s,cantidad_ordenes_cliente=%s,correo_ordenes_clientes=%s,fecha_ordenes_cliente=%s WHERE ordenes_clientes.cedula_ordenes_cliente=%s;"
            # query="UPDATE  ordenes_clientes SET ({},{},{},12,'{}','{}','vegetales','{}' WHERE cedula_ordenes_cliente={})".format(a2,b2,c2,nombre,cedula,correo,fecha,cedula)
            datos=(nombre,cantidad,correo,fecha,cedula)
            data=cursor.execute(query,datos)
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            # cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},'{}','vegetales','{}')".format(value,value1,value2,nombre,cedula,correo,fecha))
            # query="UPDATE  ordenes_clientes SET ({},{},{},12,'{}','{}','vegetales','{}' WHERE cedula_ordenes_cliente={})".format(value,value1,value2,nombre,correo,fecha,cedula)
            query="UPDATE  ordenes_clientes SET nombre_ordenes_cliente=%s,cantidad_ordenes_cliente=%s,correo_ordenes_clientes=%s,fecha_ordenes_cliente=%s WHERE cedula_ordenes_cliente=%s;"
            # query="UPDATE  ordenes_clientes SET id_ordenes_clientes,id_clientes,numero_ordenes_clientes,subtotal_ordenes_clientes,nombre_ordenes_cliente,,correo_ordenes_cliente=,categoria_ordenes_cliente,fecha_ordenes_cliente WHERE cedula_ordenes_clientes;".format(value,value1,value2,nombre,cedula,correo,fecha,cedula)
            datos=(nombre,cantidad,correo,fecha,cedula)
            data=cursor.execute(query,datos)
            conexion.commit()
      return data

# @app.route('/edit/<int:cedula>')

class eed():
 def editaa(cedula): 
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM ordenes_clientes WHERE cedula_ordenes_cliente=%s",(cedula))
    formulario=cursor.fetchall()
    conexion.commit()
    return formulario
    # return render_template('edit.html',formulario=formulario)





# class eddi():

#   def editara(cedula):
#     cursor=conexion.cursor()
#     form=cursor.execute("SELECT * FROM ordenes_clientes WHERE id_ordenes_clientes=%s",(cedula))
#     formulario=cursor.fetchall()
#     conexion.commit()
#     formulario=formulario
#     #print(formulario)
#     conexion.commit()
#     return formulario


class eliminar():

 def dest(cedula):
    cur=conexion.cursor()  
    elm=cur.execute("UPDATE ordenes_clientes SET estado=1  WHERE id_ordenes_clientes=%s",(cedula))
    conexion.commit()
    return elm


# class eliminar():

#  def dest(cedula):
#     cur=conexion.cursor()  
#     elm=cur.execute("DELETE FROM ordenes_clientes WHERE id_ordenes_clientes=%s",(cedula))
#     conexion.commit()
#     return elm

# def into():
#     # sql="INSERT INTO 'Formulario'('cedula','nombre','apellido','edad','telefno','correo','pregunta1','pregunta2','pregunta3') VALUES (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer')"
#     cur=conexion.cursor()
#     sql="INSERT INTO ordenes_clientes (id_ordenes_clientes,id_clientes,numero_ordenes_clientes,fecha_ordenes_clientes,subtotal_ordenes_clientes,hora_ordenes_clientes,cedula_ordenes_cliente) VALUES (2,2,2,'03-11-2021',21,'12:00',1109825367) "
#     cur.execute(sql)
#     print(sql)
#     conexion.commit()
#     conexion.close()










