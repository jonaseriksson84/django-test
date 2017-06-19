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
        # Check that user is authenticated, otherwise forbidden
        if not request.user.is_authenticated:
            return Response({"errorMessage": "You must be logged in to rent a license"},
                            status=status.HTTP_403_FORBIDDEN)

        if License.objects.filter(rented_by=request.user):
            return Response({"errorMessage": "You can only rent 1 license at a time"},
                            status=status.HTTP_403_FORBIDDEN)

        fifteensecondsago = timezone.now() - datetime.timedelta(seconds=15)
        print(License.objects.filter(rented_by=request.user))
        license = License.objects.filter(Q(rent_date=None) | Q(
            rent_date__lt=fifteensecondsago)).first()
        serializer = LicenseSerializer(license)

        if license:
            license.rent(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"errorMessage": "No licenses currently available on server"},
                            status=status.HTTP_404_NOT_FOUND)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
