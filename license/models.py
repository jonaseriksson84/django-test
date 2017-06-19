from django.db import models
from django.utils import timezone
import threading
import time


# Create your models here.
class License(models.Model):
    identifier = models.CharField(max_length=100, blank=False, unique=True)
    rent_date = models.DateTimeField(blank=True, null=True)
    rented = models.BooleanField(default=False)
    rented_by = models.ForeignKey('auth.User', related_name='license', null=True)

    def save(self, *args, **kwargs):
        super(License, self).save()

    def mark_available(self, *args, **kwargs):
        time.sleep(15)
        self.rented = False
        self.rented_by = None
        print('License', self.identifier, 'expired at', timezone.now())
        super(License, self).save(*args, **kwargs)

    def rent(self, user):
        self.rented_by = user
        self.rented = True
        self.rent_date = timezone.now()
        print(repr(self.rented_by))
        super(License, self).save()
        t = threading.Thread(target=self.mark_available)
        t.start()
