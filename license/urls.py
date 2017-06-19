from django.conf.urls import url, include
from license import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'license', views.LicenseViewSet)
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
