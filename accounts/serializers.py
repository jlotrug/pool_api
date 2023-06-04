from .models import CustomUser
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CreateCustomUserSerializer(RegisterSerializer, serializers.ModelSerializer):
    class Meta:
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
        )
        model = CustomUser

    def custom_signup(self, request, user):
        
        
        # print("FIELDS HERE", self.Meta.fields)
        # print("REQUEST HERE", request)
        for field in self.Meta.fields:
            if hasattr(user, field) and not getattr(user, field):
                setattr(user, field, self.initial_data[field])

        user.save()

class UserDetailsSerializer(UserDetailsSerializer, serializers.ModelSerializer):
    print("User Serializer")
    class Meta:
        fields = [
            "id",
            "first_name",
            "last_name"
        ]
        model = CustomUser