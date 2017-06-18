from django.db import models


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False, unique=True)
    rented = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier
