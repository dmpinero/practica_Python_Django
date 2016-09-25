from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from posts.forms import PostForm
from posts.models import Post
from datetime import datetime

class PostView(View):
    """
    Visualiza los últimos 5 post publicados por los usuarios
    """
    def get(self, request):
        # Devuelve los últimos 5 posts publicados por los usuarios
        posts = Post.objects.filter(published_at__lt=datetime.now()).order_by('-created_at')  # Devolver posts publicados
        context = {
            'posts_list': posts[:5]
        }
        return render(request, 'posts/home.html',context)

# Formulario de login
class PostCreationView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crear un post
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PostForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'posts/new-post.html', context)


    def post(self, request):
        """
        Gestiona el alta de un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = ""  # Mensaje de respuesta
        post_form = PostForm(request.POST)  # Crea objeto de post con los datos del formulario
        if post_form.is_valid():            # Django recorre los campos del formulario y aplica a
                                       # cada uno los validadores
            title = post_form.cleaned_data.get('title')
            head = post_form.cleaned_data.get('head')
            body = post_form.cleaned_data.get('body')
            url_image_or_video = post_form.cleaned_data.get('url_image_or_video')
            published_at = post_form.cleaned_data.get('published_at')
            categories = post_form.cleaned_data.get('categories')
            post = Post.objects.create(title=title,
                                       head=head,
                                       body=body,
                                       url_image_or_video=url_image_or_video,
                                       published_at=published_at,
                                       categories=categories,
                                       owner=request.user
                                       )

            message = 'Post creado con éxito'
            post.save()  # Guardar nuevo usuario

        context = {'message': message, 'form': post_form}

        return render(request, 'posts/new-post.html', context)