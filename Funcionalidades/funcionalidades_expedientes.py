from Data.expediente_paciente import Expediente
from Funcionalidades.funciones_cripto import FuncionesCripto
from JSONstorage.crear_json_expedientes import CrearJsonExpediente


class FuncionalidadesExpediente:

    def __init__(self, email):
        self.email = email

    def interfaz_expediente(self):
        print('¿Qué deseas hacer?\n')
        print('- Crear Expediente de nuevo paciente (/crear-expediente)\n')
        print('- Eliminar Expediente (/eliminar-expediente)\n')
        print('- Visualizar Expediente (/ver-expediente\n')
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




    def introducir_datos_expediente(self):

        print('- Creación de expediente')
        nombre_mascota = input('Nombre de la mascota: ')
        sexo_mascota = input('Sexo de la mascota: ')
        nacimiento_mascota = input('Fecha de nacimiento de la mascota: ')
        especie = input('Especie: ')
        raza = input('Raza: ')
        alergias= input('Alergias o Enfermedades Hereditarias (separadas por guiones): ')

        nombre_dueños = input('Nombre y Apellidos del dueño/a: ')
        telefono = input('Telefono: ')
        direccion = input('Direccion: ')

        cripto_funciones = FuncionesCripto()
        telefono_cifrado = cripto_funciones.cifrado(telefono, self.email)
        direccion_cifrado = cripto_funciones.cifrado(direccion, self.email)


        expediente_paciente = Expediente(nombre_mascota, sexo_mascota, nacimiento_mascota, especie, raza, alergias,
                                         nombre_dueños, telefono_cifrado, direccion_cifrado)

        print('Rellena su historial: ')
        nombre_veterinario = input('Nombre del veterinario que realizó la consulta: ')
        fecha_observacion = input('Fecha de cuando se realizó la consulta: ')
        observaciones = input('Observaciones realizadas durante la consulta: ')

        nombre_veterinario_cifrado = cripto_funciones.cifrado(nombre_veterinario,self.email)

        expediente_paciente.crear_historial(nombre_veterinario_cifrado, fecha_observacion, observaciones)
        expediente_paciente.crear_expediente()
        print('Expediente creado')
        self.interfaz_expediente()

    def verExpediente(self):
        paciente_json = CrearJsonExpediente()
        print('Por favor, escriba el ID del expediente que desee visualizar')
        paciente_json.mostrar_expedientes()
        stop = False
        while not stop:
            respuesta = input('- ')
            item = paciente_json.find_element(respuesta, 'id')
            if item:
                stop = True
            else:
                print('Ese id no existe, por favor, inserte otro')
        self.display_expediente(item)

    def display_expediente(self, expediente):
        cripto_funciones = FuncionesCripto()
        for key in expediente:
            if key == 'historial':
                for item in expediente[key]:
                    for fields in item:
                        valor_print = item[fields]
                        if fields == "nombre_veterinario":
                            valor_print = cripto_funciones.descifrado(valor_print, self.email)
                        print(fields+':'+valor_print)
            else:
                valor_print = expediente[key]
                if (key == 'telefono') or (key == "direccion"):
                    valor_print = cripto_funciones.descifrado(valor_print, self.email)
                print(key+':'+valor_print)

        stop = False
        while not stop:
            respuesta = input('Salir (/leave): ')
            if respuesta == '/leave':
                stop = True
            else:
                print('Comando desconocido')
        self.interfaz_expediente()



