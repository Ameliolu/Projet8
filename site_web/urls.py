from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.decorators import login_required

from . import views
from .views import SearchView, Choix, Substituts
from .models import Product, Sauvegarde

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('signup/', views.signup, name='signup'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True) , name='login'),
    path('accounts/', login_required(TemplateView.as_view(template_name='accounts.html')) , name='accounts'),
    path('product/<pk>', DetailView.as_view(model=Product, template_name='product.html'), name='product'),
    path('search/', SearchView.as_view() , name='search'),
    path('sauvegarde/<pk>', views.sauvegarde, name='sauvegarde'),
    path('choix/', Choix.as_view(), name='choix'),
    path('substituts/<pk>', Substituts.as_view(), name='substituts'),
    path('legal/', views.legal, name='legal'),
]