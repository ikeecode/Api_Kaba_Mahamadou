# Api_Kaba_Mahamadou
-
- 👋 👀 🌱 💞️ 📫
-

- Api_Kaba_Mahamadou est un mini projet qui couvre:
-    1. Utilisation d'une API en python
-    2. Programmation Orientée Objet en python
-    3. Utilisation de mysql.connector

## Architecture du projet
-  ../Api_Kaba_Mahamadou/
-  ├── controllers
-  │   ├── controller.py
-  │   └── __init__.py
-  │  
-  ├── models
-  │   ├── albums.py
-  │   ├── comments.py
-  │   ├── __init__.py
-  │   ├── models.py
-  │   ├── models.sql
-  │   ├── my.ini
-  │   ├── photos.py
-  │   ├── posts.py
-  │   ├── refactory_of_models.py
-  │   ├── todos.py
-  │   └── users.py
-  ├── README.md
-  ├── refactoring.py
-  └── views
-      └── main.py
___
### Model
* Dossier __*models*__
-  Dans ce dossier on a toutes les classes strutures des classes:
      * users
      * todos
      * posts
      * comments
      * albums
      * photos


___
### View
* Dossier __*views*__
-  Dans ce dossier on a les differents menu pour le coté utilisateur:
*  fichier : *main.py*
      * le menu principal
      * le menu de selection

___
### Controller
* Dossier *controllers*
-  Dans ce dossier on a le controller qui fait les opérations sur le model:
  fichier : *controller.py*


Pour executer le projet il faut faire:
```bash
                                    cd Api_Kaba_Mahamadou/views
                                    python3 main.py
```
