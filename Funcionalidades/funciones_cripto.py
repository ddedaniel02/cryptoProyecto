"""Fichero contiene clase que permite realizar las operaciones de criptografía necesarias en la aplicación"""

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

    # Función para realizar el hash
    @staticmethod
    def hashing(codigo_acceso: str, salt_contraseña):
        cod_acc_bits = bytes(codigo_acceso, 'ISO-8859-1')
        salt_contraseña = salt_contraseña.encode('ISO-8859-1')
        kdf = Scrypt(
            salt=salt_contraseña,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(cod_acc_bits)
        key = key.decode('ISO-8859-1')
        return key

    # Función para verificar la contraseña de usuario
    def verificar_codigo_acceso(self, codigo_acceso, email):
        cod_acc_bits = bytes(codigo_acceso, 'ISO-8859-1')
        salt_contraseña = self.get_salt(email, 'contraseña')
        kdf = Scrypt(
            salt=salt_contraseña,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = self.get_key(email)
        kdf.verify(cod_acc_bits, key)

    # Función que recupera la clave del usuario de la DB
    @staticmethod
    def get_key(email):
        usuario_salt = CrearJsonSalt()
        item = usuario_salt.find_element(email, 'user')
        key = item['key']
        key = key.encode('ISO-8859-1')
        return key

    # Función para el cifrado
    def cifrado(self, valor_cifrar, email, password):
        valor_bytes = bytes(valor_cifrar, 'ISO-8859-1')
        password_bytes = bytes(password, 'ISO-8859-1')
        salt_cifrado = self.get_salt(email, 'cifrado')
        kdf = Scrypt(
            salt=salt_cifrado,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(password_bytes)
        key_base64 = base64.urlsafe_b64encode(key)
        fernet = Fernet(key_base64)

        valor_encriptado = fernet.encrypt(valor_bytes)
        valor_cifrado = valor_encriptado.decode('ISO-8859-1')
        return valor_cifrado

    # Función para el descifrado
    def descifrado(self, valor_descifrar, email, password):
        valor_bytes = bytes(valor_descifrar, 'ISO-8859-1')
        password_bytes = bytes(password, 'ISO-8859-1')
        salt_cifrado = self.get_salt(email, 'cifrado')
        kdf = Scrypt(
            salt=salt_cifrado,
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
        )
        key = kdf.derive(password_bytes)
        key_base64 = base64.urlsafe_b64encode(key)
        fernet = Fernet(key_base64)

        valor_retorno = fernet.decrypt(valor_bytes)
        valor = valor_retorno.decode('ISO-8859-1')
        return valor

    # Función para generar el salt
    @staticmethod
    def generar_salt():
        salt = os.urandom(16)
        salt_str = salt.decode('ISO-8859-1')
        return salt_str

    # Función para rescatar de la DB el salt del usuario indicado
    @staticmethod
    def get_salt(email, tipo):
        user_salt = CrearJsonSalt()
        item = user_salt.find_element(email, 'user')
        if tipo == 'cifrado':
            salt_cifrado = item['salt_cifrado']
            salt_encripted = salt_cifrado.encode('ISO-8859-1')
            return salt_encripted
        salt_contraseña = item['salt_contraseña']
        salt_encripted = salt_contraseña.encode('ISO-8859-1')
        return salt_encripted

