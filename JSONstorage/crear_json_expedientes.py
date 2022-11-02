"""Fichero que contiene la clase con las funcionalidades disponibles para los ficheros .json de expedientes"""

from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonExpediente(CrearJson):
    """Clase con las funcionalides disponibles para los .json relacionados a los expedientes"""

    _file_path = JSON_FILES_PATH + 'expedientes.json'

    def __init__(self):
        pass

    def find_element(self, value, key):
        """Encuentra el elemento en el fichero .json"""
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return item
        return False