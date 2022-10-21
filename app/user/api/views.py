"""
Views for the user API
"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.contrib.auth import get_user_model

from rest_framework import generics, authentication, permissions
from rest_framework import viewsets
from user.api.serializers import UserSerializer

class ManageUserView(generics.RetrieveAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user. """
        return self.request.user

@extend_schema_view(
    list = extend_schema(description = 'Allow obtain a list of users'),
    retrieve = extend_schema(description = 'Allow obtain a user'),
    create = extend_schema(description = 'Allow create a new user'),
    update = extend_schema(description = 'Allow update an existing user'),
    destroy = extend_schema(description = 'Allow delete an existing user'),
)
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.IsAuthenticated]