# from django.shortcuts import render
from license.models import License
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from license.serializers import LicenseSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

    @list_route()
    def rent(self, request):

        license = License.objects.filter(rented=False).first()
        serializer = LicenseSerializer(license)
        if license:
            license.rented = True
            # license.save()
            print(license.identifier)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


"""
        class UserViewSet(viewsets.ReadOnlyModelViewSet):
            queryset = User.objects.all()
            serializer_class = UserSerializer

            @detail_route(methods=['post'])
            def register(request):
                serializer = UserSerializer(data=request.DATA)
                if serializer.is_valid():
                    user = User.objects.create_user(
                        username = serializer.init_data['username'],
                        password = serializer.init_data['password'],
                    )

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""