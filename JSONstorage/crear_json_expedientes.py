

from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonExpediente(CrearJson):
    _file_path = JSON_FILES_PATH + 'expedientes.json'
    """"""

    def __init__(self):
        pass

    def find_element(self, value, key):
        """Find element in the file"""
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return item
        return False