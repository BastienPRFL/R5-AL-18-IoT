# Ressource R5-AL-18 : IoT 



## Pour le visualiser

Lien vers l'api : https://data.toulouse-metropole.fr/explore/dataset/points-dapport-volontaire-dechets-et-moyens-techniques/export/

* Télécharger tout le code source et décompresser l'archive *.zip
* $cd R5-AL-18-IoT-master
* $mkdocs serve

## Pre-requis éventuels

```
sudo apt-get update
```
et :

```
sudo apt install mkdocs mkdocs-material mkdocs-material-extensions
```

## Pour l'enseignant

* Récupérer la dernière debian (11 ici car bug affichage avec virtualbox...)
* installer dans une VM sous virtualbox avec user/resu comme compte
* configurer réseau en connexion par pont
* dans paramètres, choisir FR pour le clavier
* installer openssh-server
* Dans /etc/ssh/sshd_config :
   * décommentez pour avoir : PasswordAuthentication yes
   * décommentez et augmentez la valeur de : MaxAuthTries
* systemctl restart ssh
* une fois que tout est OK, dupliquez les VM selon nombre de groupes
* se brancher en filaire dans la salle


