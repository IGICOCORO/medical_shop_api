from django.contrib import admin
from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "fullname", "is_enterprise", "details"
	search_fields = "fullname", 

@admin.register(AutoMobile)
class AutoMobileAdmin(admin.ModelAdmin):
	list_display = 'nom', 'provenance', 'image', 'details'
	search_fields = "nom",
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
	list_display = "automobile", "details", "date_commande", "prix_commande", "date_arrivee", "prix_vente", "payee", "added_by", "client"
	search_fields = "automobile__nom", "client__fullname"

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = "commande", "montant", "date"
	search_fields = "commande__automobile__name", "commande__automobile__client", 