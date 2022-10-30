"""Fichero contiene la clase de los veterinarios registrados en la aplicación VetQuery"""

from JSONstorage.crear_json_doctor import CrearJsonVet


class Vet:

    """Clase Veterianrio"""

    def __init__(self, nombre_completo: str, telefono: str, email: str, fecha_nacimiento: int, direccion: str,
                 direccion_clinica: str, nombre_clinica: str, telefono_clinica: str, email_clinica: str, codigo_acceso:str,
                 *especialidades: str):

        """Atributos de la clase veterinario"""

        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.especialidades = especialidades
        self.direccion_clinica = direccion_clinica
        self.nombre_clinica = nombre_clinica
        self.telefono_clinica = telefono_clinica
        self.email_clinica = email_clinica
        self.codigo_acceso = codigo_acceso

    def crear_usuario(self):
        user_store = CrearJsonVet()
        user_store.add_item(self)
    def __del__(self):
        print('Cerrando sesión')









