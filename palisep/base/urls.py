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

    path('blasonnement-delete/<str:pk>/', views.deleteBlasonnement, name="blasonnement-delete")
    
]
