from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from blogs.serializers import BlogSerializer
from datetime import datetime
from posts.models import Post
from posts.serializers import PostListSerializer


class BlogListAPI(ListAPIView):
    """
    Endpoint de listado de blogs (es el listado de usuarios)
    """
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username')
    ordering_fields = ('username')
    serializer_class = BlogSerializer
    queryset = User.objects.all()

class PostsAPIView(ListAPIView):
    """
    Endpoint de listado de posts de un blog
    """
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body')
    ordering_fields = ('title', 'created_at')
    serializer_class = PostListSerializer

    def get_queryset(self):
        """
        Definición dinámica del queryset
        :return:
        """
        blog_username = self.kwargs['blog_username']
        if not self.request.user.is_authenticated:  # Usuario no autenticado
            posts = Post.objects.filter(published_at__lt=datetime.now()).order_by('-created_at') # Devolver posts publicados
        else:  # Usuario autenticado
            user = get_object_or_404(User, username=blog_username)  # Obtener usuario del sistema
            if (self.request.user.is_superuser) or (self.request.user == blog_username):  # Usuario administrador
                                                                                          # o propietario del blog
                posts = Post.objects.filter(owner=user).order_by('-created_at')  # Devolver todos los posts del usuario
            else:
                posts = Post.objects.filter(published_at__lt=datetime.now()).order_by('-created_at')  # Devolver posts publicados

        return posts  # Devolver respuesta