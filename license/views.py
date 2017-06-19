import datetime
from django.utils import timezone
from django.db.models import Q
from license.models import License
from rest_framework import viewsets, status, generics
from rest_framework.decorators import list_route
from rest_framework.response import Response
from license.serializers import LicenseSerializer, UserSerializer
from django.contrib.auth.models import User


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    pagination_class = None

    @list_route()
    def rent(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)

        fifteensecondsago = timezone.now() - datetime.timedelta(seconds=15)
        license = License.objects.filter(Q(rent_date=None) | Q(
            rent_date__lt=fifteensecondsago)).first()
        serializer = LicenseSerializer(license)

        if license:
            print(request.user)
            license.rent()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
