import time
import json
import os
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions

# user : Loufox
# password : Alaba5BUT3

# Configuration de l'accès à InfluxDB
url = "http://localhost:8086"  # Change si nécessaire
token = "8c1183f7cd621185018e9e6a60311095895ec55d443820b25ddfe963cf226934"
org = "Alaba5"
bucket = "Alaba"

# Config mqtt
broker = "localhost"
port = 1884
topic = "recupverres"
dico_data = {}

def get_data(mqttc, obj, msg):
    print("message reçu")
    try:
        dico_data = json.loads(msg.payload)
        print("Nouvelles infos reçues : \n")
        print(dico_data)
        write_to_influxdb(dico_data)
        time.sleep(interval)

    except json.JSONDecodeError as e:
        print("paquet avec données vides reçu")

def send(val):
    pass

mqttc = mqtt.Client()
mqttc.on_message = get_data
mqttc.connect(broker, port, 60)
mqttc.loop_start()
mqttc.subscribe(topic,0)

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

mqttc.loop_start()

# Boucle pour écrire les données à une fréquence donnée
def write_periodically(file_path, interval):
    print("En attente des messages MQTT...")
    while True:
        try:
            time.sleep(interval)
            
            print("En attente de nouvelles données...")
        except KeyboardInterrupt:
            print("\nArrêt du programme.")
            mqttc.disconnect()
            break  # Arrête la boucle proprement en cas d'interruption


# Définir l'intervalle en secondes (par exemple, écrire toutes les 10 secondes)
interval = 30
json_file_path = "nginx_html/geoloc_datas.json"  # Chemin du fichier JSON

write_periodically(json_file_path, interval)