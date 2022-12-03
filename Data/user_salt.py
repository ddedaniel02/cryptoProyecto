"""Fichero contiene clase para el guardado de salt, email y contraseña resumida de cada usuario registrado en la
aplicación"""

from JSONstorage.crear_json_salt import CrearJsonSalt


class UserSalt:
    """Clase para el guardado del Salt del usuario  en una Base de Datos (DB) externa, junto con la contraseña
    resumida y el correo electrónico del usuario"""

    def __init__(self, user, salt_password, salt_cifrado, key):
        """Campos a guardar en la DB externa: email del usuario, su salt y contraseña ya resumida"""

        self.user = user
        self.salt_password = salt_password
        self.salt_cifrado = salt_cifrado
        self.password_hash = key

    def crear_base_datos(self):
        """Añade a la DB el correo del usuario junto al salt y contraseña resumida correspondientes"""

        user_store = CrearJsonSalt()
        user_store.add_item(self)
