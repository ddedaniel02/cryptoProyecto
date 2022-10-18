"""Fichero contiene sección de ayuda"""

#Función invocada para consultar los comandos disponibles en VetQuery
def ayuda():

    titulo_ayuda = "\t\tLista de comandos de VetQuery\n"
    listado_comandos = ("/registro", "/inicio-sesion" )
    listado_uso_comandos = ("Activa ventana de registro de veterinarios.", "Activa ventana de inicio de sesión",)

    print()
    for instr in range(len(listado_comandos)):
        print("\n--> " + listado_comandos[instr] +"<---> " + listado_uso_comandos[instr])
