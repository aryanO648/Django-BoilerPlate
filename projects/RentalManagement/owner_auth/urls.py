
from django.urls import path,include
from .views import *
urlpatterns = [
    path('register/', OwnerRegisterApiView.as_view()),
    path('infoid/', GetOnwerById.as_view()),
]