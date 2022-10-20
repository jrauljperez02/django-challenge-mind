
"""
Serializers for account APIs
"""
from dataclasses import fields
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
            'team_consult'
        ]
        read_only_fields = ['id']
