"""
Views for the team API
"""
from rest_framework import generics, authentication, permissions
from rest_framework import viewsets

from django_filters import rest_framework as filters
from team.api.serializsers import TeamSerializer
from core.models import Team

class TeamFilter(filters.FilterSet):
    class Meta:
        model = Team
        fields = {
            'team_name' : ['icontains']
        }

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class =  TeamFilter

    #permission_classes = [permissions.IsAuthenticated]