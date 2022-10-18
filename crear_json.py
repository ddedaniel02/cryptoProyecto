"""Fichero contiene la clase de creación de archivos .json"""
import json

class CrearJson:
    _file_path = ""
    _key_field = ""

    """Clase de creación de archivos .json"""
    def __init__(self):
        pass

    def load(self):
        try:
            with open(self._file_path, "r", encoding="utf-8", newline="") as file:
                print('Estoy aqui')
                data_list = json.load(file)
        except FileNotFoundError:
            print('Hola')
            data_list = []
        except json.JSONDecodeError:
            print('Error en el archivo JSON')
            return -1
        return data_list

    def find_element(self, value, key=None):
        """Find element in the file"""
        data_list = self.load()
        if key is None:
            key = self._key_field
        for item in data_list:
            if item[key] == value:
                return True
        return False

    def save_data(self, data_list):
        """save the data from the files"""
        try:
            with open(self._file_path, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError:
            print(self._file_path)
            print('Error: fichero no encontrado')
            return -1

    def add_item(self, item):
        """add item into the file"""
        data_list = self.load()
        data_list.append(item.__dict__)
        self.save_data(data_list)
