from Funcionalidades.funcionalidades_expedientes import FuncionalidadesExpediente
from Funcionalidades.funcionalidades_usuario import FuncionalidadesUsuario


class FuncionalidadesGenerales:
    def __init__(self, email):
        self.email = email

    def interfaz_inicio(self):
        print('¿Que desea hacer?\n')
        print('\t- Visualizar usuario (/funciones_user)')
        print('\t- Funcionalidades del Expediente (/funciones_exp)')
        print('\t- Cerrar Sesion (/log_out)')
        respuesta = input('-')
        self.elegir_funcion(respuesta)

    def elegir_funcion(self, input):
        respuesta_valida = False
        while not respuesta_valida:
            if input == '/funciones_user':
                respuesta_valida = True
                funciones_user = FuncionalidadesUsuario(self.email)
                funciones_user.interfaces_usuario()
            elif input == '/funciones_exp':
                respuesta_valida = True
                funciones_expediente = FuncionalidadesExpediente(self.email)
                funciones_expediente.interfaz_expediente()
            elif input == '/log_out':
                respuesta_valida = True
                from Funcionalidades.registro_inicio_de_sesion import inicio_aplicacion
                print('Cerrando sesión')
                inicio_aplicacion()
            else:
                print('ERROR: Opción introducida no válida')







