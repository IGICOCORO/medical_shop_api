from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "nom", "tel"
	search_fields = "fullname", 

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
	list_display = 'nom', 'unite', 'unite_sortant', 'rapport','quantite','prix_vente','picture','prix_achat'
	search_fields = "nom",
    
@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
	list_display = "produit", "quantite", "date", "user", "details", "prix_total", "prix_unitaire"
	search_fields = "produit", "quantite"

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
	list_display = "produit", "quantite", "commande","details","prix_achat","prix_vente"
	search_fields = "produit", "quantite",


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
	list_display = "user", "client", "date","a_payer","payee","reste"
	search_fields = "client", "date", 


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
	list_display = "commande","client","somme", "date","validated"
	search_fields = "somme", "date","client" 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
	list_display = "name",
	search_fields = "name",