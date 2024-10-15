import os
import random
import json
import time
import paho.mqtt.client as mqtt


broker = "localhost"
port = 1884
topic = "recupverres"

# Fonction pour générer un nombre aléatoire supérieur à la base
def random_greater_than_base(base):
    if base >= 100:
        return "Le chiffre de base doit être inférieur à 100."
    return random.randint(base + 1, 100)

# Fonction pour lire le fichier JSON et le retourner sous forme de dictionnaire
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    

# Fonction pour écrire les données mises à jour dans un fichier JSON
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Obtenir le chemin absolu du fichier JSON
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'nginx_html/geoloc_datas.json')

# Boucle pour mettre à jour le fichier toutes les 30 secondes
"""while True:
    # Charger les données du fichier JSON existant
    geoloc_data = read_json_file(file_path)

    # Générer un nombre aléatoire pour chaque entrée dans le fichier JSON
    base = 0
    for key in geoloc_data.keys():
        number = random_greater_than_base(base)
        geoloc_data[key]['stockage'] = number

    # Sauvegarder les nouvelles données dans le fichier JSON
    write_json_file(file_path, geoloc_data)
    # Sauvegarder les nouvelles données dans le fichier JSON
    write_json_file(file_path, geoloc_data)

    print(f"Mise à jour du fichier avec les valeurs de stockage effectuée à {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Attendre 30 secondes avant la prochaine mise à jour
    time.sleep(30)
"""

def envoi_donnees_recupverres(client, recupverres):
    dico_donnees = {}
    for rec in recupverres:
        #datas = rec.get('fields', {})
        lon = recupverres[rec].get('lon')
        lat = recupverres[rec].get('lat')
        stock = random_greater_than_base(1)
        dico_donnees[rec] = {
            "lon": lon,
            "lat": lat,
            "stockage": stock
        }

    envoi_data = json.dumps(dico_donnees)
    client.publish(topic,envoi_data)
    print("Mise à jour des données")
    print(envoi_data)



recupverres = read_json_file("nginx_html/geoloc_datas.json")
print("debut")

def sur_connexion(client, user_datas, flags, retour):
    print("Connecté à MQTT, code de retour : " + str(retour))

client = mqtt.Client()
client.on_connect = sur_connexion
client.connect(broker, port, 60)
client.loop_start()

while True:
        envoi_donnees_recupverres(client, recupverres)
        time.sleep(30)
