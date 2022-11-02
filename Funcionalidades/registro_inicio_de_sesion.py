"""Fichero de registro e inicio de sesión de doctores en la aplicación VetQuery"""
import re
from funciones_regex.func_regex import *
from Data.doctors import Vet
from Data.user_salt import UserSalt
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funcionalidades import FuncionalidadesGenerales
from Funcionalidades.funciones_cripto import FuncionesCripto
from cryptography.exceptions import InvalidKey


def inicio_aplicacion():
    """Permite ejecutar el conjunto de la aplicación"""

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
            print('¡Hasta la próxima!')
        else:
            print('[ERROR]: La opción introducida no es válida\n')


def inicio_sesion():
    """Permite al usuario acceder al inicio de sesión"""

    sesion_iniciada = False
    back = False
    while not sesion_iniciada and not back:
        print('Si desea volver atrás, escriba /back en cualquiera de los campos, por favor')
        correo_electronico = input('Introduce tu correo electrónico: ')
        codigo_acceso = input('Introduce tu contraseña: ')

        funcion_cripto = FuncionesCripto()
        try:
            if correo_electronico == '/back' or codigo_acceso == '/back':
                back = True
            else:
                funcion_cripto.verificar_codigo_acceso(codigo_acceso, correo_electronico)
                sesion_iniciada = True
        except TypeError:
            print('Correo incorrecto')
        except InvalidKey:
            print('ERROR: Las contraseñas no coinciden\n')

    if back:
        print('Volviendo atrás')
        inicio_aplicacion()
    else:
        print('Acceso concedido\n')

        # Traslada al usuario al menu de la aplicación (distinto del de inicio-registro)
        funcionalidades = FuncionalidadesGenerales(correo_electronico, codigo_acceso)
        funcionalidades.interfaz_inicio()


def registro_usuario():
    """Permite al usuario acceder al registro de usuario"""

    # Comprueba que las entradas de cada campo sigue el formato permitido
    nombre_completo = validar_regex(REGEX_NOMBRE_COMPLETO, '\tNombre y Apellido(s) [Aviso: No incluir tilde]: ')
    telefono = validar_regex(REGEX_TELEFONO, '\tTeléfono [formato: +prfx (espacio) num.telf]: ')
    email = validar_regex(REGEX_EMAIL, '\tCorreo Electrónico [Únicos caracteres especiales aceptados son @ _ y .]: ')
    fecha_nacimiento = validar_regex(REGEX_FECHA_NACIMIENTO, '\tFecha de nacimiento [YYYY-MM-DD]: ')
    codigo_postal = validar_regex(REGEX_CODIGO_POSTAL, '\tCodigo Postal: ')
    codigo_acceso = validar_regex(REGEX_CODIGO_ACCESO, '\tCódigo de acceso [Aviso: mín. 8 caracteres, 1 mayús, 1 minús '
                                                       ', un caracter especial y al menos un número]: ')

    # Comprueba si el usuario ya esta registrado
    if not validar_usuario(email, 'email'):
        cripto_funciones = FuncionesCripto()

        salt_contraseña = cripto_funciones.generar_salt()
        salt_cifrado = cripto_funciones.generar_salt()
        key_value = cripto_funciones.hashing(codigo_acceso, salt_contraseña)

        user_salt = UserSalt(email, salt_contraseña, salt_cifrado, key_value)
        user_salt.crear_base_datos()

        nombre_cifrado = cripto_funciones.cifrado(nombre_completo, email, codigo_acceso)
        telefono_cifrado = cripto_funciones.cifrado(telefono, email, codigo_acceso)
        codigo_postal_cifrado = cripto_funciones.cifrado(codigo_postal, email, codigo_acceso)

        user_vet = Vet(nombre_cifrado, telefono_cifrado, email, fecha_nacimiento, codigo_postal_cifrado)
        user_vet.crear_usuario()
        print('Usuario creado\n')

        # Traslada al usuario al menu de la aplicación (distinto del de inicio-registro)
        funcionalidades = FuncionalidadesGenerales(email, codigo_acceso)
        funcionalidades.interfaz_inicio()
    else:
        print('El correo ya está asociado a un usuario\n')


def validar_usuario(correo, campo_correo):
    """Comprueba si el usuario ya existe"""

    user_store = CrearJsonVet()
    user_found = user_store.find_element(correo, campo_correo)
    return user_found

