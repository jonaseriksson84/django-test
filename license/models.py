from django.db import models
from django.utils import timezone
import threading
import time


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False, unique=True)
    rent_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(License, self).save()

    def mark_available(self, *args, **kwargs):
        time.sleep(10)
        self.rented = False
        super(License, self).save(*args, **kwargs)

    def rent(self, *args, **kwargs):
        self.rented = True
        self.rent_date = timezone.now()
        super(License, self).save(*args, **kwargs)
        t = threading.Thread(target=self.mark_available)
        t.start()
