
from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonFirmas(CrearJson):
    """Funciones vinculadas a los ficheros .json de los veterinarios"""
    _file_path = JSON_FILES_PATH + 'firma_digital.json'

    def __init__(self):
        pass

    def find_element(self, value, key):
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return item['firma_digital']
        return False