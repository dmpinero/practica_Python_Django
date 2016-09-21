from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):

    # Campos a devolver en la respuesta
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username ) \
                and User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario {0} ya está siendo utilizado".format(username))
        return username

    def validate_email(self, email):
        if (self.instance is None or self.instance.email != email) \
                and User.objects.filter(email=email).exists():
            raise ValidationError("El email {0} ya está siendo utilizado".format(email))
        return email