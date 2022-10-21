from django.urls import include, path
from rest_framework import routers

from user.api.views import UserViewSet


router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
