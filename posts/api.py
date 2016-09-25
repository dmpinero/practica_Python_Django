from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from users.permissions import UserPostPermission


class PostViewSet(ViewSet):
    permission_classes = (UserPostPermission,)  # Aplica los permisos indicados en este módulo

    def create(self, request):
        self.check_permissions(request)
        self.check_object_permissions(request, None)
        serializer = PostSerializer(data=request.data) # Pasa el diccionario de datos
        if serializer.is_valid():                      # Validar el serializador
            new_post = serializer.save(owner=self.request.user)  # Modificamos el owner del objeto con el usuario
                                                                 # autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolver datos del post creado
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """
        Obtiene el detalle de un post de un sistema.
        Si el post no es público deben aplicarse los permisos
        """
        self.check_permissions(request)
        post = get_object_or_404(Post, pk=pk)  # Busca el post por clave primaria
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def update(self, request, pk):
        """
        API de actualización de un post
        :param request: Petición
        :param pk: identificador del post a actualizar
        :return: Respuesta de Django REST Framework
        """
        self.check_permissions(request)
        post = get_object_or_404(Post, pk=pk)  # Busca el post por clave primaria
        self.check_object_permissions(request, post)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """
        API de borrado de post
        :param request: Petición
        :param pk: identificador del post a borrar
        :return:
        """
        self.check_permissions(request)
        post = get_object_or_404(Post, pk=pk)  # Busca el post por clave primaria
        self.check_object_permissions(request, post)
        post.delete()  # Borra el oist de la base de datos

        return Response(status=status.HTTP_204_NO_CONTENT)
