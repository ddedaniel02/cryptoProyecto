"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""
import re
from Data.doctors import Vet
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
        except invalidKey:
            print('ERROR: Las contraseñas no coinciden\n')

    print('Acceso concedido\n')

    funcionalidades = FuncionalidadesGenerales()
    funcionalidades.interfaz_inicio()


def registro_usuario():

    nombre_completo = input('\tNombre y Apellido(s): ')
    #if not re.match("^\b([A-Za-z][-,a-z. ']+[ ]*)+$", nombre_completo):
    telefono = input('\tTeléfono: ')
    email = input('\tCorreo Electrónico: ')
    fecha_nacimiento = float(input('\tFecha de nacimiento: '))
    direccion = input('\tDirección: ')
    direccion_clinica = input('\tDirección de la clínica: ')
    nombre_clinica = input('\tNombre de la clínica: ')
    telefono_clinica = input('\tTeléfono de la clínica: ')
    email_clinica = input('\tCorreo Electrónico de la clínica: ')
    codigo_acceso = input('\tCódigo de acceso: ')

    if not validar_usuario(email, 'email'):
        cripto_funciones = FuncionesCripto()
        cripto_funciones.generar_salt(email)

        key_value = cripto_funciones.hashing(codigo_acceso, email)
        nombre_cifrado = cripto_funciones.cifrado(nombre_completo, key_value)
        telefono_cifrado = cripto_funciones.cifrado(telefono, key_value)
        direccion_cifrada = cripto_funciones.cifrado(direccion, key_value)
        cripto_funciones.guardar_cod(email, key_value)

        user_vet = Vet(nombre_cifrado, telefono_cifrado, email, fecha_nacimiento, direccion_cifrada,
                       direccion_clinica, nombre_clinica, telefono_clinica, email_clinica)
        user_vet.crear_usuario()
        print('Usuario creado\n')

        funcionalidades = FuncionalidadesGenerales()
        funcionalidades.interfaz_inicio()
    else:
        print('El correo ya está asociado a un usuario\n')


def validar_usuario(correo, campo_correo):

    user_store = CrearJsonVet()
    user_found = user_store.find_element(correo, campo_correo)
    return user_found

