from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model

class NIC(models.Model):
    nic_number = models.CharField(max_length=10, primary_key=True)
    delivery_date = models.DateField()
    #expiration_date = models.DateField()
    expiration_date = models.GeneratedField(
        expression = models.F('delivery_date') + timedelta(days=1826),
        output_field = models.DateField(),
        db_persist = True
    )
    # GeneratedField

    def __str__(self):
        return f'{self.nic_number}(del: {self.delivery_date}, exp: {self.expiration_date})'


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
    nic = models.OneToOneField(
        'reader.NIC', 
        related_name='reader', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
        )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr', 'Mrs', 'Ms', 'Dr'])
            )
        ]

