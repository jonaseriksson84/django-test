from django.db import models
from django.utils import timezone
import threading
import time


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False, unique=True)
    rent_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False)
    rented_by = models.CharField(max_length=100, null=True, unique=False)

    def save(self, *args, **kwargs):
        super(License, self).save()

    def mark_available(self, *args, **kwargs):
        time.sleep(15)
        self.rented = False
        print('License', self.identifier, 'expired at', timezone.now())
        super(License, self).save(*args, **kwargs)

    def rent(self, *args, **kwargs):
        print(self, *args, **kwargs)
        self.rented = True
        self.rent_date = timezone.now()
        super(License, self).save(*args, **kwargs)
        t = threading.Thread(target=self.mark_available)
        t.start()
