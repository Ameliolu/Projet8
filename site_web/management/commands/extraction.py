from django.core.management import BaseCommand

import json
import requests

from site_web.models import Category, Product


class Command(BaseCommand):
    def add_arguments(self, parser):
    # Positional arguments
        parser.add_argument('Categorie')
        
    def handle(self, *args, **options):
        
        CAT = options['Categorie']
        
        #constante, à modifier si besoin
        PAGE_SIZE = 20
    
        if CAT not in Category.objects.all():
        
            #on commence par créer la catégorie vu qu'elle n'existe pas
            nouvelle_categorie = Category(category_name = CAT)
            nouvelle_categorie.save()
            print("Une nouvelle catégorie a été créée.")
        
            #bloc pour déterminer le nb de page à parcourir
            url_base = 'https://fr.openfoodfacts.org/categorie/' + CAT + '.json'
            r = requests.get(url_base)
            data = r.json()
            nb_pages = data['count'] // PAGE_SIZE
            
            #une fois le nb de pages récupérées, on les interroge une par une
            page = 1
            while page <= nb_pages:
                url_page = 'https://fr.openfoodfacts.org/categorie/' + CAT + '/' + str(page) + '.json'
                r = requests.get(url_page)
                data = r.json()
                
                # boucle pour extirper toutes les id d'une page
                i = 0
                while i < PAGE_SIZE:
                    try:
                        nouveau_produit = Product(
                            category = nouvelle_categorie,
                            product_name_fr = data['products'][i]['product_name_fr'],
                            nutrition_grade_fr = data['products'][i]['nutrition_grade_fr'],
                            url_product = data['products'][i]['url'],
                            image_front_url = data['products'][i]['image_front_url'],
                            salt = data['products'][i]['nutriments']['salt_100g'],
                            fat = data['products'][i]['nutriments']['fat_100g'],
                            sugar = data['products'][i]['nutriments']['sugars_100g'],
                            saturated_fat = data['products'][i]['nutriments']['saturated-fat_100g'],
                        )
                        nouveau_produit.save()
                        print("Un nouveau produit a été ajouté")
                        i = i + 1
                    except:
                        i = i + 1
                        print("Données de mauvaise qualité")
                i = 0
              
                page = page + 1
                
            print("Terminé!")
        
        else:
            print("La catégorie a déjà été extraite.")
        
        
        
