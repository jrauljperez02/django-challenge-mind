"""
Serializer for team APIs
"""
from dataclasses import fields
from django.contrib.auth import (
    get_user_model,
)
from rest_framework import serializers
from core.models import Team

class TeamSerializer(serializers.ModelSerializer):
    """Serializer for the team object"""

    class Meta:
        model = Team
        fields = [
            'id',
            'team_name',
            'coworkers'
        ]
        read_only_fields = ['id']