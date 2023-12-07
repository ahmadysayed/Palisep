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

# Delete APIs

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteBlasonnement(request, pk):
    blasonnements = Blasonnements.objects.get(blasonnement_id=pk)
    blasonnements.delete()
    return Response("Blasonnement Deleted")



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePresentation(request, pk):
    presentation = Presentation.objects.get(id=pk)
    presentation.delete()
    return Response("Presentation Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteEquivalence(request, pk):
    equivalence = Equivalence.objects.get(id=pk)
    equivalence.delete()
    return Response("Equivalence Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePatronyme(request, pk):
    patronyme = Patronyme.objects.get(id_patronym=pk)
    patronyme.delete()
    return Response("Patronyme Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePartnaire(request, pk):
    partnaire = Partnaire.objects.get(id=pk)
    partnaire.delete()
    return Response("Partnaire Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteGenealogy(request, pk):
    genealogy = Genealogy.objects.get(id_genealogy=pk)
    genealogy.delete()
    return Response("Genealogy Deleted")



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteMyReferences(request, pk):
    references = MyReferences.objects.get(reference_id=pk)
    references.delete()
    return Response("Reference Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteShots(request, pk):
    shot = Shots.objects.get(shot_id=pk)
    shot.delete()
    return Response("Shot Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategories(request, pk):
    category = Categories.objects.get(category_id=pk)
    category.delete()
    return Response("Category Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteDetails(request, pk):
    detail = Details.objects.get(id=pk)
    detail.delete()
    return Response("Detail Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteLegentPhotos(request, pk):
    legentPhoto = LegentPhotos.objects.get(id=pk)
    legentPhoto.delete()
    return Response("LegentPhoto Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteArmorial(request, pk):
    armorial = Armorial.objects.get(armorial_id=pk)
    armorial.delete()
    return Response("Armorial Deleted")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAdmin(request, pk):
    admin = Admin.objects.get(id=pk)
    admin.delete()
    return Response("User Deleted")
