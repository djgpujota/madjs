# MODULOS se comunica con los modulos inferiores, envia datos a la db y envia datos a las rutas 
from database import con

def resiva():
        cone=con
        cursor= cone.cursor()
        cursor.execute('SELECT * FROM rol')
        print(cursor.fetchall())
        
        cone.commit
       
        


resiva()