# <span style="color:#696969">P10-Créez une API sécurisée RESTful en utilisant Django REST</span>

## <span style="color:#007ee6"> Pour commencer </span>

<span style="color:#696969">API permettant de remonter et suivre des problèmes techniques (issue tracking system) de Softdesk.</span>

## <span style="color:#007ee6"> Pré-requis </span>

* <span style="color:#696969">Editeur de code
* <span style="color:#696969">Pyhton 3
* <span style="color:#696969">Django
* <span style="color:#696969">Environnement virtuel de Python 3
* <span style="color:#696969">Shell,Terminal ou Git Bash

## <span style="color:#007ee6"> Installation </span>

1. <span style="color:#696969">Télécharger le dossier zip depuis Git Hub (<https://github.com/ThomasOCRPython/P10.git>) ou taper la commande: `git clone git@github.com:ThomasOCRPython/P10.git`.</span>

## <span style="color:#007ee6"> Démarrage </span>

1. <span style="color:#696969">A partir de votre terminal, se mettre au niveau du répertoire "P10".</span>
1. <span style="color:#696969">Créer un environnement virtuel avec la commande :
   `python3 -m venv env` ou `py -m venv env`</span>
1. <span style="color:#696969">Démarrer l'environnement virtuel avec les commandes:
   * pour mac: `source venv/bin/activate`
   * pour win: `env\Scripts\activate.bat`
   * Pour Git Bash: `source env/Scripts/activate`</span>
1. <span style="color:#696969">Lancer l'installation des bibliothèques nécessaires à partir du fichier "requiremts.txt" avec la commande: `pip install -r requirements.txt`</span>
1. <span style="color:#696969">Lancer le serveur Django:
`py manage.py runserver` ou `python manage.py runserver`</span> 
1. <span style="color:#696969">Utilisateurs déjà créés:
   * Nom: `Madga` Password: `secret`
   * Nom: `Ranga` Password: `secret`
   * Nom: `Thomas` Password: `secret`
   * Nom: `Rachel` Password: `secret`</span> 
1. <span style="color:#696969">Administrateur créé:
   * Nom: `thomas` Password: `secret`
   </span> 

## Créer une base de données

<span>Lancer les fichiers de migrations :
    `python manage.py makemigrations`</span>

# Migrer:
    python manage.py migrate


## Lancer le serveur
    http://127.0.0.1:8000

## Documentation API
<span>La documentation de l'API est disponible sur :
    `https://documenter.getpostman.com/view/19244405/UVkmQGZZ`</span>

