"""
Serializers fot the user API View
"""

from django.contrib.auth import (
    get_user_model,
    authenticate
)
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer the user object"""

    class Meta:
        model = get_user_model()
        fields = [
                'id',
                'email',
                'password',
                'name', 
                'english_level', 
                'technical_skills', 
                'resume_link',
                'is_staff',
                'is_superuser',
            ]
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'min_length':5
            }
        }
