#   docker run --name my-mongo -d -p 27017:27017 mongo
#   mongosh "mongodb://localhost:27017"
#   pip install pymongo==4.9.1

from pymongo import MongoClient
import json

# Charger les fichiers JSON
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Charger vos fichiers de données
uniqlomb = load_data("MongoDB/data_json/uniqlomb.json")
uniqlomo = load_data("MongoDB/data_json/uniqlomo.json")
uniqloms = load_data("MongoDB/data_json/uniqloms.json")
uniqlowb = load_data("MongoDB/data_json/uniqlowb.json")
uniqlowo = load_data("MongoDB/data_json/uniqlowo.json")
uniqlows = load_data("MongoDB/data_json/uniqlows.json")

all_data = uniqlomb + uniqlomo + uniqloms + uniqlowb + uniqlowo + uniqlows

# Se connecter à la base de données
client = MongoClient()
db_uniqlo = client.uniqlo
db_uniqlo_clothes = db_uniqlo["Clothes"]

#Supprimer la database !!!
db_uniqlo_clothes.drop()
print("suppression ok")

#Insérer les documents
db_uniqlo_clothes.insert_many(all_data)
print("les données ont été importés")


