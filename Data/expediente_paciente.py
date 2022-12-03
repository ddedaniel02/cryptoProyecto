"""Fichero contiene la clase de los expedientes de los pacientes vinculados a cada veterinario"""

from JSONstorage.crear_json_expedientes import CrearJsonExpediente
from Funcionalidades.funcionalidades_firma import FuncionalidadesFirma
from Data.historial import Historial
import random


class Expediente:
    """Clase Expediente de paciente. Cada expediente se vinicula con un único veterinario"""

    def __init__(self, usuario_creador, nombre_mascota, sexo_mascota, nacimiento_mascota, especie, raza,
                 nombre_completo_propietario, telefono, codigo_postal):
        """Campos de datos del expediente"""

        self.usuario_creador = usuario_creador
        self.id = self.assign_id()
        self.nombre_mascota = nombre_mascota
        self.sexo_mascota = sexo_mascota
        self.nacimiento_mascota = nacimiento_mascota
        self.especie = especie
        self.raza = raza
        self.nombre_completo_propietario = nombre_completo_propietario
        self.telefono = telefono
        self.codigo_postal = codigo_postal
        self.historial = []

    def crear_expediente(self):
        """Añade el expediente a la BD"""

        pacient_store = CrearJsonExpediente()
        pacient_store.add_item(self)

    def crear_historial(self, nombre_veterinario, fecha_observacion, observaciones):
        """Añade las observaciones realizadas al historial, junto con el nombre del veterinario y la fecha"""

        historial = Historial(nombre_veterinario, fecha_observacion, observaciones)
        historial.crear_data(self.historial)

    def assign_id(self) -> str:
        """Asigna un ID todavía no tomado al expediente de la mascota o lo recupera si ya lo tiene"""

        id = random.randrange(0, 999)
        expediente_storage = CrearJsonExpediente()
        assigned = False
        while not assigned:
            if not expediente_storage.find_element(id, 'id'):
                assigned = True
                return str(id)
            id = random.randrange(0, 999)
    def cargar_firma(self):
        funciones_firma = FuncionalidadesFirma()
        return funciones_firma.load_key()
    def crear_firma(self, private_key):
        funciones_firma = FuncionalidadesFirma()
        funciones_firma.crear_firma(self.id, private_key)
