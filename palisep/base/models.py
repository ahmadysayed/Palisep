from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.BooleanField()
    palisep = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)

class Armorial(models.Model):
    armorial_id = models.AutoField(primary_key=True)
    famille = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    date = models.DateField()
    country = models.CharField(max_length=255)
    fief = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    alliances = models.TextField()
    armoiries = models.TextField()
    note = models.TextField()
    le_clert = models.TextField()
    armorial_gen_champagne = models.CharField(max_length=255)
    note_armoriaux = models.CharField(max_length=255)
    crests = models.IntegerField()
    devise = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    sources = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    stamp = models.CharField(max_length=255)
    motto_shout = models.CharField(max_length=255)
    holding_support = models.CharField(max_length=255)
    decoration = models.CharField(max_length=255)
    ornaments_ext = models.CharField(max_length=255)
    emblem = models.CharField(max_length=255)
    images_geneal = models.TextField()
    image_doc = models.CharField(max_length=255)
    blasonnement_id = models.ForeignKey('Blasonnements', on_delete=models.CASCADE)
    id_genealogy = models.ForeignKey('genealogy', on_delete=models.CASCADE)
    id_patronym = models.ForeignKey('patronyme', on_delete=models.CASCADE)

    def __str__(self):
        return self.armorial_id 

class LegentPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    vedette_chan = models.CharField(max_length=255)
    autor_image = models.TextField()
    type_image = models.CharField(max_length=255)
    year_image = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    conversation_building = models.CharField(max_length=255)
    location_in_building = models.CharField(max_length=255)
    photo = models.TextField()
    city_INSEE_number = models.CharField(max_length=255)
    artificia_number_decrock = models.CharField(max_length=255)
    familly = models.CharField(max_length=255)
    representing_person = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    date = models.DateField()
    demonstration = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    ref_productions = models.CharField(max_length=255)
    biblio = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    cl_to_redo = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    edition_place = models.CharField(max_length=255)
    binding = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    cote = models.CharField(max_length=255)
    folio_emplacement = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    edition_year = models.CharField(max_length=255)
    provenance = models.CharField(max_length=255)
    blasonnement_id = models.ForeignKey('Blasonnements', on_delete=models.CASCADE)
    reference_id = models.ForeignKey('MyReferences', on_delete=models.CASCADE)
    shot_id = models.ForeignKey('shots', on_delete=models.CASCADE)
    category_id = models.ForeignKey('categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Details(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_img = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    conversation_building = models.CharField(max_length=255)
    photo = models.TextField()
    person = models.CharField(max_length=255)
    biography = models.CharField(max_length=255)
    parente = models.CharField(max_length=255)
    date = models.DateField()
    denomination = models.TextField()
    title = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    bibliography = models.CharField(max_length=255)
    emblem = models.TextField()
    authors = models.CharField(max_length=255)
    edition_place = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    edition_year = models.CharField(max_length=255)
    reliure = models.CharField(max_length=255)
    provenance = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    cote = models.CharField(max_length=255)
    folio_emplacement = models.CharField(max_length=255)
    crests = models.TextField()
    weapons = models.TextField()
    notes = models.TextField()
    devise = models.TextField()
    reference_id = models.ForeignKey('MyReferences', on_delete=models.CASCADE)
    shot_id = models.ForeignKey('shots', on_delete=models.CASCADE)
    category_id = models.ForeignKey('categories', on_delete=models.CASCADE)
    id_patronym = models.ForeignKey('patronyme', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shots(models.Model):
    shot_id = models.AutoField(primary_key=True)
    author_shot = models.CharField(max_length=255)
    type_shot = models.CharField(max_length=255)
    year_shot = models.CharField(max_length=255)

    def __str__(self):
        return self.author_shot

class MyReferences(models.Model):
    reference_id = models.AutoField(primary_key=True)
    ref_IM = models.CharField(max_length=255)
    ref_PA = models.CharField(max_length=255)
    ref_IA = models.CharField(max_length=255)
    ref_productions = models.CharField(max_length=255)

    def __str__(self):
        return self.ref_IM

class Genealogy(models.Model):
    id_genealogy = models.AutoField(primary_key=True)
    id_patronym = models.ForeignKey('patronyme', on_delete=models.CASCADE)
    name_image = models.CharField(max_length=255)

    def __str__(self):
        return self.name_image

class Partnaire(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patronyme(models.Model):
    id_patronym = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Equivalence(models.Model):
    id = models.AutoField(primary_key=True)
    expression = models.CharField(max_length=255)
    signification = models.CharField(max_length=255)

    def __str__(self):
        return self.expression

class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Blasonnements(models.Model):
    blasonnement_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
