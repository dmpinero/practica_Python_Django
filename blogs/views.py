from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
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
        # Comprobar que existe el usuario
        #TODO. Refactorizar
        users = User.objects.filter(username=blog_username)
        user = users[0] if len(users) == 1 else None
        if user is not None:
            #TODO: Redireccionar a página 404 indicando que no existe el usuario solictado
            #TODO: Comprobar por qué no funciona con el usuario 'danielito2'
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
        #TODO. Refactorizar
        users = User.objects.filter(username=blog_username)
        user = users[0] if len(users) == 1 else None

        if user is None:
            raise Http404("El usuario indicado no existe")
        else:
            #TODO. Ver por qué esta consulta no devuelve las categorías
            posts = Post.objects.filter(pk=post_id, owner=user.id).prefetch_related('categories')
            post = posts[0] if len(posts) == 1 else None
            if post is None:
                #TODO: Redireccionar a página adecuada
                raise Http404("El post {0} no pertenece al usuario {1}".format(post_id, blog_username))

            context = {
                'post_detail': post
            }

        return render(request, 'posts/post-detail.html', context)