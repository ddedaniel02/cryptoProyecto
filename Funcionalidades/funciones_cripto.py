
import os
import base64
from JSONstorage.crear_json_salt import CrearJsonSalt
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from Data.user_salt import UserSalt
from JSONstorage.crear_json_doctor import CrearJsonVet
from cryptography.fernet import Fernet


class FuncionesCripto:

    def __init__(self):
        pass

    def hashing(self, codigo_acceso: str, email: str):
        cod_acc_bits = bytes(codigo_acceso, 'ISO-8859-1')
        salt = self.get_salt(email)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(cod_acc_bits)
        key = key.decode('ISO-8859-1')
        return key

    def verificar_codigo_acceso(self, codigo_acceso, email):
        cod_acc_bits = bytes(codigo_acceso, 'ISO-8859-1')
        salt = self.get_salt(email)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = self.get_key(email)
        kdf.verify(cod_acc_bits, key)

    @staticmethod
    def get_key(email):

        usuario_json = CrearJsonVet()
        item = usuario_json.find_element(email, 'email')
        key = item['codigo_acceso']
        key = key.encode('ISO-8859-1')
        return key

    @staticmethod
    def cifrado(valor_cifrar: str, key):

        valor_bytes = bytes(valor_cifrar, 'ISO-8859-1')

        key_base64 = base64.urlsafe_b64encode(key.encode('ISO-8859-1'))
        fernet = Fernet(key_base64)

        valor_encriptado = fernet.encrypt(valor_bytes)
        valor_cifrado = valor_encriptado.decode('ISO-8859-1')
        return valor_cifrado

    @staticmethod
    def generar_salt(usuario):
        salt = os.urandom(16)
        salt_str = salt.decode('ISO-8859-1')
        user_salt = UserSalt(usuario, salt_str)
        user_salt.incluir_salt()

    @staticmethod
    def get_salt(email):
        user_salt = CrearJsonSalt()
        salt = user_salt.find_element(email, 'user')
        salt_encripted = salt.encode('ISO-8859-1')
        return salt_encripted

    @staticmethod
    def guardar_cod(email, cod_hash):

        """Guarda la clave/contraseña del usuario en el la DB del salt"""
        user_salt = CrearJsonSalt()
        user_salt.add_key(email, cod_hash)
