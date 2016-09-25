from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from posts.forms import PostForm
from posts.models import Post


class PostView(View):
    """
    Visualiza los últimos 5 post publicados por los usuarios
    """
    def get(self, request):
        # Devuelve los últimos 5 posts publicados por los usuarios
        # TODO: Los posts que se visualicen deben tener la fecha de publicación válida (a futuro no se publican)
        posts = Post.objects.filter().order_by('-created_at')
        context = {
            'posts_list': posts[:5]
        }
        return render(request, 'posts/home.html',context)

# TODO: Cuando se intente acceder a la url /new-post sin estar autenticado mostrar un mensaje de error en el
# formulario de login
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