
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funciones_cripto import FuncionesCripto
from cryptography.fernet import InvalidToken

class FuncionalidadesUsuario:
    def __init__(self, email):
        self.email = email

    def interfaces_usuario(self):
        user_json = CrearJsonVet()
        cripto_funciones = FuncionesCripto()
        item = user_json.find_element(self.email, 'email')
        error = False

        for key in item:
            valor = item[key]
            if key == 'nombre_completo' or key == 'telefono' or key == 'codigo_postal':
                try:
                    valor = cripto_funciones.descifrado(item[key], self.email)
                except InvalidToken:
                    print('Permisos denegados, acceso no permitido')
                    error = True
                    break
            print(key+':'+valor)
        if error:
            from Funcionalidades.funcionalidades import FuncionalidadesGenerales
            funciones_generales = FuncionalidadesGenerales(self.email)
            funciones_generales.interfaz_inicio()

        stop = False
        while not stop:
            respuesta = input('Salir /leave: ')
            if respuesta == '/leave':
                stop = True
            else:
                print('Comando desconocido')
        from Funcionalidades.funcionalidades import FuncionalidadesGenerales
        funciones_generales = FuncionalidadesGenerales(self.email)
        funciones_generales.interfaz_inicio()




