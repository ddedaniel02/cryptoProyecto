"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""
import re
from Data.doctors import Vet
from Data.user_salt import UserSalt
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funcionalidades import FuncionalidadesGenerales

from Funcionalidades.funciones_cripto import FuncionesCripto
from cryptography.exceptions import InvalidKey


def inicio_aplicacion():

    respuesta_valida = False
    while not respuesta_valida:
        respuesta = input('¿Desea Iniciar Sesión (/inicio-sesion), Registrarse (/registro) o Salir (/salir)? : ')
        if respuesta == '/inicio-sesion':
            respuesta_valida = True
            inicio_sesion()
        elif respuesta == '/registro':
            respuesta_valida = True
            registro_usuario()
        elif respuesta == '/salir':
            respuesta_valida = True
            print('Hasta la próxima')
        else:
            print('ERROR: La opción introducida no es válida\n')


def inicio_sesion():

    sesion_iniciada = False
    while not sesion_iniciada:
        correo_electronico = input('Introduce tu correo electrónico: ')
        codigo_acceso = input('Introduce tu contraseña: ')

        funcion_cripto = FuncionesCripto()
        try:
            funcion_cripto.verificar_codigo_acceso(codigo_acceso, correo_electronico)
            sesion_iniciada = True

        except TypeError:
            print('Correo incorrecto')
        except InvalidKey:
            print('ERROR: Las contraseñas no coinciden\n')

    print('Acceso concedido\n')

    funcionalidades = FuncionalidadesGenerales(correo_electronico)
    funcionalidades.interfaz_inicio()


def registro_usuario():

    nombre_completo = input('\tNombre y Apellido(s): ')
    #if not re.match("^\b([A-Za-z][-,a-z. ']+[ ]*)+$", nombre_completo):
    telefono = input('\tTeléfono: ')
    email = input('\tCorreo Electrónico: ')
    fecha_nacimiento = float(input('\tFecha de nacimiento: '))
    direccion = input('\tDirección: ')
    codigo_acceso = input('\tCódigo de acceso: ')

    if not validar_usuario(email, 'email'):
        cripto_funciones = FuncionesCripto()

        salt = cripto_funciones.generar_salt()
        key_value = cripto_funciones.hashing(codigo_acceso, salt)

        user_salt = UserSalt(email, salt, key_value)
        user_salt.crear_base_datos()

        nombre_cifrado = cripto_funciones.cifrado(nombre_completo, email)
        telefono_cifrado = cripto_funciones.cifrado(telefono, email)
        direccion_cifrada = cripto_funciones.cifrado(direccion, email)

        user_vet = Vet(nombre_cifrado, telefono_cifrado, email, fecha_nacimiento, direccion_cifrada)
        user_vet.crear_usuario()
        print('Usuario creado\n')

        funcionalidades = FuncionalidadesGenerales(email)
        funcionalidades.interfaz_inicio()
    else:
        print('El correo ya está asociado a un usuario\n')


def validar_usuario(correo, campo_correo):

    user_store = CrearJsonVet()
    user_found = user_store.find_element(correo, campo_correo)
    return user_found

