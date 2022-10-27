"""
Views for the recipe APIs
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Account
from account.api import serializers

from django_filters import rest_framework as filters

class AccountFilter(filters.FilterSet):
    class Meta:
        model = Account
        fields = {
            'account_name' :  ['icontains']
        }
class AccountViewSet(viewsets.ModelViewSet):
    """View for manage account APIs"""

    serializer_class = serializers.AccountSerializer
    queryset = Account.objects.all().order_by('-id')
    permission_classes = [IsAuthenticated]

    filterset_class = AccountFilter
