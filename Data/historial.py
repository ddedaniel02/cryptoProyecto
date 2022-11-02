"""Fichero contiene la clase de Historial médico (modificaciones realizadas) del expediente de la mascota"""

class Historial:
    """Historial clínico presente en el expediente de la mascota con información de las últimas modificaciones
    realizadas en el mismo"""

    def __init__(self, nombre_veterinario, fecha_observacion, observaciones):
        """Campos presentes en el historial"""

        self.nombre_veterinario = nombre_veterinario
        self.fecha_observacion = fecha_observacion
        self.observaciones = observaciones

    def crear_data(self, historial):
        """Crea el historial y lo incluye como una sección más del expediente"""

        data_list = historial
        data_list.append(self.__dict__)
