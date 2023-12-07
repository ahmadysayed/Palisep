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
    
]
