from django.urls import path,include
from .views import *
urlpatterns = [
    path('OwnerRegiste/', OwnerRelationApiView.as_view()),
    path('RenterRegister/', RenterRelationApiView.as_view()),
]