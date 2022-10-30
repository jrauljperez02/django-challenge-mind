from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

logging.getLogger('error_logger').error('Token api')
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        token['english_level'] = user.english_level
        token['technical_skills'] = user.technical_skills
        token['resume_link'] = user.resume_link
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
