from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('category/', views.getCategory, name='category'),
    path('blasonnement/', views.getBlasonnements, name='blasonnement'),
    path('presentation/', views.getPresentation, name='presentation'),
    path('equivalence/', views.getEquivalence, name='equivalence'),
    path('patronyme/', views.getPatronyme, name='patronyme'),
    path('partnaire/', views.getPartnaire, name='partnaire'),
    path('genealogy/', views.getGenealogy, name='genealogy'),
    path('reference/', views.getReferences, name='reference'),
    path('shot/', views.getShots, name='shot'),
    path('detail/', views.getDetails, name='detail'),
    path('legent-photo/', views.getLegentPhotos, name='legent-photo'),
    path('armorial/', views.getArmorial, name='armorial'),

    path('blasonnement-delete/<str:pk>/', views.deleteBlasonnement, name="blasonnement-delete"),
    path('presentation-delete/<str:pk>/', views.deletePresentation, name="presentation-delete"),
    path('equivalence-delete/<str:pk>/', views.deleteEquivalence, name="equivalence-delete"),
    path('patronyme-delete/<str:pk>/', views.deletePatronyme, name="patronyme-delete"),
    path('partnaire-delete/<str:pk>/', views.deletePartnaire, name="partnaire-delete"),
    path('genealogy-delete/<str:pk>/', views.deleteGenealogy, name="genealogy-delete"),
    path('references-delete/<str:pk>/', views.deleteMyReferences, name="references-delete"),
    path('references-delete/<str:pk>/', views.deleteShots, name="references-delete"),
    path('categories-delete/<str:pk>/', views.deleteCategories, name="categories-delete"),
    path('details-delete/<str:pk>/', views.deleteDetails, name="details-delete"),
    path('lengentphotos-delete/<str:pk>/', views.deleteLegentPhotos, name="lengentphotos-delete"),
    path('armorial-delete/<str:pk>/', views.deleteArmorial, name="armorial-delete"),
    path('user-delete/<str:pk>/', views.deleteAdmin, name="user-delete"),


    path('api/blasonnements/create/', views.createBlasonnements, name='create_blasonnements'),
    path('api/categories/create/', views.createCategories, name='create_categories'),
    path('api/presentation/create/', views.createPresentation, name='create_presentation'),
    path('api/equivalence/create/', views.createEquivalence, name='create_equivalence'),
    path('api/patronyme/create/', views.createPatronyme, name='create_patronyme'),
    path('api/partnaire/create/', views.createPartnaire, name='create_partnaire'),
    path('api/genealogy/create/', views.createGenealogy, name='create_genealogy'),
    path('api/references/create/', views.createReferences, name='create_references'),
    path('api/shots/create/', views.createShots, name='create_shots'),
    path('api/details/create/', views.createDetails, name='create_details'),
    path('api/legentphotos/create/', views.createLegentPhotos, name='create_legentphotos'),
    path('api/armorial/create/', views.createArmorial, name='create_armorial'),


    path('api/armorial/update/<int:pk>/', views.updateArmorial, name='update_armorial'),
    path('api/legentphotos/update/<int:pk>/', views.updateLegentPhotos, name='update_legentphotos'),
    path('api/details/update/<int:pk>/', views.updateDetails, name='update_details'),
    path('api/categories/update/<int:pk>/', views.updateCategories, name='update_categories'),
    path('api/shots/update/<int:pk>/', views.updateShots, name='update_shots'),
    path('api/myreferences/update/<int:pk>/', views.updateMyReferences, name='update_myreferences'),
    path('api/genealogy/update/<int:pk>/', views.updateGenealogy, name='update_genealogy'),
    path('api/partnaire/update/<int:pk>/', views.updatePartnaire, name='update_partnaire'),
    path('api/patronyme/update/<int:pk>/', views.updatePatronyme, name='update_patronyme'),
    path('api/equivalence/update/<int:pk>/', views.updateEquivalence, name='update_equivalence'),
    path('api/presentation/update/<int:pk>/', views.updatePresentation, name='update_presentation'),
    path('api/blasonnements/update/<int:pk>/', views.updateBlasonnements, name='update_blasonnements'),


    path('api/search/', views.search, name='search'),
    
]