from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, role=None):
        user = self.create_user(username, email, password, role='admin')
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('service_client', 'Service Client'),
        ('gestionnaire', 'Gestionnaire des Demandes'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='service_client')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username