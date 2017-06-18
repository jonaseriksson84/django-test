from django.db import models


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False)
    rented = models.BooleanField(default=False)
    last_rented = models.DateTimeField()
