from django.db import models
from owner_auth.models import OwnerRegisterModel
# Create your models here.

class RegisterModel(models.Model):
    # user = models.CharField(OwnerRegisterModel)
    name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    password = models.CharField(max_length = 50)
    room = models.IntegerField()
    price = models.IntegerField()
