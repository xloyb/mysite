from django.urls import path,include
from . import views
# from .views import CategoryAPIView,ProduitAPIView,ProductViewset
from rest_framework import routers
from magasin.views import CategoryAPIView,ProduitAPIView,ProductViewset,ProductViewset


# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')


urlpatterns = [
  path('', views.index, name='index'),
  path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
  path('nouvcommande/',views.nouveaucommande,name='nouvcommande'),
  path('register/',views.register, name = 'register'), 
  path('api/category/', CategoryAPIView.as_view()),
  path('api/produit/', ProduitAPIView.as_view()),
  path('api/', include(router.urls)),
  path('api/product/<int:category_id>/',ProductViewset.as_view({'get': 'retrieve'}), name='product-detail'),
  
]