from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model

class Reader(AbstractUser):
    READER_TITLE = {
        "Mr": "Mr",
        "Mrs": "Mrs",
        "Ms": "Ms",
        "Dr": "Dr"
    }
    # If no explicit primary is defined, Django will generate an id for us
    # Class attributes will represent table columns
    username = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=10, null=True, blank=True, choices=READER_TITLE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr', 'Mrs', 'Ms', 'Dr'])
            )
        ]

