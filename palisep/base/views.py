from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User 

from .models import *

from .serializers import *

# Create your views here.
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data
    
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
def getCategory(request):
    category = Categories.objects.get()
    serializer = CategoriesSerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def getBlasonnements(request):
    blasonnements = Blasonnements.objects.all()
    serializer = BlasonnementsSerializer(blasonnements, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getPresentation(request):
    presentation = Presentation.objects.all()
    serializer = PresentationSerializer(presentation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEquivalence(request):
    equivalence = Equivalence.objects.all()
    serializer = EquivalenceSerializer(equivalence, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPatronyme(request):
    patronyme = Patronyme.objects.all()
    serializer = PatronymeSerializer(patronyme, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPartnaire(request):
    partnaire = Partnaire.objects.all()
    serializer = PartnaireSerializer(partnaire, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGenealogy(request):
    genealogy = Genealogy.objects.all()
    serializer = GenealogySerializer(genealogy, many=True)
    return Response(serializer.data)

