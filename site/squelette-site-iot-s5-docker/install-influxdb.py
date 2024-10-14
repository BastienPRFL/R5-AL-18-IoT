import os
from influxdb_client import InfluxDBClient

# Configuration de la connexion à InfluxDB
url = "http://localhost:8086"  # Remplace si nécessaire
token = os.environ.get("INFLUXDB_TOKEN")  # Ton token d'accès
org = "Alaba5"  # Nom de ton organisation


#Token Graphana (à regénérer) : 8c1183f7cd621185018e9e6a60311095895ec55d443820b25ddfe963cf226934

# Créer une connexion à InfluxDB
client = InfluxDBClient(url=url, token=token)

# Test de connexion
health = client.health()
print(health.status)

# Fermer la connexion (lorsque tu as terminé)
client.close()
