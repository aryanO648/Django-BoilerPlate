from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class OwnerRegisterModel(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.IntegerField()
    password = models.CharField(max_length = 50)

# class OwnerUser(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length = 50)
#     email = models.models.EmailField( max_length=40,unique = True)
#     is_active = models.BooleanField(default = True)
#     is_admin = models.BooleanField(default = False)

#     #objects = O/wnerUserManager()

#     USERNAME_FIELD = 'email'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.email


