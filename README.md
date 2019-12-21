# Projet8
Ce projet permet de créer une plateforme web basée sur les données d'Openfoodfacts (https://fr.openfoodfacts.org). Elle permet de naviguer entre différents produits, de leurs trouver des alternatives et de sauvegarder ces alternatives. Si vous souhaitez l'utiliser, vous devez suivre les étapes suivantes :
1) Installez les librairies nécessaires :
```
pip install -r requirements.txt
```
2) Procédez aux migrations :
```
python manage.py makemigrations
python manage.py migrate
```
3) Complétez la base de données avec les produits que vous souhaitez avec la commande :
```
python manage.py extraction catégorie
```
Pour cela, commencez par selectionner une catégorie de produits sur openfoodfacts, par exemple les chouquettes (https://fr.openfoodfacts.org/categorie/chouquettes). Dans notre exempe, cela donnerait donc : python manage.py extraction chouquettes.

4) Accessoirement, il est conseillé pour vos développements de créer un profil administrateur avec la commande suivante :
```
python manage.py createsuperuser
```
5) Lancez le serveur local avec :
```
python manage.py runserver
```
6) Accédez à la plateforme via http://localhost:8000/