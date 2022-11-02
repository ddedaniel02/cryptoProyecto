"""Fichero contiene la clase que permite la creación de jsons para los doctores registrados en VetQuery"""

from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH


class CrearJsonSalt(CrearJson):
    """Clase que contiene las funcionalidades disponibles para los .json relacionados a los salts"""

    _file_path = JSON_FILES_PATH + 'base_datos_salt.json'

    def find_element(self, value, key):
        """Encuentra el elemento en el fichero .json"""
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return item
        return 'Error a la hora de la administración de la cuenta'
