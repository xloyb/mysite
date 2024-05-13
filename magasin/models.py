from django.db import models
from datetime import date
# Create your models here.


from datetime import date

class Categorie(models.Model):
    TYPE_CHOICES=[
('Al','Alimentaire'), ('Mb','Meuble'),
('Sn','Sanitaire'), ('Vs','Vaisselle'),
('Vt','Vêtement'),('Jx','Jouets'),
('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(choices=TYPE_CHOICES,max_length=50, default='Alimentation')
    def  __str__(self):
            return self.name+"";

class Produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    libelle=models.CharField("Libellé",max_length=100)
    description=models.TextField()
    prix=models.DecimalField("Prix unitaire (€)", max_digits=10,decimal_places= 3)
    type = models.CharField(choices=TYPE_CHOICES ,default='em' ,max_length=2 ) 
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    Fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)


    def  __str__(self):
            return self.libelle+""+self.description+""+str(self.prix)


class Fournisseur (models.Model):
    nom = models.CharField("Nom du fournisseur",max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField("Telephone",max_length=8)

    def  __str__(self):
            return self.nom+""+self.adresse+""+self.email+""+self.telephone

            

class ProduitC(Produit):
    duree_garantie = models.CharField(max_length=100)
    def  __str__(self):
            return self.duree_garantie+"";

class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)
    def  __str__(self):
            return self.duree_garantie+"";

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def  __str__(self):
            return self.dateCde+""+self.totalCde;

    def calculate_total_price(self):
        total_price = sum(produit.prix for produit in self.produits.all())
        return total_price




