import os
import random
import json
import time
import time

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
while True:
    # Charger les données du fichier JSON existant
    geoloc_data = read_json_file(file_path)
# Boucle pour mettre à jour le fichier toutes les 30 secondes
while True:
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