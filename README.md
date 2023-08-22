# Modelo de Sistema Bancario

El programa consiste en emular todas las opciones que se pueden hacer a través de una plataforma web de un banco.


>Desarrolado por:
>* Annuar A | [@Annuar2203](https://github.com/Annuar2203)
>* Jean Odrizola | [@erjeank25](https://github.com/erjeank25)
>* Maria Chang | [@AlexandraYuyi](https://github.com/AlexandraYuyi)
>* Moises Londoño | [@MoisesLondo](https://github.com/MoisesLondo)
>* Luis Amias | [@AstroLui](https://github.com/AstroLui)



## Explicación de los modulos

En primera instancia se tiene un submétodo el cual será llamado cada vez que se quiera crear un nuevo usuario, para esto 
se hace uso de un diccionario el cual tendrá valores vacíos que se llenarán mediante el transcurso del programa.

El submétodo **validarClave()** será encargado de que, al momento de escribir una contraseña para un usuario determinado, ésta 
cumpla con una serie de prerrequisitos como lo son: mínimo 6 caracteres, uso de mayúsculas, uso de minúsculas, uso de dígitos, 
uso de caracteres especiales.
            
El método **crearCuenta()** engloba los anteriores submétodos, aquí se le solicitará al usuario: nombre, apellido, 
cedula, usuario y contraseña.

Todos los datos solicitados pasarán por un proceso de validación (en este momento se hará uso del submétodo **validarClave()** para 
verificar si la contraseña cumple los requisitos para ser aceptada).

Una vez aceptados los datos, se procederá a pasar los valores a las claves del diccionario anteriormente mencionado, además 
de establecer un monto de 50 Bs como saldo inicial. Por último, se valida si la persona que se registró existe anteriormente en 
el banco mediante su apodo y/o cédula, en caso de estar registrada no se tomará en cuenta el registro y retornara al menú principal, 
en caso contrario se añadirán los datos guardados en ese diccionario en un vector global denominado "database", el cual se encarga 
de llevar los usuarios de cada persona para los distintos procesos de los que se quiera hacer uso.

Pasando al método **depositoBancario()**, se procederá a pedirle a un usuario que introduzca su apodo y su clave (previamente ya existentes), 
el cual será validado, para verificar si retorna al menú principal (al estar erróneo) o si continúa con el depósito bancario. En caso 
de seguir con el depósito, se pedirá introducir el monto a depositar en la cuenta (deberá ser mayor a 0), en este momento se sumará 
ese monto al saldo actual de esa persona (actualizando el valor de la clave "posición consolidada").

El siguiente método es **retiroBancario()**, el cual pedirá a un usuario ingresar su apodo y contraseña, se validará que 
el mismo exista y que no sea erróneo, posteriormente se le pedirá al usuario que indique el monto a retirar, el cual 
deberá ser menor o igual a su saldo disponible, una vez retirado el dinero, se actualizará el saldo disponible en su 
cuenta (actualizando el valor de la clave "posición consolidada").

Pasando al siguiente modulo denominado **consultarCuenta()**, se pedirá al usuario que introduzca su apodo y su contraseña, 
validando que este exista y que los datos no sean incorrectos. Una vez validado el usuario, se procederá a enseñar: 
su nombre, apellido, cédula y su saldo disponible. Posteriormente se procede a volver al menú principal.

Seguidamente está el método **realizarTransferencia()**, el cual pedirá al usuario introducir su apodo y contraseña, las cuales 
se validaran al momento de introducirlas, una vez verificadas se pedirá al usuario introducir la cédula de la persona a la 
que desea realizar la transferencia, haciendo un llamado al submetodo **transferirACedula()**, el cual enviará como 
argumento: la persona que se busca en la variable global database(), la cédula ingresada de la persona a transferir, y el 
vector global "database" para manejar las cédulas validas dentro del banco.

El submódulo **transferirACedula()** validará si el parámetro "cedula" se encuentra dentro del sistema del banco, de ser así se 
mostrará el nombre y apellido de la persona a transferir y se solicitará un monto a transferir, el cual deberá ser mayor a 0 y 
menor al saldo disponible, posteriormente verificado el proceso, se restará el dinero transferido al usuario y se sumará el dinero 
transferido al destinatario, a su vez se mostrará el monto transferido y el saldo actual del usuario.

Por último, está el método principal main(), el cual será el menú principal de todos los demás métodos, aquí se pedirá al usuario
que realice una acción dentro del banco, y cuando no quiera realizar otra acción, se procederá a salir del programa.

## Tips
Como elementos a mejorar en el programa en un futuro, se puede hacer uso de la refactorización de código para hacerlo más 
entendible y más compacto (menos líneas de código), además de que se puede implementar la Programación Orientada a Objetos (POO), 
para una mas óptima resolucion del ejercicio.
