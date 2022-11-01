"""Fichero de funciones para comprobar los emparejamientos de datos de entrada con expr. regulares"""

import re

# Expresiones regulares para el registro de nuevos usuarios
REGEX_NOMBRE_COMPLETO = "([A-Z][-,a-z. ']+[ ]*){2,}"
REGEX_TELEFONO = "\+([1-9]){1,3}\s[1-9][0-9]{8}"
REGEX_EMAIL = "[A-Za-z0-9._]+@[a-z0-9]+\.([a-z0-9]+\.)?[a-z]{2,3}"
REGEX_FECHA_NACIMIENTO = "[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"
REGEX_CODIGO_POSTAL = "^\d{5}$"
REGEX_CODIGO_ACCESO = "(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}"


def validar_regex(regex: str, info_requerida: str) -> str:
    """Retorna el dato introducido por el usuario tras confirmar que sigue el formato válido"""
    while True:
        dato_entrada = input(info_requerida)
        if re.fullmatch(regex, dato_entrada):
            return dato_entrada
        else:
            print("ERROR: Dato de entrada no válido\n")
