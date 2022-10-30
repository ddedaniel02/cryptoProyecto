from Data.expediente_paciente import Expediente


class FuncionalidadesExpediente:

    def interfaz_expediente(self):
        print('¿Qué deseas hacer?\n')
        print('- Crear Expediente de nuevo paciente (/crear-expediente)\n')
        print('- Eliminar Expediente (/eliminar-expediente)\n')
        print('- Modificar Expediente (/modificar-expediente)\n')
        print('- Añadir Notas al Historial del Paciente (/añadir-notas)\n')
        print('- Retroceder (/back)')
        comando = input('- ')
        self.elegir_funcionalidades(comando)

    def elegir_funcionalidades(self, comando):

        if comando == '/crear-expediente':
            self.introducir_datos_expediente()
        elif comando == '/eliminar-expediente':
            self.eliminarExpediente()
        elif comando == '/modificar-expediente':
            self.modificarExpediente()
        elif comando == '/añadir-notas':
            self.añadirNotas()
        elif comando == '/back':
            from Funcionalidades.funcionalidades import FuncionalidadesGenerales
            interfaz_inicio = FuncionalidadesGenerales()
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


        expediente_paciente = Expediente(nombre_mascota, sexo_mascota, nacimiento_mascota, especie, raza, alergias,
                                         nombre_dueños, telefono, direccion)

        print('Rellena su historial: ')
        nombre_veterinario = input('Nombre del veterinario que realizó la consulta: ')
        fecha_observacion = input('Fecha de cuando se realizó la consulta: ')
        observaciones = input('Observaciones realizadas durante la consulta: ')

        expediente_paciente.crear_historial(nombre_veterinario, fecha_observacion, observaciones)
        expediente_paciente.crear_expediente()
        print('Expediente creado')
        self.interfaz_expediente()






    """(está por ahora mal)"""
    def rellenar_historial(self):
        expediente = Expediente()
        adding = True
        while(adding):
            continue_inserting = input('¿Quiéres añadir historial previo? (y/n)')

            if continue_inserting == 'y':
                nombre_veterinario = input('Nombre Veterinario: ')
                observaciones = input('Observaciones: ')
                conclusiones = input('Conclusiones: ')
            elif continue_inserting == 'n':
                adding = False



    def eliminarExpediente(self):
        pass

    def modificarExpediente(self):
        pass

    def añadirNotas(self):
        print('Rellena el nuevo historial: ')
        nombre_veterinario = input('Nombre del veterinario que realizó la consulta: ')
        fecha_observacion = input('Fecha de cuando se realizó la consulta: ')
        observaciones = input('Observaciones realizadas durante la consulta: ')

        expediente_paciente.crear_historial(nombre_veterinario, fecha_observacion, observaciones)