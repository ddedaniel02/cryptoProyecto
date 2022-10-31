from Funcionalidades.funcionalidades_expedientes import FuncionalidadesExpediente
from Funcionalidades.funcionalidades_usuario import FuncionalidadesUsuario


class FuncionalidadesGenerales:
    def __init__(self, email):
        self.email = email

    def interfaz_inicio(self):
        print('¿Que desea hacer?')
        print('- Visualizar usuario (/funciones_user)')
        print('- Funcionalidades del Expediente (/funciones_exp)')
        print('- Cerrar Sesion (/log_out)')
        respuesta = input('-')
        self.elegir_funcion(respuesta)
    def elegir_funcion(self, input):
        if input == '/funciones_user':
            funciones_user = FuncionalidadesUsuario(self.email)
            funciones_user.interfaces_usuario()
        elif input == '/funciones_exp':
            funciones_expediente = FuncionalidadesExpediente(self.email)
            funciones_expediente.interfaz_expediente()
        elif input == '/log_out':
            from Funcionalidades.registro_inicio_de_sesion import inicio_aplicacion
            print('Cerrando sesión')
            inicio_aplicacion()








