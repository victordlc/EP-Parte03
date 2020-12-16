


import gestor_archivos


def verificaruser(us):
    user=gestor_archivos.listarusuario(us)
    return user

def verificarcontra(con):
    contra=gestor_archivos.listarCONTRASENIA(con)
    return contra

def Agregar():
     print("-- Agregar producto --")
     nom=str(input("Ingrese nombre de producto: "))
     cod=input("Ingrese codigo de producto: ")
     pre=input("Ingrese precio de producto: ")
     gestor_archivos.agregarproducto(nom, cod, pre)
     
def Eliminar():
     print("-- Eliminar producto --")
     ide=input("Ingrese codigo de producto a eliminar: ")
     gestor_archivos.eliminarproducto(ide)
def Modificar():
     print("-- Modificar producto --")
     cod=input("Ingrese el codigo del producto a modificar: ")
     nom=str(input("Ingrese nombre de producto: "))
     pre=input("Ingrese precio de producto: ")
     gestor_archivos.modificarproducto(cod,nom,pre)
    
def Listar():
    print("-- Mostrar Contenido --")
    gestor_archivos.listarproductosbd()
    print("\n")

def Error():
    print("Ingrese de nuevo...\n")
    
def xd():
    print("** Datos Producto **")
    print("1. Listar")
    print("2. Agregar")
    print("3. Eliminar")
    print("4. Modificar")
    print("5. Salir")
    
def Salir():
    print("Muchas Gracias")
    return 0;

def opciones():
    op=1
    while op!=5:
        op=int(input("Ingrese opción: "))
        if op==1:
            Listar()
            xd()
        if op==2:
            Agregar()
            xd()
        if op==3:
            Eliminar()
            xd()
        if op==4:
            Modificar()
            xd()
        if op==5:
           Salir()
        if op<1 or op>6:
            Error()