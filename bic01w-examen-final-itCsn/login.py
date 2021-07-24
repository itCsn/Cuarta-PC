BASE_DE_DATOS = {}


def crear_usuario():
    usuario = input("Ingrese su usuario: ")

    if usuario in BASE_DE_DATOS.keys():
        print(f"El usuario {usuario} ya existe!" )
        while usuario not in BASE_DE_DATOS.keys():
            usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        BASE_DE_DATOS[usuario] = clave

    if usuario not in BASE_DE_DATOS.keys():
        clave = input("Ingrese su clave: ")
        BASE_DE_DATOS[usuario] = clave
        print(f"El usuario {usuario} se creo con éxito")
    
    return usuario    

def ingresar():
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if clave == BASE_DE_DATOS[usuario]:
        print(f"Bienvenido {usuario}")
        return True
    else:
        print("Credenciales incorrectas")
        return False


def iniciar():
    print("Ingrese (1) para crear usuario")
    print("Ingrese (2) para crear ingresar")
    print("Ingrese (3) para crear salir")
    opcion = int(input("Opcion: "))
    lista = [1, 2, 3]
    
    while opcion not in lista:
        print("Opcion invalida!")
        opcion = int(input("Opcion: "))

    if opcion == 1:
        crear_usuario()
    elif opcion == 2:
        ingresar()
    elif opcion == 3:
        print("Chau!")
    
    print("")


if __name__ == "__main__":
    iniciar()
