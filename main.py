import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def leer_archivos(ruta):
    archivos = []

    for nombre in os.listdir(ruta):
        if nombre.endswith(".txt"):
            ruta_completa = os.path.join(ruta, nombre)

            with open(ruta_completa, "r", encoding="utf-8") as f:
                contenido = f.read()

            archivos.append((nombre, contenido))

    return archivos


# Función para convertir textos en vectores
def vectorizar(archivos, modelo):
    nombres = []
    textos = []

    for nombre, contenido in archivos:
        nombres.append(nombre)
        textos.append(contenido)

    vectores = modelo.encode(textos)

    return nombres, textos, vectores

# Función para buscar similitud
def buscar(consulta, modelo, nombres, textos, vectores):
    vector_consulta = modelo.encode([consulta])

    similitudes = cosine_similarity(vector_consulta, vectores)[0]

    resultados = list(zip(nombres, textos, similitudes))

    resultados.sort(key=lambda x: x[2], reverse=True)

    return resultados


# =========================
# PROGRAMA PRINCIPAL
# =========================

# Carpeta donde están los archivos
ruta = "data"

# Cargar modelo de IA
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Leer archivos
archivos = leer_archivos(ruta)

# Verificar si hay archivos
if not archivos:
    print("No se encontraron archivos .txt en la carpeta data")
    exit()

# Mostrar archivos encontrados
print("Archivos encontrados:")
for archivo in archivos:
    print(f"- {archivo[0]}")

# Vectorizar archivos
nombres, textos, vectores = vectorizar(archivos, modelo)

# Pedir búsqueda
consulta = input("\n ¿Qué archivo deseas buscar?: ")

# Buscar resultados
resultados = buscar(consulta, modelo, nombres, textos, vectores)

# Mostrar resultados
print("\n Top 2 resultados encontrados:")
for i, (nombre, contenido, score) in enumerate(resultados[:2], start=1):
    print(f"\n{i}. {nombre}")
    print(f"   Similitud: {score:.4f}")
    print(f"   Contenido: {contenido[:100]}...")