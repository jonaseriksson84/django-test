# from django.shortcuts import render
from license.models import License
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from license.serializers import LicenseSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

    @list_route()
    def rent(self, request):
        unrented = License.objects.all()
        print(unrented)
        return Response(LicenseSerializer(unrented.data))
