# Configuration
Une fois que le dépôt GitHub a été cloné sur votre machine locale, vous pouvez exécuter :

```
pipenv install
```
depuis le racine du projet pour installer les dépendances requises et créer un environnement virtuel.
Il est nécessaire d’avoir pipenv installé sur votre machine pour effectuer cette opération.
Une fois installé, vous pouvez lancer le serveur API depuis la racine du projet Django (softdesksupport) :

```
pipenv run python manage.py runserver
```
Ainsi, toutes les opérations habituelles que vous effectueriez avec manage.py doivent être exécutées avec :

```
pipenv run
```

# Opérations sur l’API
Toute personne peut créer un compte utilisateur via une requête POST.
Elle doit indiquer un nom d'utilisateur, une adresse e-mail, un mot de passe, un âge (validé à partir de 15 ans), si elle peut être contactée (can_be_contacted) et si ses données peuvent être partagées (can_data_be_shared).

Toute personne disposant d’un nom d'utilisateur et d’un mot de passe valides peut obtenir un JSON Web Token et un jeton de rafraîchissement.
Elle doit envoyer son nom d'utilisateur et son mot de passe via POST à l’adresse suivante :
http://127.0.0.1:8000/api/token/

Tout utilisateur authentifié peut créer un projet via une requête POST.
Il doit spécifier un titre, une description et un type (front-end / back-end / iPhone / Android).

Tout utilisateur authentifié peut s’ajouter comme contributeur à un projet donné.

L’auteur d’un projet peut retirer n’importe lequel des contributeurs.

Tout utilisateur authentifié qui est contributeur d’un projet peut créer un ticket (issue) lié à ce projet.
Tout utilisateur authentifié qui est contributeur d’un projet peut créer un commentaire sur un ticket lié à ce projet.

Les auteurs de commentaires, de tickets et de projets peuvent les modifier ou les supprimer.

Un utilisateur peut supprimer son propre compte ; cela entraîne également la suppression de tous les projets, commentaires ou tickets qu’il a créés.

# Configuration

Once the github repository has been cloned on your local machine, you can run:
```
pipenv install
```
from the root of the project to install the required dependencies and establish a virtual environment.
It is necessary for you to have pipenv installed on your machine in order to do this.
Once installed, you can launch the api server from the root of the django project (softdesksupport).
```
pipenv run python manage.py runserver
```
In this way, all the normal operations you would do with manage.py must be executed with 
```
pipenv run
```

# Operations on the API

Anyone can create a user account via POST.
They must specify username, email, password, age (validated 15+), can_be_contacted, and can_data_be_shared.

Anyone with a valid username and password can obtain a JSON Web Token and refresh token.
They must send their username and password via POST to http://127.0.0.1:8000/api/token/ 

Any authenticated user can create a project via POST.
They must specify title, description, and type (front-end/back-end/iphone/android).

Any authenticated user can add themselves as a contributor to a specified project.

The author of a given project can remove any of the contributors from it.

Any authenticated user that is a contributor to a project can create an issue related to it.
Any authenticated user that is a contributor to a project can create a comment on an issue related to it.

Authors of comments, issues, and projects can modify or delete them.

A user can delete their own account; this in turn deletes all projects, comments, or issues they have created.