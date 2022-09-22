# LE PROJET Coffee Shop Full Stack

Le projet Coffee Shop est un café activé numériquement dans lequel les étudiants peuvent commander à boire, se sociabiliser, et étudier. Les utilisateurs de cette plate-forme peuvent en fonction de leur droits d'accès(rôlres) afficher des graphiques représentant les ratios d'ingrédients dans chaque boisson, visualiser les noms et les graphiques des boissons,  voir les informations sur les recettes(avec le rôle baristas de la boutique),  créer de nouvelles boissons et de modifier les boissons existantes et enfin supprimer une boisson(avec le rôle manager).


Tout le code backend suit [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

## Pour Commencer

### Pré-requis et Développement local
Les développeurs qui utilisent ce projet doivent déjà avoir Python3, pip et node installés sur leurs machines locales.

### Configuration du backend

Depuis le dossier backend, exécutez `pip install requirements.txt`. Tous les paquets requis sont inclus dans le fichier d'exigences. 

Pour lancer l'application, exécutez les commandes suivantes : 
```
export FLASK_APP=api.py
export FLASK_ENV=development
flask run --reload
```
L'option  `--reload` détectera les changements de fichiers et redémarrera le serveur automatiquement.


Ces commandes mettent l'application en mode développement et dirigent notre application à utiliser le fichier `api.py` dans notre dossier src. Le travail en mode développement affiche un débogueur interactif dans la console et redémarre le serveur à chaque fois que des modifications sont apportées. Si vous exécutez localement sous Windows, recherchez les commandes dans la [documentation Flask] (http://flask.pocoo.org/docs/1.0/tutorial/factory/).

L'application est exécutée sur `http://127.0.0.1:5000/` par défaut et est un proxy dans la configuration du frontend. 

### Configuration du Frontend

#### Installation de Node et NPM

Ce projet dépend de Nodejs et de Node Package Manager (NPM). Avant de continuer, vous devez télécharger et installer Node (le téléchargement inclut NPM) à partir de [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installation de Ionic Cli

L'interface de ligne de commande Ionic est nécessaire pour servir et construire le frontend. Les instructions pour l'installation de la CLI se trouvent dans les [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installation des dépendances du projet

Depuis le dossier du frontend, exécutez les commandes suivantes pour démarrer le client : 
```
npm install // une seule fois pour installer les dépendances 
```
## Exécuter votre front-end en mode Dev
```bash
ionic serve
```

Par défaut, le frontend sera exécuté sur localhost:8100.
