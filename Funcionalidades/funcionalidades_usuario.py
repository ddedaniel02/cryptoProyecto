
from JSONstorage.crear_json_doctor import CrearJsonVet
from Funcionalidades.funciones_cripto import FuncionesCripto

class FuncionalidadesUsuario:
    def __init__(self, email):
        self.email = email

    def interfaces_usuario(self):
        user_json = CrearJsonVet()
        cripto_funciones = FuncionesCripto()
        item = user_json.find_element(self.email, 'email')

        nombre_descifrado = cripto_funciones.descifrado(item['nombre_completo'], self.email)
        telefono_descifrado = cripto_funciones.descifrado(item['telefono'], self.email)
        direccion_descifrada = cripto_funciones.descifrado(item['direccion'], self.email)

        print('\tNombre y Apellidos: '+nombre_descifrado)
        print('\tTelefono: ' + telefono_descifrado)
        print('\tCorreo Electrónico: '+self.email)
        print('\tDireccion: '+direccion_descifrada)

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




