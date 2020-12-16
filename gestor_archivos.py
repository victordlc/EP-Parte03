
import sqlite3

def listarproductosbd():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    consulta =  """ SELECT * FROM producto """
    cursor = conexion.cursor()
    cursor.execute(consulta)
    productos = cursor.fetchall()

    

    for producto in productos:
        print(str(producto[0]) + ") " + str(producto[1]) + ", " + str(producto[2]) + ", " + str(producto[3]))
    conexion.close()

    

    
def agregarproducto(nom,cod,pre):
    conexion = sqlite3.connect("ventas.db")
    consulta = """INSERT INTO 
                PRODUCTO(NOMBRE,CODIGO,PRECIO)
                VALUES('"""+nom+"""','"""+cod+"""',"""+pre+""") """
          
    cursor = conexion.cursor()
    cursor.execute(consulta)

    conexion.commit()
    conexion.close()

def eliminarproducto(cod):
    conexion = sqlite3.connect("ventas.db")
    consulta = """ DELETE FROM PRODUCTO WHERE CODIGO = '"""+cod+"""' """

    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
    
def modificarproducto(cod,nom,pre):
    conexion = sqlite3.connect("ventas.db")
    consulta = """ UPDATE PRODUCTO 
                SET
                    
                    NOMBRE = '"""+nom+"""',
                    PRECIO ="""+pre+"""
                WHERE
                    CODIGO = '"""+cod+"""'
            """

    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()