"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""

from Data.doctors import Vet
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funcionalidades import FuncionalidadesGenerales

from Funcionalidades.funciones_cripto import FuncionesCripto



def inicio_aplicacion():
    respuesta = input('Desea Iniciar Sesion (/inicio-sesion) o Registrarse (/registro): ')
    if respuesta == '/inicio-sesion':
        inicio_de_sesion()
    elif respuesta == '/registro':
        registro_usuario()


def inicio_de_sesion():
    correo_electronico = input('Introduce tu correo electrónico: ')
    codigo_acceso = input('Introduce tu contraseña: ')

    funcion_cripto = FuncionesCripto()
    funcion_cripto.verificar_contraseña(codigo_acceso, correo_electronico)

    print('Acceso concedido')

    funcionalidades = FuncionalidadesGenerales()
    funcionalidades.interfaz_inicio()




def registro_usuario():

    nombre_completo = input('Nombre: ')
    telefono = input('Telefono: ')
    email = input('Correo Electronico: ')
    fecha_nacimiento = input('Fecha de nacimiento: ')
    direccion = input('Direccion: ')
    direccion_clinica = input('Direccion de la clinica: ')
    nombre_clinica = input('Nombre de la clinica: ')
    telefono_clinica = input('Telefono de la clinica: ')
    email_clinica = input('Correo Electronico de la clinica: ')
    codigo_acceso = input("Codigo de acceso: ")


    if not validar_usuario(email, 'email'):
        cripto_funciones = FuncionesCripto()
        cripto_funciones.generar_salt(email)

        key_value = cripto_funciones.hashing(codigo_acceso, email)
        nombre_cifrado = cripto_funciones.cifrado(nombre_completo, key_value)
        telefono_cifrado = cripto_funciones.cifrado(telefono, key_value)
        direccion_cifrada = cripto_funciones.cifrado(direccion, key_value)

        user_vet = Vet(nombre_cifrado, telefono_cifrado, email, fecha_nacimiento, direccion_cifrada,
                       direccion_clinica, nombre_clinica, telefono_clinica, email_clinica, key_value)
        user_vet.crear_usuario()
        print('Usuario creado')

        funcionalidades = FuncionalidadesGenerales()
        funcionalidades.interfaz_inicio()
    else:
        print('El correo ya está asociado a un usuario')



def validar_usuario(valor, key, data_list = None):

    user_store = CrearJsonVet()
    if data_list == None:
        user_found = user_store.find_element(valor, key)
    else:
        user_found = user_store.find_element(valor, key, data_list)
    return user_found

