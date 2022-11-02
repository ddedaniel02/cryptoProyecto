"""Fichero contiene la clase de creación de archivos .json"""
import json


class CrearJson:
    """Clase para operaciones realizadas sobre ficheros .json"""
    _file_path = ""

    def __init__(self):
        pass

    def load(self):
        """Carga los elementos del fichero .json"""
        try:
            with open(self._file_path, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError:
            print('Error en el archivo JSON')
            return -1
        return data_list

    def find_element(self, value, key) -> bool:
        """Busca un elemento específico del ficheor .json en base a un campo y el valor de dicho campo deseado"""
        data_list = self.load()
        for item in data_list:
            if item[key] == value:
                return True
        return False

    def save_data(self, data_list):
        """Almacena los datos del fichero .json"""
        try:
            with open(self._file_path, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError:
            print('Error: fichero no encontrado')
            return -1

    def add_item(self, item):
        """Añade el elmento al fichero .json"""
        data_list = self.load()
        data_list.append(item.__dict__)
        self.save_data(data_list)

    def mostrar_expedientes(self):
        """Permite mostrar los expedientes disponibles"""
        data_list = self.load()
        for item in data_list:
            print(item['id']+' Nombre Dueño: '+item['nombre_completo_propietario']+' Nombre Mascota: '+item['nombre_mascota'])