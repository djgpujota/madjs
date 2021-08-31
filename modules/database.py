import psycopg2



def abrirConexion():
    try:
        con= psycopg2.connect(
            host = 'localhost',
            database = 'Proyecto',
            user = 'postgres',
            password  = 'Negruras123.'
            )
        return con

    except:
        print('Error al conectarse ')    

def cerrarConexion(con):
    con.close()



