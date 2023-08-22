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
    print("")
    print("")
    print("Excelente. Ha introducido la opcion 1. (Crear cuenta)")
    registro = cuenta()
    nombre = input("Introduce el nombre: ")
    while not nombre.isalpha():
        print("")
        print("El nombre no debe tener caracteres especiales ni numeros.")
        nombre = input("Nombre: ")
    print("")
    print("Nombre validado.")
    apellido = input("Introduce el apellido: ")
    while not apellido.isalpha():
        print("")
        print("El apellido no debe tener caracteres especiales ni numeros.")
        apellido = input("Apellido: ")
    print("")
    print("Apellido validado.")
    cedula = input("Cedula: ")
    while not cedula.isdigit():
        print("")
        print("La cedula no debe tener caracteres especiales ni letras.")
        cedula = input("Cedula: ")
    print("")
    print("Cedula validada.")
    print("")
    usuario = input("Introduce tu nombre de usuario: ")
    print("")
    print("Usuario validado.")
    print("")
    print("Requisitos para la creacion de la clave.")
    print("* Que tenga como minimo 6 caracteres.")
    print("* Que tenga al menos una letra en mayuscula y en minusculas.")
    print("* Que tenga al menos un caracter especial y un numero")
    print("Ejemplo: Pablo123@")
    clave = input("Introduce la clave: ")
    validacion_clave = validarClave(clave)
    while not validacion_clave:
        print("")
        print("Introduce una clave que cumpla con los requisitos.")
        print("* Que tenga como minimo 6 caracteres.")
        print("* Que tenga al menos una letra en mayuscula y en minusculas.")
        print("* Que tenga al menos un caracter especial y un numero")
        print("Ejemplo: Pablo123@")
        print("")
        clave = input("Introduce una clave valida: ")
        validacion_clave = validarClave(clave)
    print("")
    print("Clave validada.")
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
        print("")
        print("Usuario registrado correctamente. Retornando al menu principal")



def depositoBancario():
    print("")
    print("Ha seleccionado la opcion 2. (Realizar un deposito bancario)")
    print("")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("")
            print("Usuario encontrado")
            print("")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("")
                print("Usuario y clave correcta.")
                print("")
                print("Bienvenido! ",fila["nombre"]," ",fila["apellido"])
                print("")
                monto = float(input("Introduzca el monto a depositar en su cuenta: "))
                if monto > 0:
                    fila["posicion consolidada"] += monto
                    print("Monto introducido: ",monto)
                    print("Monto total: ",fila["posicion consolidada"])
                else:
                    print("")
                    print("Error al introducir un monto. Intentalo de nuevo...")
                    print("")     
    if existe_usuario == False:
        print("")
        print("El usuario introducido no se encuentra registrado en el sistema.")
    else:
        if existe_clave == False:
            print("La clave introducida es incorrecta...")
    

def retiroBancario():
    print("")
    print("Ha seleccionado la opcion 3. (Realizar un retiro bancario)")
    print("")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("")
            print("Usuario encontrado")
            print("")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("")
                print("Usuario y clave correcta.")
                print("")
                print("Bienvenido! ",fila["nombre"]," ",fila["apellido"])
                print("")
                monto = float(input("Introduzca el monto a retirar de su cuenta: "))
                if monto > fila["posicion consolidada"] or monto <= 0:
                    print("Introduzca un monto menor o igual al saldo disponible de su cuenta. Intente de nuevo")
                    print("")
                elif monto > 0 and monto <= fila["posicion consolidada"]:
                    fila["posicion consolidada"] -= monto
                    print("Monto introducido: ",monto)
                    print("Monto total: ",fila["posicion consolidada"])
    if existe_usuario == False:
        print("")
        print("El usuario introducido no se encuentra registrado en el sistema.")
    else:
        if existe_clave == False:
            print("La clave introducida es incorrecta...")



def consultarCuenta():
    print("")
    print("Ha seleccionado la opcion 4. (Consultar datos de una cuenta)")
    print("")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("")
            print("Usuario encontrado")
            print("")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("")
                print("Usuario y clave correcta. Mostrando los datos de la cuenta...")
                print("Nombre: ",fila["nombre"])
                print("Apellido: ",fila["apellido"])
                print("Cedula: ",fila["cedula"])
                print("Usuario: ",fila["usuario"])
                print("Posicion Consolidada: ",fila["posicion consolidada"])
                print("")
    if existe_usuario == False:
        print("")
        print("El usuario introducido no se encuentra registrado en el sistema.")
    else:
        if existe_clave == False:
            print("La clave introducida es incorrecta...")


def transferirACedula(persona,cedula,database):
    existe_cedula = False
    for fila in database:
        if fila["cedula"] == cedula:
            existe_cedula = True
            print("")
            print("Cedula encontrada.")
            print("")
            print("Nombre: ",fila["nombre"])
            print("Apellido: ",fila["apellido"])
            print("")
            monto = float(input("Introduzca el monto a transferir: "))
            if monto > 0 and monto <= persona["posicion consolidada"]:
                persona["posicion consolidada"] -= monto
                fila["posicion consolidada"] += monto
                print("")
                print("Monto transferido: ",monto)
                print("Saldo disponible en su cuenta: ",persona["posicion consolidada"])
            else:
                print("Introduzca un monto correcto y/o que no supere su saldo disponible en la cuenta.")
    if existe_cedula == False:
        print("")
        print("La persona a la cual desea realizarle una transferencia no se encuentra en el sistema.")


def realizarTransferencia():
    print("")
    print("Ha seleccionado la opcion 5. (Realizar una transferencia bancaria)")
    print("")
    existe_usuario = False
    existe_clave = False
    usuario = input("Introduzca un nombre de usuario existente: ")
    for fila in database:
        if fila["usuario"] == usuario:
            existe_usuario = True
            print("")
            print("Usuario encontrado")
            print("")
            clave = input("Introduzca la clave respectiva: ")
            if fila["clave"] == clave:
                existe_clave = True
                print("")
                print("Bienvenido! ",fila["nombre"]," ",fila["apellido"])
                print("")
                cedula = input("Introduzca la cedula de la persona a la que desea realizar la transferencia: ")
                while not cedula.isdigit():
                    print("")
                    print("La cedula no debe tener caracteres especiales ni letras.")
                    cedula = input("Cedula: ")
                print("")
                print("Cedula procesada...")
                transferirACedula(fila,cedula,database)
    if existe_usuario == False:
        print("")
        print("El usuario introducido no se encuentra registrado en el sistema.")
    else:
        if existe_clave == False:
            print("La clave introducida es incorrecta...")


def main():
    continuidad = True
    print("Hola, bienvenido/a al banco nacional, a continuacion le presentare las opciones que tenemos disponibles:")
    print("")
    while continuidad:
        try:
            print("")
            print("")
            print("Introduzca su opcion marcando cualquiera de los numeros indicados.")
            print("1.- Crear una Cuenta.")
            print("2.- Realizar un Deposito Bancario.")
            print("3.- Realizar un Retiro")
            print("4.- Consultar los datos de una cuenta.")
            print("5.- Realizar una transferencia a otro usuario.")
            print("6.- Salir del programa.")
            opcion = int(input("Opcion: "))
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
                print("")
                print("Hasta luego!")
                continuidad = False
            else:
                raise Exception("Dato introducido invalido. Intente de nuevo.")
        except Exception as error:
            print("")
            print("ERROR: ",error)
main()