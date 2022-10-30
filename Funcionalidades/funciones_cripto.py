
import base64
from JSONstorage.crear_json_salt import CrearJsonSalt
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from Data.user_salt import UserSalt
from JSONstorage.crear_json_doctor import CrearJsonVet
from cryptography.fernet import Fernet



class FuncionesCripto:


    def hashing(self, contraseña:str, email:str):
        contraseña_bits = bytes(contraseña, 'ISO-8859-1')
        salt = self.get_salt(email)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(contraseña_bits)
        key = key.decode('ISO-8859-1')
        return key

    def verificar_contraseña(self, contraseña, email):
        contraseña_bits = bytes(contraseña, 'ISO-8859-1')
        salt = self.get_salt(email)
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = self.get_key(email)
        kdf.verify(contraseña_bits, key)

    def get_key(self, email):
        usuario_json = CrearJsonVet()
        item = usuario_json.find_element(email, 'email')
        key = item['codigo_acceso']
        key = key.encode('ISO-8859-1')
        return key


    def cifrado(self, valor_cifrar:str, key):
        valor_bytes = bytes(valor_cifrar, 'ISO-8859-1')

        key_base64 = base64.urlsafe_b64encode(key.encode('ISO-8859-1'))
        fernet = Fernet(key_base64)

        valor_encriptado = fernet.encrypt(valor_bytes)
        valor_cifrado = valor_encriptado.decode('ISO-8859-1')
        return valor_cifrado


    def generar_salt(self, usuario):
        salt = os.urandom(16)
        salt_str = salt.decode('ISO-8859-1')
        user_salt = UserSalt(usuario, salt_str)
        user_salt.añadir_salt()

    def get_salt(self, email):
        user_salt = CrearJsonSalt()
        salt = user_salt.find_element(email, 'user')
        salt_encripted = salt.encode('ISO-8859-1')
        return salt_encripted
