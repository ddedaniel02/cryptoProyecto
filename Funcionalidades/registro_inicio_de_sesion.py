"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""

from Data.doctors import Vet
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funcionalidades import Funcionalidades

from Funcionalidades.funciones_cripto import FuncionesCripto

from base64 import urlsafe_b64encode
from base64 import urlsafe_b64decode


def inicio_aplicacion():
    respuesta = input('Desea Iniciar Sesion (/inicio-sesion) o Registrarse (/registro): ')
    if respuesta == '/inicio-sesion':
        inicio_de_sesion()
    elif respuesta == '/registro':
        registro_usuario()


def inicio_de_sesion():
    correo_electronico = input('Introduce tu correo electrónico: ')
    codigo_acceso = input('Introduce tu contraseña: ')

    hashing = FuncionesCripto()
    codigo_hash = hashing.hashing(codigo_acceso)

    item = validar_usuario(correo_electronico, 'email')
    if item and validar_usuario(codigo_hash, "codigo_acceso", item):
        print('Acceso concedido')
        user_vet = Vet(item['nombre_completo'], item["fecha_nacimiento"], item["telefono"], item["email"],
                                 item["direccion"], item["especialidades"], item["direccion_clinica"], item["nombre_clinica"],
                                 item["telefono_clinica"], item["email_clinica"], item["codigo_acceso"])

        funcionalidades = Funcionalidades()
        funcionalidades.display_funcionalidades()
    else:
        print('No existe ese usuario')


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

    hashing = FuncionesCripto()
    codigo_hash = hashing.hashing(codigo_acceso)


    if not validar_usuario(email, 'email'):
        print('Se puede crear al usuario')
        user_vet = Vet(nombre_completo, telefono, email, fecha_nacimiento, direccion,
                       direccion_clinica, nombre_clinica, telefono_clinica, email_clinica, codigo_hash)
        user_vet.crear_usuario()
        funcionalidades =  Funcionalidades()
        funcionalidades.display_funcionalidades()
    else:
        print('El correo ya está asociado a un usuario')



def validar_usuario(valor, key, data_list = None):

    user_store = CrearJsonVet()
    if data_list == None:
        user_found = user_store.find_element(valor, key)
    else:
        user_found = user_store.find_element(valor, key, data_list)
    return user_found

