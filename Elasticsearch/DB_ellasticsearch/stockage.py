from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json


# Connexion au client Elasticsearch
es_client = Elasticsearch("http://localhost:9200")



# Charger les fichiers JSON
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Charger vos fichiers de données
uniqlomb = load_data("Elasticsearch/data_json/uniqlomb.json")
uniqlomo = load_data("Elasticsearch/data_json/uniqlomo.json")
uniqloms = load_data("Elasticsearch/data_json/uniqloms.json")
uniqlowb = load_data("Elasticsearch/data_json/uniqlowb.json")
uniqlowo = load_data("Elasticsearch/data_json/uniqlowo.json")
uniqlows = load_data("Elasticsearch/data_json/uniqlows.json")

# Préparer les données pour bulk
def prepare_bulk_actions(index_name, data):
    for doc in data:
        yield {
            "_index": index_name,
            "_source": doc
        }


# Fusionner toutes les données
all_data = uniqlomb + uniqlomo + uniqloms + uniqlowb + uniqlowo + uniqlows

# Indexer avec bulk
index_name = "clothes"
bulk(es_client, prepare_bulk_actions(index_name, all_data))

print(f"Indexation de {len(all_data)} documents terminée avec succès dans l'index '{index_name}'.")

# Vidage de la base de données, en utilisant ignore_status pour ignorer les erreurs 400 et 404
#es_client.options(ignore_status=[400, 404]).indices.delete(index="clothes")



