from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name_fr = models.CharField(max_length=255)
    nutrition_grade_fr = models.CharField(max_length=1)
    url_product = models.CharField(max_length=255)
    image_front_url = models.CharField(max_length=255)
    
    salt = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    sugar = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.product_name_fr

class Sauvegarde(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_sauvegarde = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_sauvegarde