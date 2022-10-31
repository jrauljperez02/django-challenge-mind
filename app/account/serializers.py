
"""
Serializers for account APIs
"""
from rest_framework import serializers

from core.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer for accounts."""

    class Meta:
        model = Account
        fields = [
            'id', 
            'account_name', 
            'account_customer', 
            'operational_responsable',
            'team_id'
        ]
        read_only_fields = ['id']
