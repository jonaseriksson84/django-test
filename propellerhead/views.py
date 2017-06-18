# from django.shortcuts import render
from propellerhead.models import License
from rest_framework import viewsets
from propellerhead.serializers import LicenseSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
