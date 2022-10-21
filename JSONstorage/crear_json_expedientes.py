

from JSONstorage.crear_json import CrearJson
from config.config import JSON_FILES_PATH

class CrearJsonExpediente(CrearJson):
    _file_path = JSON_FILES_PATH + 'expedientes.json'
    """"""

    def __init__(self):
        pass