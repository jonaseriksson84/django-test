import datetime
from django.utils import timezone
from django.db.models import Q
from license.models import License
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from license.serializers import LicenseSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    pagination_class = None

    @list_route()
    def rent(self, request):
        fifteensecondsago = timezone.now() - datetime.timedelta(seconds=15)
        license = License.objects.filter(Q(rent_date=None) | Q(
            rent_date__lt=fifteensecondsago)).first()
        serializer = LicenseSerializer(license)
        if license:
            license.rent()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
