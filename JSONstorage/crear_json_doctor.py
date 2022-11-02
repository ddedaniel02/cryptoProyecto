"""Fichero contiene la clase que permite la creación de jsons para los doctores registrados en VetQuery"""

from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonVet(CrearJson):
    """Funciones vinculadas a los ficheros .json de los veterinarios"""
    _file_path = JSON_FILES_PATH + 'veterinarios.json'

    def __init__(self):
        pass

    def find_element(self, value, key):
        """Encuentra el element oen el fichero .json"""
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return item
        return False