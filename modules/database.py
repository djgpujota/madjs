import psycopg2


def abrirConexion():
        con= psycopg2.connect(
            host = 'localhost',
            database = 'Proyecto',
            user = 'postgres',
            password  = '152018'
            )
        return con 

def cerrarConexion(con):
    con.close()






