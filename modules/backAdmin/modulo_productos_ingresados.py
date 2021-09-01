from ..database import abrirConexion,cerrarConexion
# from datetime import datetime

class productosIngresados():
        def consulta():
         abrir = abrirConexion()
         cursor = abrir.cursor()
         cursor.execute("select * from producto_ingresado")
         extraer = cursor.fetchall()
         cerrarConexion(abrir)
         return extraer

        def consultaProveedor():
         abrir = abrirConexion()
         cursor = abrir.cursor()
         cursor.execute("select * from proveedor")
         extraer = cursor.fetchall()
         cerrarConexion(abrir)
         return extraer


        def registro(proveedor,nombre,precio,cantidad,imagen):
         # Llammamos a la conexion a la base de datos
         con= abrirConexion()
         conexion=con
         #Creamos el cursor con la conexion anteriormente llamado
         cursor= conexion.cursor()
         cursor.execute("select id_producto_ingresado from producto_ingresado")
         id = cursor.fetchall()
         # Validaciones de id 
         # si existe algun dato registrado  
         if(id!=[]):
          cursor.execute("select id_producto_ingresado from producto_ingresado")
          a = cursor.fetchall()
          a1 = (len(a))+1
          cursor.execute("insert into producto_ingresado values ({},{},'{}',{},{},'{}')".format(a1,proveedor,nombre,precio,cantidad,imagen))
          conexion.commit()
         else:
          a2 = 1
          cursor.execute("insert into producto_ingresado values ({},{},'{}',{},{},'{}')".format(a2,proveedor,nombre,precio,cantidad,imagen))
          conexion.commit()
         cerrarConexion(conexion)

        def registroProveedor(nombre,ruc,direccion,telefono,email):
         # Llammamos a la conexion a la base de datos
         con= abrirConexion()
         conexion=con
         #Creamos el cursor con la conexion anteriormente llamado
         cursor= conexion.cursor()
         cursor.execute("select id_proveedor from proveedor")
         id = cursor.fetchall()
         # Validaciones de id 
         # si existe algun dato registrado  
         if(id!=[]):
          cursor.execute("select id_proveedor from proveedor")
          a = cursor.fetchall()
          a1 = (len(a))+1
          cursor.execute("insert into proveedor values ({},'{}','{}','{}',{},'{}')".format(a1,nombre,ruc,direccion,telefono,email))
          conexion.commit()
         else:
          a2 = 1
          cursor.execute("insert into proveedor values ({},'{}','{}','{}',{},'{}')".format(a2,nombre,ruc,direccion,telefono,email))
          conexion.commit()
         cerrarConexion(conexion)
    