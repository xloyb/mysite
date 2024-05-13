from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse


from django.template import loader
from .models import Produit
from .models import Fournisseur
from .models import Commande

from .forms import ProduitForm
from .forms import FournisseurForm
from .forms import commandeForm

from django.contrib.auth.decorators import login_required




from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages



from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer,ProductSerializer
from rest_framework import viewsets


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset



class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProductSerializer(produits, many=True)
        return Response(serializer.data)

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Coucou {username}, Votre compte a été créé avec succès !")
            return redirect("index")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})


# def register(request):
#    if request.method == "POST":
#       form = UserCreationForm(request.POST)
#    if form.is_valid():
#       form.save()
#       username = form.cleaned_data.get("username")
#       password = form.cleaned_data.get("password1")
#       user = authenticate(username=username, password=password)
#       login(request, user)
#       messages.success(request, f"Coucou {username}, Votre compte a été créé avec succès !")
#       return redirect("home")
#    else:
#       form = UserCreationForm()
#       return render(request, "registration/register.html", {"form": form})



# def index(request):
#    return HttpResponse("Première application django")



# def index(request):
#     products = Produit.objects.all()
#     context = {'products': products}
#     return render(request, 'magasin/mesProduits.html', context)

# def index(request):
#     if request.method == "POST":
#         form = ProduitForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/magasin')  # Rediriger vers une autre URL après l'enregistrement
#     else:
#         form = ProduitForm()  # Créer un formulaire vide
#     return render(request, 'magasin/majProduits.html', {'form': form})
#     list=Produit.objects.all()
#     return render(request,'magasin/vitrine.html',{'list':list})

@login_required
def Main(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html',context)

def nouveaucommande(request):
    if request.method == 'POST':
        form = commandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouvcommande')
    else:
        form = commandeForm()
    
    commandes = Commande.objects.all()    
    return render(request, 'magasin/NCommande.html', {'form': form, 'commandes': commandes})

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')
    else:
        form = FournisseurForm()
    
    fournisseurs = Fournisseur.objects.all()
    
    return render(request, 'magasin/Fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})


@login_required
def index(request):
   list=Produit.objects.all()
   return render(request,'magasin/vitrine.html',{'list':list})
@login_required
def indexacc(request):
      return render(request,'acceuil.html' )

def index111(request):
   if request.method == "POST" :
      form = ProduitForm(request.POST,request.FILES)
   if form.is_valid():
      form.save()
      return HttpResponseRedirect('/magasin')
   else :
      form = ProduitForm() #créer formulaire vide
   return render(request,'magasin/majProduits.html',{'form':form})

def index11(request):
   list=Produit.objects.all();
   return render(request,'F:\Iset\DSI\Semester_2\Django\env\TP5\mysite\magasin\\templates\\acceuil.html',{'list':list})

def vitrine(request):
   return render(request,'F:\Iset\DSI\Semester_2\Django\env\TP5\mysite\magasin\\templates\magasin\\vitrine.html' )