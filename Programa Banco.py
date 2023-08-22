"""Programa realizado por:
    Annuar Abouharb
    Jean Odriozola
    Maria Chang
    Moises Londoño
    Luis Amias"""
from string import punctuation

database = []



def cuenta():
    account = {
        "nombre": None,
        "apellido": None,
        "cedula": None,
        "usuario": None,
        "clave": None,
        "posicion consolidada": 0.0,
    }
    return account

def validarClave(contraseña):
    longitud = False
    minuscula = False
    mayuscula = False
    caracter_especial = False
    numero = False
    if len(contraseña) >= 6:
        longitud = True
    for i in contraseña:
        if i.islower():
            minuscula = True
        if i.isupper():
            mayuscula = True
        if i in punctuation:
            caracter_especial = True
        if i.isdigit():
            numero = True
    if longitud and minuscula and mayuscula and caracter_especial and numero:
        return True
    else:
        return False

def crearCuenta():
    print("\nExcelente. Ha introducido la opcion 1. (Crear cuenta)\n")
    registro = cuenta()
    nombre = input("Introduce el nombre: ")
    while not nombre.isalpha():
        print("\nEl nombre no debe tener caracteres especiales ni numeros.")
        nombre = input("Nombre: ")
    print("\nNombre validado.")
    apellido = input("\nIntroduce el apellido: ")
    while not apellido.isalpha():
        print("\nEl apellido no debe tener caracteres especiales ni numeros.")
        apellido = input("Apellido: ")
    print("\nApellido validado.")
    cedula = input("\nCedula: ")
    while not cedula.isdigit():
        print("\nLa cedula no debe tener caracteres especiales ni letras.")
        cedula = input("Cedula: ")
    print("\nCedula validada.\n")
    usuario = input("Introduce tu nombre de usuario: ")
    print("\nUsuario validado.")
    print("\nRequisitos para la creacion de la clave.")
    print("* Que tenga como minimo 6 caracteres.")
    print("* Que tenga al menos una letra en mayuscula y en minusculas.")
    print("* Que tenga al menos un caracter especial y un numero")
    print("Ejemplo: Pablo123@")
    clave = input("Introduce la clave: ")
    validacion_clave = validarClave(clave)
    while not validacion_clave:
        print("\nIntroduce una clave que cumpla con los requisitos.")
        print("* Que tenga como minimo 6 caracteres.")
        print("* Que tenga al menos una letra en mayuscula y en minusculas.")
        print("* Que tenga al menos un caracter especial y un numero")
        print("Ejemplo: Pablo123@\n")
        clave = input("Introduce una clave valida: ")
        validacion_clave = validarClave(clave)
    print("\nClave validada.")
    registro["nombre"] = nombre
    registro["apellido"] = apellido
    registro["cedula"] = cedula
    registro["usuario"] = usuario
    registro["clave"] = clave
    saldo_inicial = 50.0
    registro["posicion consolidada"] += saldo_inicial
    existe = False
    for fila in database:
        if fila["cedula"] == cedula or fila["usuario"] == usuario:
            existe = True
            print("La persona con el usuario y/o cedula anteriormente introducida ya existe.")
    if existe == False:
        database.append(registro)
        print("\nUsuario registrado correctamente. Retornando al menu principal")



def depositoBancario():
    print("\nHa seleccionado la opcion 2. (Realizar un deposito bancario)\n")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("\nUsuario encontrado\n")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("\nUsuario y clave correcta.\n")
                print("Bienvenido! ",fila["nombre"]," ",fila["apellido"])
                monto = float(input("\nIntroduzca el monto a depositar en su cuenta: \n"))
                if monto > 0:
                    fila["posicion consolidada"] += monto
                    print("Monto introducido: ",monto)
                    print("Monto total: ",fila["posicion consolidada"])
                else:
                    print("\nError al introducir un monto. Intentalo de nuevo...\n")     
    if existe_usuario == False:
        print("\nEl usuario introducido no se encuentra registrado en el sistema.\n")
    else:
        if existe_clave == False:
            print("\nLa clave introducida es incorrecta...\n")
    

def retiroBancario():
    print("\nHa seleccionado la opcion 3. (Realizar un retiro bancario)\n")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("\nUsuario encontrado\n")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("\nUsuario y clave correcta.\n")
                print("Bienvenido! ",fila["nombre"]," ",fila["apellido"])
                monto = float(input("\nIntroduzca el monto a retirar de su cuenta: "))
                if monto > fila["posicion consolidada"] or monto <= 0:
                    print("\nIntroduzca un monto menor o igual al saldo disponible de su cuenta. Intente de nuevo\n")
                elif monto > 0 and monto <= fila["posicion consolidada"]:
                    fila["posicion consolidada"] -= monto
                    print("Monto introducido: ",monto)
                    print("Monto total: ",fila["posicion consolidada"])
    if existe_usuario == False:
        print("\nEl usuario introducido no se encuentra registrado en el sistema.\n")
    else:
        if existe_clave == False:
            print("\nLa clave introducida es incorrecta...\n")



def consultarCuenta():
    print("\nHa seleccionado la opcion 4. (Consultar datos de una cuenta)\n")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("\nUsuario encontrado\n")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("\nUsuario y clave correcta. Mostrando los datos de la cuenta...\n")
                print("Nombre: ",fila["nombre"])
                print("Apellido: ",fila["apellido"])
                print("Cedula: ",fila["cedula"])
                print("Usuario: ",fila["usuario"])
                print("Posicion Consolidada: ",fila["posicion consolidada"],"\n")
    if existe_usuario == False:
        print("\nEl usuario introducido no se encuentra registrado en el sistema.\n")
    else:
        if existe_clave == False:
            print("\nLa clave introducida es incorrecta...\n")


def transferirACedula(persona,cedula,database):
    existe_cedula = False
    for fila in database:
        if fila["cedula"] == cedula:
            existe_cedula = True
            print("\nCedula encontrada.\n")
            print("Nombre: ",fila["nombre"])
            print("Apellido: ",fila["apellido"])
            monto = float(input("\nIntroduzca el monto a transferir: "))
            if monto > 0 and monto <= persona["posicion consolidada"]:
                persona["posicion consolidada"] -= monto
                fila["posicion consolidada"] += monto
                print("\nMonto transferido: ",monto)
                print("Saldo disponible en su cuenta: ",persona["posicion consolidada"])
            else:
                print("\nIntroduzca un monto correcto y/o que no supere su saldo disponible en la cuenta.\n")
    if existe_cedula == False:
        print("\nLa persona a la cual desea realizarle una transferencia no se encuentra en el sistema.\n")


def realizarTransferencia():
    print("\nHa seleccionado la opcion 5. (Realizar una transferencia bancaria)\n")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("\nUsuario encontrado\n")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("\nBienvenido! ",fila["nombre"]," ",fila["apellido"])
                cedula = input("\nIntroduzca la cedula de la persona a la que desea realizar la transferencia: \n")
                while not cedula.isdigit():
                    print("La cedula no debe tener caracteres especiales ni letras.\n")
                    cedula = input("Cedula: ")
                print("\nCedula procesada...")
                transferirACedula(fila,cedula,database)
    if existe_usuario == False:
        print("\nEl usuario introducido no se encuentra registrado en el sistema.")
    else:
        if existe_clave == False:
            print("\nLa clave introducida es incorrecta...")


def main():
    continuidad = True
    print("Hola, bienvenido/a al banco nacional, a continuacion le presentare las opciones que tenemos disponibles:\n")
    while continuidad:
        try:
            print("\n\nIntroduzca su opcion marcando cualquiera de los numeros indicados.")
            print("1.- Crear una Cuenta.")
            print("2.- Realizar un Deposito Bancario.")
            print("3.- Realizar un Retiro")
            print("4.- Consultar los datos de una cuenta.")
            print("5.- Realizar una transferencia a otro usuario.")
            print("6.- Salir del programa.")
            opcion = int(input("Opcion > "))
            if opcion == 1:
                crearCuenta()
            elif opcion == 2:
                depositoBancario()
                continue
            elif opcion == 3:
                retiroBancario()
                continue
            elif opcion == 4:
                consultarCuenta()
            elif opcion == 5:
                realizarTransferencia()
                continue
            elif opcion == 6:
                print("\nHasta luego!")
                continuidad = False
            else:
                raise Exception("Dato introducido invalido. Intente de nuevo.")
        except Exception as error:
            print("\nERROR: ",error)
main()