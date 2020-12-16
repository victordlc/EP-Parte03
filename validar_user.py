

import sqlite3
import Menu



us=input("Usuario: ")
pas=input("Constraseña: ")

conexion = sqlite3.connect("ventas.db")


consulta="""SELECT* FROM usuario WHERE usuario='{0}' AND CLAVE='{1}'""".format(us,pas)
cursor = conexion.cursor()
cursor.execute(consulta)
usu=cursor.fetchall()
for a in usu:
    try:
        print(a)
        conexion.close()
        if (us == a[1] and pas == a[2]):
            Menu.xd()
            Menu.opciones()
            pass
        else:
        
            print("....Error Error Error....")
            pass
        pass
    except Exception as e:
        print("Error :" + e)
        pass
    pass