
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

    @staticmethod
    def hashing(codigo_acceso: str, salt):
        cod_acc_bits = bytes(codigo_acceso, 'ISO-8859-1')
        salt = salt.encode('ISO-8859-1')
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

        usuario_salt = CrearJsonSalt()
        item = usuario_salt.find_element(email, 'user')
        key = item['key']
        key = key.encode('ISO-8859-1')
        return key

    def cifrado(self,valor_cifrar, email):

        valor_bytes = bytes(valor_cifrar, 'ISO-8859-1')
        key = self.get_key(email)

        key_base64 = base64.urlsafe_b64encode(key)
        fernet = Fernet(key_base64)

        valor_encriptado = fernet.encrypt(valor_bytes)
        valor_cifrado = valor_encriptado.decode('ISO-8859-1')
        return valor_cifrado

    def descifrado(self, valor_descifrar, email):
        valor_bytes = bytes(valor_descifrar, 'ISO-8859-1')
        key = self.get_key(email)

        key_base64 = base64.urlsafe_b64encode(key)
        fernet = Fernet(key_base64)

        valor_retorno = fernet.decrypt(valor_bytes)
        valor = valor_retorno.decode('ISO-8859-1')
        return valor

    @staticmethod
    def generar_salt():
        salt = os.urandom(16)
        salt_str = salt.decode('ISO-8859-1')
        return salt_str

    @staticmethod
    def get_salt(email):
        user_salt = CrearJsonSalt()
        item = user_salt.find_element(email, 'user')
        salt = item['salt']
        salt_encripted = salt.encode('ISO-8859-1')
        return salt_encripted

