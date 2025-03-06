import matplotlib.pyplot as plt
from pymongo import MongoClient

## conexion a mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client["anime_db"]
collection = db["top_anime"]
animes = collection.find({}, {"_id": 0, "titulo": 1, "puntuacion": 1})
## fin conexion a mongodb

# Extraer títulos y puntuaciones
titulos = []
puntuaciones = []
##busca 
for anime in animes:
    titulos.append(anime["titulo"])
    puntuaciones.append(anime["puntuacion"])

##grafica
titulos = titulos[:20]
puntuaciones = puntuaciones[:20]
plt.figure(figsize=(15, 5))
plt.barh(titulos, puntuaciones, color='red')
plt.xlabel("Puntuación")
plt.ylabel("Titulo de Anime")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
##fin grafica


