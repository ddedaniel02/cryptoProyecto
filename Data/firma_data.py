
from JSONstorage.crear_json_firma import CrearJsonFirmas

class FirmaData:

    def __init__(self, id_expediente, firma_digital):
        self.id = id_expediente
        self.firma_digital = firma_digital

    def guardar_data(self):
        json_firmas = CrearJsonFirmas()
        json_firmas.add_item(self)
