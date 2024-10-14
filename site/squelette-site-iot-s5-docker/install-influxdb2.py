import time
import json
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions

# user : Loufox
# password : Alaba5BUT3

# Configuration de l'accès à InfluxDB
url = "http://localhost:8086"  # Change si nécessaire
token = "8c1183f7cd621185018e9e6a60311095895ec55d443820b25ddfe963cf226934"
org = "Alaba5"
bucket = "Alaba"

client = InfluxDBClient(url=url, token=token)

# Utilisation correcte de WriteOptions
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

# Charger les données depuis le fichier JSON
def read_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Fonction pour écrire les données dans InfluxDB
def write_to_influxdb(data):
    for id, record in data.items():
        stock = record.get('stockage')
        if stock:
            point = (
                Point("stock_data")  # Nom de la mesure
                .tag("id", id)  # Ajout de l'id en tant que tag
                .field("stockage", stock)  # Ajout de la longitude en champ
                .time(time.time_ns(), WritePrecision.NS)  # Ajout du timestamp
            )
            write_api.write(bucket=bucket, org=org, record=point)

# Boucle pour écrire les données à une fréquence donnée
def write_periodically(file_path, interval):
    while True:
        data = read_json_data(file_path)
        write_to_influxdb(data)
        print(f"Données écrites à {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(interval)

# Définir l'intervalle en secondes (par exemple, écrire toutes les 10 secondes)
interval = 30
json_file_path = "nginx_html/geoloc_datas.json"  # Chemin du fichier JSON

write_periodically(json_file_path, interval)