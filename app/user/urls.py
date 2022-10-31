from django.urls import include, path
from rest_framework import routers

from user.views import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
]