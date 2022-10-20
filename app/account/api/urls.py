"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from account.api import views

router = DefaultRouter()
router.register('accounts', views.AccountViewSet)

app_name = 'account'

urlpatterns = [
    path('', include(router.urls)),
]