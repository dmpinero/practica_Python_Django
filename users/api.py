from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet
from users.permissions import UserPermission
from users.serializers import UserSerializer

class UserViewSet(ViewSet):
    """
    Endpoint de usuarios
    """
    permission_classes = (UserPermission,)

    def create(self, request):
        """
        Creación de usuario
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk):
        """
        Obtiene el detalle de un usuario
        Sólo puede visualizar el detalle de usuario un administrador o el propio usuario
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usaurio por clave primaria
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data)


    def update(self, request, pk):
        """
        API de actualización de un usuario
        Sólo puede actualizar los datos de un usuario un administrador o el propio usuario
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return: Respuesta de Django REST Framework
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        """
        API de borrado de usuarios
        Sólo puede borrar los datos de un usuario un administrador o el propio usuario
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return:
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        self.check_object_permissions(request, user)
        user.delete()  # Borra el usuario de la base de datos

        return Response(status=status.HTTP_204_NO_CONTENT)