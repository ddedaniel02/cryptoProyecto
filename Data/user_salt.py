
from JSONstorage.crear_json_salt import CrearJsonSalt


class UserSalt:

    def __init__(self, user, salt, key):
        self.user = user
        self.salt = salt
        self.key = key

    def crear_base_datos(self):
        user_store = CrearJsonSalt()
        user_store.add_item(self)
