# MQTT et simuler des capteurs

## Objectifs

Ici nous allons voir le minimum pour simuler des objets connectés qui vont publier leurs données en MQTT. Pour cela, vous allez :

* Installer un broker MQTT (mosquitto ici)
* Configurer le broker afin d'activer les websockets
* Développer un script python de simulation des objets

Dans tous les cas, lisez bien la documentation !

## Installation du broker MQTT

``` bash
sudo apt-get install mosquitto mosquitto-clients
```

### Test de validation

Utilisez les commandes [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) et [mosquitto_sub](https://mosquitto.org/man/mosquitto_sub-1.html) afin de valider la bonne configuration du logiciel.

Par exemple, dans votre terminal :

``` bash
mosquitto_sub -v -t "#" -h IP_du_broker_MQTT
```

Dans un autre terminal :

``` bash
mosquitto_pub -t "test" -m "hello" -h IP_du_broker_MQTT

```

!!! info "Astuce"
    Vous pouvez aussi utiliser le client graphique [MQTT-explorer](https://mqtt-explorer.com/) comme vu en S3.


!!! info "Astuce"

    Le projet mosquitto met à votre disposition un service de test : [test.mosquitto.org](https://test.mosquitto.org/)

### Websockets

Prenez connaissance de la documentation de Mosquitto :

[Documentation du démon](https://mosquitto.org/man/mosquitto-8.html)

[Documentation de la configuration](https://mosquitto.org/man/mosquitto-conf-5.html)

À l'aide ces documentations afin d'obtenir les fonctionnalités suivantes :

* Activation d'un listener MQTT sur tcp sans TLS sur le port 1883
* Activation d'un listener MQTT sur websocket sans TLS sur le port 9001

Ajoutez les lignes suivantes dans le fichier de configuration /etc/mosquitto/conf.d/mosquitto.conf :

``` bash
listener 1883
listener 9001
protocol websockets
allow_anonymous true
```

Redémarrage de mosquitto afin d'appliquer la configuration :

``` bash
systemctl restart mosquitto
```

## Script Python de simulation

A l'aide de la [librairie paho-mqtt](https://pypi.org/project/paho-mqtt/), développez un script python de simulation de l'objet connecté de votre application.

``` bash
apt-get install python3-paho-mqtt
```

Modifiez le script d'exemple afin de créer le squelette de base des trois scripts python que vous allez devoir créer :

``` python
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```
