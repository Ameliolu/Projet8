from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User
from django.core.management import call_command

from unittest.mock import patch

from .views import *
from .models import Category, Product, Sauvegarde




# Tests sur les vues publiques
class TestPublicView(TestCase):

    def test_accueil(self):
        """Vérification de la page d'accueil"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html', 'accueil.html')
        self.assertEqual(response.status_code, 200)
        
#test sur le parcours d'un utilisateur
class UserTest(TestCase):

    def setUp(self):
        # création de l'utilisateur
        utilisateur_test = User.objects.create(username="utilisateur_test", email="utilisateur_test@mail.com")
        utilisateur_test.set_password('lEmdPdusi3cle!')
        utilisateur_test.save()
        
        # création d'une catégorie et de produits
        categorie_test = Category(category_name="categorie_test")
        categorie_test.save()
        
        produit_note_a = Product(
            category = Category.objects.get(category_name="categorie_test"),
            product_name_fr = "produit_note_a",
            nutrition_grade_fr = "a",
            url_product = "produit_note_a.com",
            image_front_url = "produit_note_a.png",
            salt = 0.1,
            fat = 0.1,
            sugar = 0.1,
            saturated_fat = 0.1,
            )
        produit_note_a.save()
        
        
    def test_existence_utilisateur(self):
        self.assertTrue(User.objects.filter(email="utilisateur_test@mail.com").exists())
        
    def test_categorie_test(self):
        self.assertTrue(Category.objects.filter(category_name="categorie_test").exists())
        
    def test_existence_produit_a(self):
        self.assertTrue(Product.objects.filter(product_name_fr = "produit_note_a").exists())
        
    def test_search_view(self):
        """On vérifie que l'url search répond correctement"""
        response = self.client.get('/search/' + "?product=note_a")
        self.assertTemplateUsed(response, 'base.html', 'search.html')
        self.assertEqual(response.status_code, 200)
        
    def test_search_results(self):
        """On vérifie que la recherche renvoie bien qch"""
        response = self.client.get('/search/' + "?product=note_a")
        self.assertEqual(response.context_data["object_list"].count(), 1)
        
    def test_product(self):
        """On vérifie que la fiche produit existe"""
        response = self.client.get('/product/' + '1')
        self.assertTemplateUsed(response, 'base.html', 'product.html')
        self.assertEqual(response.status_code, 200)
        
    def test_login_and_save(self):
        """On vérifie que l'user peut se logger et qu'il peut enregistrer un produit"""
        self.client.login(username="utilisateur_test", password="lEmdPdusi3cle!")
        user_id = User.objects.get(username="utilisateur_test").id
        response = self.client.get('/save/' + '1')
        self.assertFalse(Sauvegarde.objects.filter(user=user_id).exists())
