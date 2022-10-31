from django.urls import include, path
from rest_framework import routers

from team.api.views import TeamViewSet


router = routers.DefaultRouter()
router.register('teams', TeamViewSet)

app_name = 'team'

urlpatterns = [
    path('', include(router.urls)),
]
