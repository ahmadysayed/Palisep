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
    famille = models.CharField(max_length=255, null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    fief = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    alliances = models.TextField(null=True, blank=True)
    armoiries = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    le_clert = models.TextField(null=True, blank=True)
    armorial_gen_champagne = models.CharField(max_length=255,null=True, blank=True)
    note_armoriaux = models.CharField(max_length=255, null=True, blank=True)
    crests = models.TextField(null=True, blank=True)
    devise = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    observations = models.CharField(max_length=255, null=True, blank=True)
    sources = models.CharField(max_length=255, null=True, blank=True)
    document = models.CharField(max_length=255, null=True, blank=True)
    stamp = models.CharField(max_length=255, null=True, blank=True)
    motto_shout = models.CharField(max_length=255, null=True, blank=True)
    holding_support = models.CharField(max_length=255, null=True, blank=True)
    decoration = models.CharField(max_length=255, null=True, blank=True)
    ornaments_ext = models.CharField(max_length=255, null=True, blank=True)
    emblem = models.CharField(max_length=255, null=True, blank=True)
    images_geneal = models.TextField(null=True, blank=True)
    image_doc = models.CharField(max_length=255, null=True, blank=True)
    blasonnement_id = models.ForeignKey('Blasonnements', null=True, blank=True, on_delete=models.CASCADE)
    id_genealogy = models.ForeignKey('Genealogy', null=True, blank=True, on_delete=models.CASCADE)
    id_patronym = models.ForeignKey('Patronyme', null=True, blank=True, on_delete=models.CASCADE)
    related_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.armorial_id)

class LegentPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    libelle_img = models.CharField(max_length=255, null=True, blank=True)
    vedette_chan = models.CharField(max_length=255, null=True, blank=True)
    autor_image = models.TextField(null=True, blank=True)
    type_image = models.CharField(max_length=255, null=True, blank=True)
    year_image = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    conversation_building = models.CharField(max_length=255, null=True, blank=True)
    location_in_building = models.CharField(max_length=255, null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    city_INSEE_number = models.CharField(max_length=255, null=True, blank=True)
    artificia_number_decrock = models.CharField(max_length=255, null=True, blank=True)
    familly = models.CharField(max_length=255, null=True, blank=True)
    representing_person = models.CharField(max_length=255, null=True, blank=True)
    quality = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    denomination = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    category_id = models.ForeignKey('categories', on_delete=models.CASCADE, null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    ref_productions = models.CharField(max_length=255, null=True, blank=True)
    biblio = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    cl_to_redo = models.CharField(max_length=255, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    edition_place = models.CharField(max_length=255, null=True, blank=True)
    binding = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    section = models.CharField(max_length=255, null=True, blank=True)
    cote = models.CharField(max_length=255, null=True, blank=True)
    folio_emplacement = models.CharField(max_length=255, null=True, blank=True)
    editor = models.CharField(max_length=255, null=True, blank=True)
    edition_year = models.CharField(max_length=255, null=True, blank=True)
    provenance = models.CharField(max_length=255, null=True, blank=True)
    blasonnement_id = models.ForeignKey('Blasonnements', on_delete=models.CASCADE, null=True, blank=True)
    reference_id = models.ForeignKey('MyReferences', on_delete=models.CASCADE, null=True, blank=True)
    shot_id = models.ForeignKey('shots', on_delete=models.CASCADE, null=True, blank=True)
    
    related_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Details(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_img = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    conservation_building = models.CharField(max_length=255, null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    person = models.CharField(max_length=255, null=True, blank=True)
    biography = models.CharField(max_length=255, null=True, blank=True)
    parente = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    denomination = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    bibliography = models.CharField(max_length=255, null=True, blank=True)
    emblem = models.TextField(null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    edition_place = models.CharField(max_length=255,null=True, blank=True)
    editor = models.CharField(max_length=255, null=True, blank=True)
    edition_year = models.CharField(max_length=255, null=True, blank=True)
    reliure = models.CharField(max_length=255, null=True, blank=True)
    provenance = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    section = models.CharField(max_length=255, null=True, blank=True)
    cote = models.CharField(max_length=255, null=True, blank=True)
    folio_emplacement = models.CharField(max_length=255, null=True, blank=True)
    crests = models.TextField(null=True, blank=True)
    weapons = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    devise = models.TextField(null=True, blank=True)
    reference_id = models.ForeignKey('MyReferences', on_delete=models.CASCADE, null=True, blank=True)
    shot_id = models.ForeignKey('shots', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('categories', on_delete=models.CASCADE, null=True, blank=True)
    id_patronym = models.ForeignKey('patronyme', on_delete=models.CASCADE, null=True, blank=True)
    related_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Shots(models.Model):
    shot_id = models.AutoField(primary_key=True)
    author_shot = models.CharField(max_length=255, null=True, blank=True)
    type_shot = models.CharField(max_length=255, null=True, blank=True)
    year_shot = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.author_shot

class MyReferences(models.Model):
    reference_id = models.AutoField(primary_key=True)
    ref_IM = models.CharField(max_length=255, null=True, blank=True)
    ref_PA = models.CharField(max_length=255, null=True, blank=True)
    ref_IA = models.CharField(max_length=255, null=True, blank=True)
    ref_productions = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ref_IM

class Genealogy(models.Model):
    id_genealogy = models.AutoField(primary_key=True)
    id_patronym = models.ForeignKey('patronyme', on_delete=models.CASCADE, null=True, blank=True)
    name_image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_image

class Partnaire(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Patronyme(models.Model):
    id_patronym = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Equivalence(models.Model):
    id = models.AutoField(primary_key=True)
    expression = models.CharField(max_length=255, null=True, blank=True)
    signification = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.expression

class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description

class Blasonnements(models.Model):
    blasonnement_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name) if self.name else f"Blasonnement {self.blasonnement_id}"

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)