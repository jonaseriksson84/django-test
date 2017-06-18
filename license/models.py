from django.db import models


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False, unique=True)
    rent_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False)
