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
    category = Categories.objects.all()
    serializer = CategoriesSerializer(category, many=True)
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
    query = request.GET.get('q', None)
    type_name = request.GET.get('type', None)
    
    if query is not None and type_name is not None:
        type_obj = Type.objects.filter(name__iexact=type_name).first()
        
        if type_obj is not None:
            armorials = Armorial.objects.filter(Q(famille__icontains=query) & Q(related_type=type_obj))
            legent_photos = LegentPhotos.objects.filter(Q(libelle_img__icontains=query) & Q(related_type=type_obj))
            details = Details.objects.filter(Q(libelle_img__icontains=query) & Q(related_type=type_obj))

            results = list(armorials.values()) + list(legent_photos.values()) + list(details.values())
            return Response(results)

        return Response({"message": "Type not found."}, status=404)

    return Response({"message": "No query parameter provided."}, status=400)




# Get By Id APIs

# User views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Armorial view
@api_view(['GET'])
def get_armorial(request, armorial_id):
    try:
        armorial = Armorial.objects.get(armorial_id=armorial_id)
    except Armorial.DoesNotExist:
        return Response({'error': 'Armorial not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ArmorialSerializer(armorial)
    return Response(serializer.data)


# LegentPhotos view
@api_view(['GET'])
def get_legent_photos(request, id):
    try:
        legent_photos = LegentPhotos.objects.get(id=id)
    except LegentPhotos.DoesNotExist:
        return Response({'error': 'LegentPhotos not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LegentPhotosSerializer(legent_photos)
    return Response(serializer.data)


# Details view
@api_view(['GET'])
def get_details(request, id):
    try:
        details = Details.objects.get(id=id)
    except Details.DoesNotExist:
        return Response({'error': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DetailsSerializer(details)
    return Response(serializer.data)


# Categories view
@api_view(['GET'])
def get_categories(request, category_id):
    try:
        category = Categories.objects.get(category_id=category_id)
    except Categories.DoesNotExist:
        return Response({'error': 'Categories not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriesSerializer(category)
    return Response(serializer.data)


# Shots view
@api_view(['GET'])
def get_shots(request, shot_id):
    try:
        shots = Shots.objects.get(shot_id=shot_id)
    except Shots.DoesNotExist:
        return Response({'error': 'Shots not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ShotsSerializer(shots)
    return Response(serializer.data)


# MyReferences view
@api_view(['GET'])
def get_my_references(request, reference_id):
    try:
        my_references = MyReferences.objects.get(reference_id=reference_id)
    except MyReferences.DoesNotExist:
        return Response({'error': 'MyReferences not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MyReferencesSerializer(my_references)
    return Response(serializer.data)


# Genealogy view
@api_view(['GET'])
def get_genealogy(request, id_genealogy):
    try:
        genealogy = Genealogy.objects.get(id_genealogy=id_genealogy)
    except Genealogy.DoesNotExist:
        return Response({'error': 'Genealogy not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = GenealogySerializer(genealogy)
    return Response(serializer.data)


# Partnaire view
@api_view(['GET'])
def get_partnaire(request, id):
    try:
        partnaire = Partnaire.objects.get(id=id)
    except Partnaire.DoesNotExist:
        return Response({'error': 'Partnaire not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PartnaireSerializer(partnaire)
    return Response(serializer.data)

# Patronyme view
@api_view(['GET'])
def get_patronyme(request, id_patronym):
    try:
        patronyme = Patronyme.objects.get(id_patronym=id_patronym)
    except Patronyme.DoesNotExist:
        return Response({'error': 'Patronyme not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PatronymeSerializer(patronyme)
    return Response(serializer.data)

# Equivalence view
@api_view(['GET'])
def get_equivalence(request, id):
    try:
        equivalence = Equivalence.objects.get(id=id)
    except Equivalence.DoesNotExist:
        return Response({'error': 'Equivalence not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EquivalenceSerializer(equivalence)
    return Response(serializer.data)

# Presentation view
@api_view(['GET'])
def get_presentation(request, id):
    try:
        presentation = Presentation.objects.get(id=id)
    except Presentation.DoesNotExist:
        return Response({'error': 'Presentation not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PresentationSerializer(presentation)
    return Response(serializer.data)

# Blasonnements view
@api_view(['GET'])
def get_blasonnements(request, blasonnement_id):
    try:
        blasonnements = Blasonnements.objects.get(blasonnement_id=blasonnement_id)
    except Blasonnements.DoesNotExist:
        return Response({'error': 'Blasonnements not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlasonnementsSerializer(blasonnements)
    return Response(serializer.data)

# Type view
@api_view(['GET'])
def get_type(request, type_id):
    try:
        type_obj = Type.objects.get(type_id=type_id)
    except Type.DoesNotExist:
        return Response({'error': 'Type not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TypeSerializer(type_obj)
    return Response(serializer.data)
