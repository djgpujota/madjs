# MODULOS se comunica con los modulos inferiores, envia datos a la db y envia datos a las rutas 

from modules.database import con,cerrarConexion
def resiva(): 
        cone=con
        cursor= cone.cursor()
        cursor.execute('SELECT * FROM rol')
        print(cursor.fetchall())
        
        cone.commit
       
        


resiva()