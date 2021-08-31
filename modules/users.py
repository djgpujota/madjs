# Importaciones externas
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from wtforms.fields.simple import PasswordField

# Importaciones de modulos internos
from modules.database import cerrarConexion,abrirConexion


class Persona(FlaskForm):
    nombre=StringField("Nombre",validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(max=20, min=5, message="El campo debe tener entre 5 y 20 caracteres")
    ])
    direccion=StringField("Direccion",validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min=9, max=50, message="El campo debe tener entre 9 y 50 caracteres.")
    ])
    telefono=StringField("Telefono",validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min=7, max=11, message="El campo debe tener entre 9 y 11 caracteres.")
    ])
    correo= StringField("Email",validators=[
        DataRequired(message="El campo es obligatorio"),
        Email(message="Email erroneo")
    ])
    clave=PasswordField("Clave",validators=[
        DataRequired(message="El campo es obligatorio"),
        Length(min=4, max=10, message="Se requiere de 4 a 10 caracteres")
    ])
    submit=SubmitField('Enviar')


class users():
    

        
        
    def registro(name,dir,telf,email,clave1):
        name=name
        dir=dir
        telf=telf
        email=email
        clave1=clave1
        # Llammamos a la conexion a la base de datos
        con= abrirConexion()
        conexion=con
        #Creamos el cursor con la conexion anteriormente llamado
        cursor= conexion.cursor()

        cursor.execute("select id_personas from personas")
        id = cursor.fetchall()
        # Validaciones de id 
        # si existe algun dato registrado  
        if(id!=[]):
            
            cursor.execute("select id_personas from personas")
            a1 = cursor.fetchall()
            a2= (len(a1))+1
            cursor.execute("insert into personas values ({},2,'{}','{}',{},'{}','{}',0)".format(a2,name,dir,telf,email,clave1))
            conexion.commit()
        
        else:
            # Validacion por si no existe ningun dato registrado
            value=1

            cursor.execute("insert into personas values ({},2,'{}','{}',{},'{}','{}',0)".format(value,name,dir,telf,email,clave1))

            conexion.commit()
        
        
        cerrarConexion(conexion)

    def actualizarCliente(id,name,dir,telf,email,clave1):
        id=id
        name=name
        dir=dir
        telf=telf
        email=email
        clave1=clave1
        # Llammamos a la conexion a la base de datos
        con= abrirConexion()
        conexion=con
        #Creamos el cursor con la conexion anteriormente llamado
        cursor= conexion.cursor()

        cursor.execute("update personas set nombre_personas='{}', dir_personas='{}', telf_personas={}, email_personas='{}', clave_personas='{}' where id_personas={}".format(name,dir,telf,email,clave1,id))
        conexion.commit()
        
        
        
        cerrarConexion(conexion)




# users.registro('Dylan2','alal',999,'das@gmail.com','1234')