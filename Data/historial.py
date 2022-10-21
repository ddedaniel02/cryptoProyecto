

class Historial:
    def __init__(self, nombre_veterinario, fecha_observacion, observaciones):
        self.nombre_veterinario = nombre_veterinario
        self.fecha_observacion = fecha_observacion
        self.observaciones = observaciones




    def crear_data(self, historial):
        data_list = historial
        data_list.append(self.__dict__)