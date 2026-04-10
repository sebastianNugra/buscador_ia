import os


def leer_archivos(ruta):
    archivos = []

    for nombre in os.listdir(ruta):
        if nombre.endswith(".txt"):
            with open(os.path.join(ruta, nombre), "r", encoding="utf-8") as f:
                contenido = f.read()
                archivos.append((nombre, contenido))

    return archivos


ruta = "data"  # carpeta donde se pondran los archivos
archivos = leer_archivos(ruta)

for a in archivos:
    print(a[0]) # imprime nombres