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

    def resr(nombre,cedula,correo,fecha):
      nombre=nombre
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
            cursor.execute("select id_clientes from ordenes_clientes")
            b1 = cursor.fetchall()
            b2=(len(b1))+1
            cursor.execute("select numero_ordenes_clientes from ordenes_clientes")
            c1 = cursor.fetchall()
            c2=(len(c1))+1
            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},'{}','{}')".format(a2,b2,c2,nombre,cedula,correo,fecha))
            conexion.commit()
      else:
            value=1
            value1=1
            value2=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into ordenes_clientes values ({},{},{},12,'{}',{},'{}','{}')".format(value,value1,value2,nombre,cedula,correo,fecha))

            conexion.commit()



#### aqui se muestran los datos de la reserva 

class alm():

  def almacenados():
    cursor=conexion.cursor()
    query="SELECT * FROM ordenes_clientes"
    cursor.execute(query)
    formulario=cursor.fetchall()
    formulario=formulario
    #print(formulario)
    conexion.commit()
    return formulario



### aqui se eliminan los atos de la reserva 

class eliminar():

 def dest(cedula):
    cur=conexion.cursor()  
    elm=cur.execute("DELETE FROM ordenes_clientes WHERE id_ordenes_clientes=%s",(cedula))
    conexion.commit()
    return elm


### aqui para editar las reservas 





# def into():
#     # sql="INSERT INTO 'Formulario'('cedula','nombre','apellido','edad','telefno','correo','pregunta1','pregunta2','pregunta3') VALUES (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer')"
#     cur=conexion.cursor()
#     sql="INSERT INTO ordenes_clientes (id_ordenes_clientes,id_clientes,numero_ordenes_clientes,fecha_ordenes_clientes,subtotal_ordenes_clientes,hora_ordenes_clientes,cedula_ordenes_cliente) VALUES (2,2,2,'03-11-2021',21,'12:00',1109825367) "
#     cur.execute(sql)
#     print(sql)
#     conexion.commit()
#     conexion.close()

class buscar():
  def busquedaProducto(p):
    conexion=abrirConexion()
    cursor= conexion.cursor()
    cursor.execute("select * from producto_ingresado Where nombre_producto_ingresado = '{}';".format(p))
    consulta=cursor.fetchall()
    if consulta==[]:
      print('Producto No Encontrado')
    else:  
     print(consulta,'Holaaaaaaaaaaaaaaaaaaaaaaa')
     return consulta