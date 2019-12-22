from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import EnregistrementForm
from .models import Product, Sauvegarde

#Vue home
def accueil(request):
    return render(request, 'accueil.html')

#Vue pour s'enregistrer    
def signup(request):
    if request.method == 'POST':
        form = EnregistrementForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('accueil'))
    else:
        form = EnregistrementForm()
    return render(request, 'signup.html', {'form': form})

#Vue pour se déconnecter    
def deconnexion(request):
    logout(request)
    return redirect(reverse('accueil'))

#Vue en cas de recherche    
class SearchView(ListView):
    model = Product
    template_name = 'search.html'
    paginate_by = '6'

    def get_queryset(self):
        return Product.objects.filter(
            product_name_fr__icontains=self.request.GET.get('product')
        )

#Vue pour sauvegarder        
def sauvegarde(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    Sauvegarde.objects.get_or_create(
        user=user,
        product_sauvegarde=product
    )
    return redirect('accueil')

#Vue pour voir ses produts enregistrés    
class Choix(ListView):
    model = Sauvegarde
    template_name = 'sauvegardes.html'
    paginate_by = '6'
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

#Vue pour découvrir des aliments plus sains de la même catégorie        
class Substituts(ListView):
    model = Product
    template_name = 'substituts.html'
    paginate_by ='6'
    
    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return Product.objects.filter(
            category=product.category
        )

def legal(request):
    return render(request, 'legal.html')        