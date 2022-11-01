from Funcionalidades.funcionalidades_expedientes import FuncionalidadesExpediente
from Funcionalidades.funcionalidades_usuario import FuncionalidadesUsuario


class FuncionalidadesGenerales:
    def __init__(self, email):
        self.email = email

    def interfaz_inicio(self):
        print('¿Que desea hacer?\n')
        print('\t- Visualizar usuario (/funciones-user)')
        print('\t- Funcionalidades del Expediente (/funciones-exp)')
        print('\t- Cerrar Sesion (/log-out)')
        respuesta = input('-')
        self.elegir_funcion(respuesta)

    def elegir_funcion(self, input):
        """Presenta la interfaz solicitada al usuario o cierra la sesión. En caso de opción no válida, vuelve a
        mostrar la interfaz principal"""

        if input == '/funciones-user':
            funciones_user = FuncionalidadesUsuario(self.email)
            funciones_user.interfaces_usuario()
        elif input == '/funciones-exp':

            funciones_expediente = FuncionalidadesExpediente(self.email)
            funciones_expediente.interfaz_expediente()
        elif input == '/log-out':

            from Funcionalidades.registro_inicio_de_sesion import inicio_aplicacion
            print('Cerrando sesión')
            inicio_aplicacion()
        else:
            print('ERROR: Opción introducida no válida')
            self.interfaz_inicio()
