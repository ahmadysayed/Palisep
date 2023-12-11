from django.shortcuts import render
from django.db.models import Q
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
def getBlasonnements(request):
    blasonnements = Blasonnements.objects.all()
    serializer = BlasonnementsSerializer(blasonnements, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request):
    category = Categories.objects.get()
    serializer = CategoriesSerializer(category)
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


@api_view(['GET'])
def getReferences(request):
    reference = MyReferences.objects.all()
    serializer = MyReferencesSerializer(reference, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getShots(request):
    shot = Shots.objects.all()
    serializer = ShotsSerializer(shot, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDetails(request):
    detail = Details.objects.all()
    serializer = DetailsSerializer(detail, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLegentPhotos(request):
    LegentPhoto = LegentPhotos.objects.all()
    serializer = LegentPhotosSerializer(LegentPhoto, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getArmorial(request):
    armorial = Armorial.objects.all()
    serializer = ArmorialSerializer(armorial, many=True)
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



# Create Apis

# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def createArmorial(request):
#     if request.method == 'POST':
#         serializer = ArmorialSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createBlasonnements(request):
    if request.method == 'POST':
        serializer = BlasonnementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createCategories(request):
    if request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createPresentation(request):
    if request.method == 'POST':
        serializer = PresentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createEquivalence(request):
    if request.method == 'POST':
        serializer = EquivalenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createPatronyme(request):
    if request.method == 'POST':
        serializer = PatronymeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createPartnaire(request):
    if request.method == 'POST':
        serializer = PartnaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createGenealogy(request):
    if request.method == 'POST':
        serializer = GenealogySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createReferences(request):
    if request.method == 'POST':
        serializer = MyReferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createShots(request):
    if request.method == 'POST':
        serializer = ShotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDetails(request):
    if request.method == 'POST':
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createLegentPhotos(request):
    if request.method == 'POST':
        serializer = LegentPhotosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createArmorial(request):
    if request.method == 'POST':
        serializer = ArmorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Update Apis

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateArmorial(request, pk):
    try:
        armorial = Armorial.objects.get(armorial_id=pk)
    except Armorial.DoesNotExist:
        return Response("Armorial not found", status=status.HTTP_404_NOT_FOUND)

    serializer = ArmorialSerializer(armorial, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateLegentPhotos(request, pk):
    try:
        legent_photo = LegentPhotos.objects.get(id=pk)
    except LegentPhotos.DoesNotExist:
        return Response("LegentPhoto not found", status=status.HTTP_404_NOT_FOUND)

    serializer = LegentPhotosSerializer(legent_photo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateDetails(request, pk):
    try:
        detail = Details.objects.get(id=pk)
    except Details.DoesNotExist:
        return Response("Details not found", status=status.HTTP_404_NOT_FOUND)

    serializer = DetailsSerializer(detail, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateCategories(request, pk):
    try:
        category = Categories.objects.get(category_id=pk)
    except Categories.DoesNotExist:
        return Response("Category not found", status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriesSerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateShots(request, pk):
    try:
        shot = Shots.objects.get(shot_id=pk)
    except Shots.DoesNotExist:
        return Response("Shot not found", status=status.HTTP_404_NOT_FOUND)

    serializer = ShotsSerializer(shot, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateMyReferences(request, pk):
    try:
        reference = MyReferences.objects.get(reference_id=pk)
    except MyReferences.DoesNotExist:
        return Response("Reference not found", status=status.HTTP_404_NOT_FOUND)

    serializer = MyReferencesSerializer(reference, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateGenealogy(request, pk):
    try:
        genealogy = Genealogy.objects.get(id_genealogy=pk)
    except Genealogy.DoesNotExist:
        return Response("Genealogy not found", status=status.HTTP_404_NOT_FOUND)

    serializer = GenealogySerializer(genealogy, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePartnaire(request, pk):
    try:
        partnaire = Partnaire.objects.get(id=pk)
    except Partnaire.DoesNotExist:
        return Response("Partnaire not found", status=status.HTTP_404_NOT_FOUND)

    serializer = PartnaireSerializer(partnaire, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePatronyme(request, pk):
    try:
        patronyme = Patronyme.objects.get(id_patronym=pk)
    except Patronyme.DoesNotExist:
        return Response("Patronyme not found", status=status.HTTP_404_NOT_FOUND)

    serializer = PatronymeSerializer(patronyme, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateEquivalence(request, pk):
    try:
        equivalence = Equivalence.objects.get(id=pk)
    except Equivalence.DoesNotExist:
        return Response("Equivalence not found", status=status.HTTP_404_NOT_FOUND)

    serializer = EquivalenceSerializer(equivalence, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePresentation(request, pk):
    try:
        presentation = Presentation.objects.get(id=pk)
    except Presentation.DoesNotExist:
        return Response("Presentation not found", status=status.HTTP_404_NOT_FOUND)

    serializer = PresentationSerializer(presentation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateBlasonnements(request, pk):
    try:
        blasonnement = Blasonnements.objects.get(blasonnement_id=pk)
    except Blasonnements.DoesNotExist:
        return Response("Blasonnement not found", status=status.HTTP_404_NOT_FOUND)

    serializer = BlasonnementsSerializer(blasonnement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


# Search Functionality

@api_view(['GET'])
def search(request):
    query = request.query_params.get('query', '')

    # Perform a case-insensitive search on category names
    categories_results = Categories.objects.filter(name__icontains=query)
    categories_serializer = CategoriesSerializer(categories_results, many=True)

    # Perform a case-insensitive search on armorial names
    armorial_results = Armorial.objects.filter(Q(famille__icontains=query) | Q(country__icontains=query))
    armorial_serializer = ArmorialSerializer(armorial_results, many=True)

    # Perform a case-insensitive search on legentphotos titles and descriptions
    legentphotos_results = LegentPhotos.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    legentphotos_serializer = LegentPhotosSerializer(legentphotos_results, many=True)

    # Perform a case-insensitive search on details titles
    details_results = Details.objects.filter(title__icontains=query)
    details_serializer = DetailsSerializer(details_results, many=True)

    # Combine the results from different models into a single response
    response_data = {
        'categories': categories_serializer.data,
        'armorial': armorial_serializer.data,
        'legentphotos': legentphotos_serializer.data,
        'details': details_serializer.data,
    }

    return Response(response_data)