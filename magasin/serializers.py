from rest_framework.serializers import ModelSerializer
from .models import Categorie, Produit

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields ='__all__'

        