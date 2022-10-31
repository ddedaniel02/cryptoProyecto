
from JSONstorage.crear_json_salt import CrearJsonSalt


class UserSalt:

    def __init__(self, user, salt):
        self.user = user
        self.salt = salt

    def incluir_salt(self):
        user_store = CrearJsonSalt()
        user_store.add_item(self)
