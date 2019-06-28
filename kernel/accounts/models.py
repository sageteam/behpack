import uuid
import secrets

from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()


class Profile(models.Model):
    MEMBER = 1
    GENIUES = 2
    SUPERVISOR = 3

    ROLE_CHOICES = (
        (MEMBER, 'Member'),
        (GENIUES, 'Genius'),
        (SUPERVISOR, 'SuperVisor'),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length = 11)
    national_code = models.CharField(max_length = 10)

    def __str__(self): 
        return self.user.email
