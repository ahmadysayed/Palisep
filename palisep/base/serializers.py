from rest_framework import serializers
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin']
    
    def get_id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



class ArmorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armorial
        fields = '__all__'




class LegentPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegentPhotos
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shots
        fields = '__all__'


class MyReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyReferences
        fields = '__all__'


class GenealogySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genealogy
        fields = '__all__'


class PartnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnaire
        fields = '__all__'


class PatronymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patronyme
        fields = '__all__'


class EquivalenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equivalence
        fields = '__all__'

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class BlasonnementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blasonnements
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'