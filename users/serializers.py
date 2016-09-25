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
        """
        Crea una nueva instancia de User y la almacena en base de datos
        :param validated_data:
        :return:
        """
        instance = User()
        return self.update(instance, validated_data)

    def validate_username(self, username):
        """
        Validación de nombre de usuario. No debe estar en uso
        :param username:
        :return:
        """
        if (self.instance is None or self.instance.username != username ) \
                and User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario {0} ya está siendo utilizado".format(username))
        return username

    def validate_email(self, email):
        """
        Validación de correo electrónico. El correo electrónnico no debe estar en uso
        :param email:
        :return:
        """
        if (self.instance is None or self.instance.email != email) \
                and User.objects.filter(email=email).exists():
            raise ValidationError("El email {0} ya está siendo utilizado".format(email))
        return email

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a poartir de los datos de
        validated_data que contiene valores deserializados
        :param validated_data: Diccionario con los datos de usuario
        :return: objeto User
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))    # Encriptación de la contraseña
        instance.save()                                          # Guardar objeto en la base de datos

        return instance

