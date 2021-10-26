from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *


class ClientViewset(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]



class ProduitViewset(viewsets.ModelViewSet):
	serializer_class = ProduitSerializer
	queryset = Produit.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	
class CommandeViewset(viewsets.ModelViewSet):
	serializer_class = CommandeSerializer
	queryset = Commande.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class VenteViewset(viewsets.ModelViewSet):
	serializer_class = VenteSerializer
	queryset = Vente.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class AchatViewset(viewsets.ModelViewSet):
	serializer_class = AchatSerializer
	queryset = Achat.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]


class PaiementViewset(viewsets.ModelViewSet):
	serializer_class = PaiementSerializer
	queryset = Paiement.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class CategoriesViewset(viewsets.ModelViewSet):
	serializer_class = CategoriesSerializer
	queryset = Categories.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]	
	    