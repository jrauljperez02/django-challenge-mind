"""
Views for the team API
"""
from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import generics, authentication, permissions
from rest_framework import viewsets
from team.api.serializsers import TeamSerializer
from core.models import Team

@extend_schema_view(
    list = extend_schema(description = 'Allow obtain a list of users'),
    retrieve = extend_schema(description = 'Allow obtain a user'),
    create = extend_schema(description = 'Allow create a new user'),
    update = extend_schema(description = 'Allow update an existing user'),
    destroy = extend_schema(description = 'Allow delete an existing user'),
)
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    # permission_classes = [permissions.IsAuthenticated]