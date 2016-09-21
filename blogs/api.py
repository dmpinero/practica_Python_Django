from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.serializers import UserSerializer, UserListSerializer

class BlogsViewSet(ViewSet):

    """
    Endpoint de listado de blogs
    """
    def list(self, request):
        blogs = Blogs.objects.all()
        serializer = BlogSerializer(blogs, many=True)  # Convierte lista de usuarios en lista de diccionarios
        return Response(serializer.data)
