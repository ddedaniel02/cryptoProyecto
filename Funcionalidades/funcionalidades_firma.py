from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature


import pickle
from cryptography.hazmat.primitives.asymmetric import utils

from JSONstorage.crear_json_expedientes import CrearJsonExpediente
from Data.firma_data import FirmaData
from JSONstorage.crear_json_firma import CrearJsonFirmas
from funciones_regex.func_regex import *


class FuncionalidadesFirma:


    def load_key(self):
        correcto = False
        intentos = 3
        while not correcto and intentos != 0:
            try:
                password_admin = validar_regex_password(REGEX_CODIGO_ACCESO,
                                              '\tCódigo de acceso de administrador: ')
                password_bytes = password_admin.encode('utf-8')
                with open("res/private_key.pem", "rb") as key_file:
                    private_key= serialization.load_pem_private_key(
                        data=key_file.read(),
                        password=password_bytes,
                        backend=default_backend()
                    )
                correcto = True
                return private_key
            except ValueError:
                intentos -= 1
                print('Contraseña incorrecta, le quedan ',intentos,' intento(s) más')
            except Exception:
                intentos -= 1
                print('Contraseña incorrecta, le quedan ',intentos,' intento(s) más')
        if intentos == 0:
            private_key = 'ERROR'
            return private_key

    def crear_firma(self, id, private_key):
        sign = self.firma(private_key, id)
        firma_data = FirmaData(id, sign)
        firma_data.guardar_data()

    @staticmethod
    def firma(private_key, id_expediente):
        json_expediente = CrearJsonExpediente()
        data_list = json_expediente.find_element(id_expediente, 'id')
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        data_list_bytes = pickle.dumps(data_list)
        hasher.update(data_list_bytes)
        digest = hasher.finalize()
        sig = private_key.sign(
            digest,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            utils.Prehashed(chosen_hash)
        )
        sig_no_bytes = sig.decode('ISO-8859-1')
        return sig_no_bytes

    @staticmethod
    def verificar_firma(data_list):
        with open("res/public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                data=key_file.read(),
                backend=default_backend()
            )
        data_list_bytes = pickle.dumps(data_list)
        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        hasher.update(data_list_bytes)
        digest = hasher.finalize()
        json_expedientes = CrearJsonExpediente()
        json_firma = CrearJsonFirmas()
        sig = json_firma.find_element(data_list['id'], 'id')
        sig_encode = sig.encode('ISO-8859-1')
        try:
            public_key.verify(
                sig_encode,
                digest,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                utils.Prehashed(chosen_hash)
            )
            return True
        except InvalidSignature:
            print('No se pudo verificar los datos.')
            return False






