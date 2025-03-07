import requests
from pymongo import MongoClient

# Conexion a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["anime_db"]
collection = db["top_anime"] 
url = "https://api.jikan.moe/v4/top/anime"
data = requests.get(url)
# fin Conexion a MongoDB

if data.status_code == 200:
    anime_data = data.json()["data"]
    for anime in anime_data:
        anime_doc = {
            "titulo": anime["title"],
            "puntuacion": anime["score"],
            "episodios": anime["episodes"],
        }
        collection.insert_one(anime_doc)

    print("Conexion exitosa...")
else:
    print("No se pudo conectar...")

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



