from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractUser
# Create your models here. 

class MyUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    phone = models.IntegerField()
    password = models.CharField(max_length = 50)
    