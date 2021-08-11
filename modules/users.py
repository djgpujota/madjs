from modules.database import con,cerrarConexion
class users():
    

        
        
    def registro(name,dir,telf,email,clave1):
        name=name
        dir=dir
        telf=telf
        email=email
        clave1=clave1

        # Llammamos a la conexion a la base de datos
        conexion=con
        #Creamos el cursor con la conexion anteriormente llamado
        cursor= conexion.cursor()


        # cursor.execute('insert into personas (id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values (2,%s,%s,%s,%s,%s)')
        cursor.execute("select id_personas from personas")
        id = cursor.fetchall()

        if(id!=[]):
            print('tiene datos')
            print(id)
            cursor.execute("select id_personas from personas")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("insert into personas values ({},2,'{}','{}',{},'{}','{}')".format(a2,name,dir,telf,email,clave1))
            # (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) 
            conexion.commit()
        
        else:
            value=1
            # cursor.execute("insert into personas (id_personas,id_rol,nombre_personas,dir_personas,telf_personas,email_personas,clave_personas) values ({},2,'dylan','12',12,'12','12')".format(value)

            cursor.execute("insert into personas values ({},2,'{}','{}',{},'{}','{}')".format(value,name,dir,telf,email,clave1))

            conexion.commit()
        
        
        cerrarConexion()
        
# users.registro('Dylan2','alal',999,'das@gmail.com','1234')