# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader

# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )

# # from django.urls import reverse_lazy
# from blog.forms import PostForm
# # from .models import Produit

# from .models import post


# def home(request):
#     return render(request, "bloghome.html")

# # class ListeProduits(ListView):
# #     model = Produit
# #     template_name = 'mag/liste_produits.html'
# #     context_object_name = 'produits'
# # class DetailProduit(DetailView):
# #     model = Produit
# #     template_name = 'mag/detail_produit.html'
# #     context_object_name = 'produit'


# class CreerPost(CreateView):
#     model = post
#     template_name = 'blog/creer_produit.html'
#     form_class = PostForm
#     success_url = reverse_lazy('liste_produits')


# # class ModifierProduit(UpdateView):
# #     model = Produit
# #     template_name = 'mag/modifier_produit.html'
# #     form_class = ProduitForm
# #     success_url = reverse_lazy('liste_produits')
# # class SupprimerProduit(DeleteView):
# #     model = Produit
# #     template_name = 'mag/supprimer_produit.html'
# #     success_url = reverse_lazy('liste_produits')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.forms import PostForm
from .models import post

def home(request):
    return render(request, "bloghome.html")

class CreerPost(CreateView):
    model = post
    template_name = 'blog/creer_produit.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')  

class ModifierPost(UpdateView):
    model = post
    template_name = 'blog/modifier_produit.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')

class SupprimerPost(DeleteView):
    model = post
    template_name = 'blog/supprimer_produit.html'
    success_url = reverse_lazy('liste_posts')

class ListePosts(ListView):
    model = post
    template_name = 'blog/liste_posts.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = post
    template_name = 'blog/detail_produit.html'
    context_object_name = 'post'
