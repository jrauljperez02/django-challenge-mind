"""
Database models.
"""

from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.contrib.auth.models import User

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)


    english_level = models.CharField(null = True, max_length=25)
    technical_skills = models.TextField(null = True)
    resume_link = models.URLField(null = True, blank = True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Account(models.Model):
    """Account object in the system."""
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    account_name = models.CharField(max_length=255)
    account_customer = models.CharField(max_length=255)
    operational_responsable = models.CharField(max_length=255)
    team_consult = models.CharField(max_length=255)

    def __str__(self):
        return self.account_name


#TODO: Develop unit test for Team model
class Team(models.Model):
    """Team object in the system."""
    team_name = models.CharField(max_length=255)
    developers = models.ManyToManyField(User)

    def __str__(self):
        return self.team_name