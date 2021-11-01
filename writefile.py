# Ejemplo python
# - Sobrescribe un fichero con un nuevo texto
# - Si el fichero no existe, lo crea
#

import os
import sys

palabra = str(sys.argv[1])
# print(palabra)


# f = open("testigo.txt", "w")
# fichero = os.environ['HOME']+"/testigo.txt"
# fichero = os.environ['HOME']+"/ansible/testigo.txt"
fichero = "/home/grillo/ansible/testigo.txt"
f = open(fichero, "w")
f.write("Hola, acabo de cambiar el contenido a contenido6 21:39 "+ palabra)
f.close()

