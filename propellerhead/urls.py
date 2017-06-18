from django.conf.urls import url, include
from propellerhead import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'propellerhead', views.LicenseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
