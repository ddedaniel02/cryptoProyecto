"""Fichero contiene la clase de los veterinarios registrados en la aplicación VetQuery"""

from JSONstorage.crear_json_doctor import CrearJsonVet


class Vet:

    """Clase Veterianrio"""

    def __init__(self, nombre_completo: str, telefono: str, email: str, fecha_nacimiento: str, direccion: str):

        """Atributos de la clase veterinario"""

        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.codigo_postal = codigo_postal

    def crear_usuario(self):
        user_store = CrearJsonVet()
        user_store.add_item(self)

    def __del__(self):
        print('Cerrando sesión')









