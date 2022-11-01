from JSONstorage.crear_json_expedientes import CrearJsonExpediente
from Data.historial import Historial
import random


class Expediente:
    def __init__(self, nombre_mascota, sexo_mascota, nacimiento_mascota, especie, raza, alergias,
                 nombre_completo_dueno, telefono, direccion):
        self.id = self.assign_id()
        self.nombre_mascota = nombre_mascota
        self.sexo_mascota = sexo_mascota
        self.nacimiento_mascota = nacimiento_mascota
        self.especie = especie
        self. raza = raza
        self.nombre_completo_dueno = nombre_completo_dueno
        self.telefono = telefono
        self.direccion = direccion
        self.alergias = alergias
        self.historial = []

    def crear_expediente(self):
        pacient_store = CrearJsonExpediente()
        pacient_store.add_item(self)

    def crear_historial(self, nombre_veterinario, fecha_observacion, observaciones):
        historial = Historial(nombre_veterinario, fecha_observacion, observaciones)
        historial.crear_data(self.historial)

    def assign_id(self):
        id = random.randrange(0,999)
        expediente_storage = CrearJsonExpediente()
        assigned = False
        while not assigned:
            if not expediente_storage.find_element(id, 'id'):
                assigned = True
                return str(id)
            id = random.randrange(0, 999)
