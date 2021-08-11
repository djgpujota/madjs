import psycopg2


try:
            con= psycopg2.connect(
                host = 'localhost',
                database = 'prueba',
                user = 'postgres',
                password  = '1234'
                )

except:
            print('Error al conectarse ')    

def cerrarConexion():
    con.close()




