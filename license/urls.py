from django.conf.urls import url, include
from license import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'license', views.LicenseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
