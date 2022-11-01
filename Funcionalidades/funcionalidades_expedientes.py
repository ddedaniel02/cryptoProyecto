from Data.expediente_paciente import Expediente
from Funcionalidades.funciones_cripto import FuncionesCripto
from JSONstorage.crear_json_expedientes import CrearJsonExpediente

from funciones_regex.func_regex import *
from cryptography.fernet import InvalidToken

class FuncionalidadesExpediente:

    def __init__(self, email):
        self.email = email

    def interfaz_expediente(self):
        print('¿Qué deseas hacer?\n')
        print('- Crear Expediente de nuevo paciente (/crear-expediente)\n')
        print('- Eliminar Expediente (/eliminar-expediente)\n')
        print('- Visualizar Expediente (/ver-expediente)\n')
        print('- Retroceder (/back)')
        comando = input('- ')
        self.elegir_funcionalidades(comando)

    def elegir_funcionalidades(self, comando):

        if comando == '/crear-expediente':
            self.introducir_datos_expediente()
        elif comando == '/eliminar-expediente':
            self.eliminarExpediente()
        elif comando == '/ver-expediente':
            self.verExpediente()
        elif comando == '/back':
            from Funcionalidades.funcionalidades import FuncionalidadesGenerales
            interfaz_inicio = FuncionalidadesGenerales(self.email)
            interfaz_inicio.interfaz_inicio()
        else:
            print('ERROR: Opción introducida no válida')
            self.interfaz_expediente()

    def introducir_datos_expediente(self):

        print('- Creación de expediente')
        nombre_mascota = validar_regex(REGEX_NOMBRE_ESPECIE_RAZA_MASCOTA, '\tNombre de la mascota: ')
        sexo_mascota = validar_regex(REGEX_SEXO_MASCOTA, '\tSexo de la mascota: ')
        nacimiento_mascota = validar_regex(REGEX_FECHA_NACIMIENTO,
                                           '\tFecha de nacimiento de la mascota [YYYY-MM-DD]: ')
        especie = validar_regex(REGEX_NOMBRE_ESPECIE_RAZA_MASCOTA, '\tEspecie: ')
        raza = validar_regex(REGEX_NOMBRE_ESPECIE_RAZA_MASCOTA, '\tRaza: ')
        nombre_dueños = validar_regex(REGEX_NOMBRE_COMPLETO,
                                      '\tNombre y Apellido(s) del dueño [Aviso: No incluir tilde]: ')
        telefono = validar_regex(REGEX_TELEFONO, '\tTeléfono [formato: +prfx (espacio) num.telf]: ')
        codigo_postal = validar_regex(REGEX_CODIGO_POSTAL, '\tCodigo Postal: ')

        cripto_funciones = FuncionesCripto()
        telefono_cifrado = cripto_funciones.cifrado(telefono, self.email)
        codigo_postal_cifrado = cripto_funciones.cifrado(codigo_postal, self.email)
        usuario_creador_cifrado = cripto_funciones.cifrado(self.email, self.email)


        expediente_paciente = Expediente(usuario_creador_cifrado, nombre_mascota, sexo_mascota, nacimiento_mascota,
                                         especie, raza, nombre_dueños, telefono_cifrado, codigo_postal_cifrado)

        print('Rellena su historial: ')
        nombre_veterinario = validar_regex(REGEX_NOMBRE_COMPLETO,
                                           '\tNombre y apellido(s) del veterinario que realizó la consulta: ')
        fecha_observacion = validar_regex(REGEX_FECHA_NACIMIENTO,
                                          '\tFecha de cuando se realizó la consulta[YYYY-MM-DD]: ')
        observaciones = validar_regex(REGEX_OBSERVACIONES, '\tObservaciones realizadas durante la consulta: ')

        nombre_veterinario_cifrado = cripto_funciones.cifrado(nombre_veterinario,self.email)

        expediente_paciente.crear_historial(nombre_veterinario_cifrado, fecha_observacion, observaciones)
        expediente_paciente.crear_expediente()
        print('Expediente creado')
        self.interfaz_expediente()

    def verExpediente(self):
        paciente_json = CrearJsonExpediente()
        print('Por favor, escriba el ID del expediente que desee visualizar')
        paciente_json.mostrar_expedientes()
        print('Salir (/back)')
        stop = False

        while not stop:
            respuesta = input('- ')
            if respuesta == '/back':
                stop = True
            else:
                item = paciente_json.find_element(respuesta, 'id')
                if item:
                    stop = True
                else:
                    print('Ese id no existe, por favor, inserte otro')
        if respuesta == '/back':
            self.interfaz_expediente()
        else:
            self.display_expediente(item)

    def display_expediente(self, expediente):
        cripto_funciones = FuncionesCripto()
        error = False
        for key in expediente:
            if key != 'historial':
                valor_print = expediente[key]
                if (key == 'telefono') or (key == "codigo_postal") or (key == 'usuario_creador'):
                    try:
                        valor_print = cripto_funciones.descifrado(valor_print, self.email)
                    except InvalidToken:
                        print('Permiso denegado, acceso no permitido')
                        error = True
                        break

                print(key + ':' + valor_print)
            else:
                for item in expediente[key]:
                    for fields in item:
                        valor_print = item[fields]
                        if fields == "nombre_veterinario":
                            valor_print = cripto_funciones.descifrado(valor_print, self.email)
                        print(fields+':'+valor_print)
        if error:
            self.interfaz_expediente()
        stop = False
        while not stop:
            respuesta = input('Salir (/leave): ')
            if respuesta == '/leave':
                stop = True
            else:
                print('Comando desconocido')
        self.interfaz_expediente()



