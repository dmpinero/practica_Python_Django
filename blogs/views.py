from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from blogs.models import Blog
from posts.models import Post


class BlogsView(View):
    """
    Visualiza todos los blogs publicados por los usuarios
    """
    def get(self, request):
        blogs = Blog.objects.all().select_related('owner')
        context = {
            'blogs_list': blogs
        }
        return render(request, 'blogs/home.html',context)

class BlogsUserView(View):
    """
    Visualiza todos los post publicados por un usuario
    """
    def get(self, request, blog_username):
        user = get_object_or_404(User, username=blog_username)  # Obtener usuario del sistema
        posts = Post.objects.filter(owner=user.pk).order_by('-created_at')

        context = {
            'posts_list': posts,
            'usuario': user,
        }
        return render(request, 'users/user-post-list.html', context)

class BlogPostDetailView(View):
    """
    Visualiza detalle de un post
    """
    def get(self, request, blog_username, post_id):
        user = get_object_or_404(User, username=blog_username)
        #TODO. Ver por qué esta consulta no devuelve las categorías
        #posts = Post.objects.filter(pk=post_id, owner=user.id).prefetch_related('categories')
        posts = Post.objects.filter(pk=post_id).prefetch_related('categories')
        post = posts[0] if len(posts) == 1 else None
        if post is None:
            raise Http404("El post {0} no pertenece al usuario {1}".format(post_id, blog_username))

        context = {
            'post_detail': post
        }

        return render(request, 'posts/post-detail.html', context)