from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES_PRODUITS = {
	(1,'Petite et grande chururgie'),
	(2,'Consommables et Equipement médicaux'),
	(3,'Materiel de la chururgie'),
	(4,'Produits CONWELL'),
	(5,'Produits de laboratoire'),
	(6,'Produits Dentaires'),
	(7,'Tuyauterie')
}


class Client(models.Model):
	id = models.SmallAutoField(primary_key=True)
	nom = models.CharField(max_length=50)
	tel = models.CharField(max_length=50)

	class Meta:
		unique_together = ('nom','tel')

class Produit(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=50, unique=True)
	unite = models.CharField(max_length=50, verbose_name='unité de mesure')
	unite_sortant = models.CharField(max_length=50)
	rapport = models.FloatField(default=1)
	quantite = models.FloatField(editable=False, default=0)
	prix_vente = models.FloatField(default=0)
	picture = models.ImageField(blank=True, null=True, upload_to='products/')
	prix_achat = models.FloatField(null=True, editable=False)

	def __str__(self):
		return f"{self.nom}"
		def save(self, *args, **kwargs):
			if self.quantite<0:
				raise Exception("Produit.la quantite ne peut pas etre negative")
			super().save(*args, **kwargs)

	class Meta:
		ordering = "nom",


class Categories(models.Model):
	name = models.CharField(max_length=20)
	Categorie = models.CharField(max_length=50,default=1,choices=CATEGORIES_PRODUITS)
	def __str__(self):
		return self.name

class Achat(models.Model):
	id = models.BigAutoField(primary_key=True)
	produit = models.ForeignKey("Produit", on_delete=models.PROTECT)
	quantite = models.FloatField()
	date = models.DateTimeField(blank=True, default=timezone.now)
	user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
	details = models.TextField(blank=True, null=True)
	prix_total = models.FloatField()
	prix_unitaire = models.FloatField()

	def __str__(self):
		return f"{self.produit.nom} par {self.user.username}"

	def save(self, *args, **kwargs):
		if self.quantite<0:
			raise Exception("Achat.la quantite ne peut pas etre negative")
		super().save(*args, **kwargs)

	class Meta:
		ordering = ["produit"]

class Vente(models.Model):
	id = models.BigAutoField(primary_key=True)
	produit = models.ForeignKey("Produit", on_delete=models.PROTECT)
	quantite = models.FloatField()
	commande = models.ForeignKey("Commande", on_delete=models.CASCADE)
	details = models.TextField(blank=True, null=True)
	prix_achat = models.FloatField(editable=False, null=True)
	prix_vente = models.FloatField(editable=False, default=0)

	def save(self, *args, **kwargs):
		if self.quantite<=0:
			raise Exception("Vente.la quantite ne peut pas etre negative")
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.quantite} {self.produit} {self.commande.date}"

class Commande(models.Model):
	id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
	date = models.DateTimeField(blank=True, default=timezone.now)
	a_payer = models.PositiveIntegerField(default=0, editable=False)
	payee = models.PositiveIntegerField(default=0., editable=False)
	reste = models.PositiveIntegerField(default=0., editable=False)
	uncommited = models.PositiveIntegerField(default=0, editable=False)

	def __str__(self):
		return f"commande valant {self.a_payer}"

	def save(self, *args, **kwargs):
		if self.payee > self.a_payer:
			raise Exception("Commande.payee ne peut pas etre grand que Commande.a_payer")
		super().save(*args, **kwargs)

	class Meta:
		ordering = "-pk",

class Paiement(models.Model):
	id = models.AutoField(primary_key=True)
	commande = models.ForeignKey("Commande", null=True, on_delete=models.SET_NULL)
	somme = models.PositiveIntegerField(verbose_name='somme payée', default=0)
	client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
	date = models.DateTimeField(editable=False, default=timezone.now)
	validated = models.BooleanField(default=False)

def __str__(self):
		return f"Paiement du {self.date} pour une {self.commande}"


