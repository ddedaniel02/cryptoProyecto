"""Fichero contiene la clase que permite la creación de jsons para los doctores registrados en VetQuery"""

from crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonVet(CrearJson):
    _file_path = JSON_FILES_PATH + 'veterinarios.json'
    _key_field = 'email'
    """"""

    def __init__(self):
        pass