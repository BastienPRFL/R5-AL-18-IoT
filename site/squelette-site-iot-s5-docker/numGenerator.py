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
    
# Fonction pour envoyer les données sur MQTT
def envoi_donnees_recupverres(client, recupverres):
    dico_donnees = {}
    for rec in recupverres:
        lon = recupverres[rec].get('lon')
        lat = recupverres[rec].get('lat')
        stock = random_greater_than_base(1)
        dico_donnees[rec] = {
            "lon": lon,
            "lat": lat,
            "stockage": stock
        }

    envoi_data = json.dumps(dico_donnees)
    client.publish(topic, envoi_data)
    print("Mise à jour des données")
    print(envoi_data)

# Lire les données du fichier JSON
recupverres = read_json_file("nginx_html/geoloc_datas.json")
print("debut")

# Fonction appelée lors de la connexion à MQTT
def sur_connexion(client, user_datas, flags, retour):
    print("Connecté à MQTT, code de retour : " + str(retour))

client = mqtt.Client()
client.on_connect = sur_connexion
client.connect(broker, port, 60)
client.loop_start()

# Boucle principale pour envoyer les données périodiquement
while True:
    try:
        envoi_donnees_recupverres(client, recupverres)
        time.sleep(30)
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
        client.disconnect()
        break  # Interrompt la boucle uniquement si une interruption clavier est détectée
