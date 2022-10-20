"""
Views for the recipe APIs
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Account
from account.api import serializers

from drf_spectacular.utils import extend_schema, extend_schema_view

# @extend_schema_view(
#     list = extend_schema(description = 'Allow obtain a account list'),
#     retrieve = extend_schema(description = 'Allos obtain a specific account'),
#     create = extend_schema(description = 'Allow create a new account'),
#     update = extend_schema(description = 'Allow update an existing account'),
#     destroy = extend_schema(description = 'Allows delete a account'),
# )
class AccountViewSet(viewsets.ModelViewSet):
    """View for manage account APIs"""

    serializer_class = serializers.AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve accounts for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
        # return self.queryset.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)