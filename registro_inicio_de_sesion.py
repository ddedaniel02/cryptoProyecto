"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""

from doctors import Vet
from crear_json_doctor import CrearJsonVet


def inicio_aplicacion():
    respuesta = input('Desea Iniciar Sesion (/inicio-sesion) o Registrarse (/registro): ')
    registro_inicio(respuesta)




def registro_inicio(respuesta :str):
    if respuesta == '/registro':
        nombre_completo = input('Nombre: ')
        telefono = input('Telefono: ')
        email = input('Correo Electronico: ')
        fecha_nacimiento = input('Fecha de nacimiento: ')
        direccion = input('Direccion: ')
        direccion_clinica = input('Direccion de la clinica: ')
        nombre_clinica = input('Nombre de la clinica: ')
        telefono_clinica = input('Telefono de la clinica: ')
        email_clinica = input('Correo Electronico de la clinica: ')

        if not validar_usuario(email):
            print('Se puede crear al usuario')
            user_vet = Vet(nombre_completo, telefono, email, fecha_nacimiento, direccion,
                           direccion_clinica, nombre_clinica, telefono_clinica, email_clinica)
            user_vet.crear_usuario()
        else:
            print('El correo ya está asociado a un usuario')
            return -1

    elif respuesta == '/inicio-sesion':
        id_usuario = input('Introduce tu ID de usuario: ')
        contraseña = input('Introduce tu contraseña: ')

def validar_usuario(email):

    user_store = CrearJsonVet()
    user_found = user_store.find_element(email)
    if not user_found:
        print('No se encontró al usuario')
        return False
    print('Se encontró al usuario')
    return True

