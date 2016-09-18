from django.shortcuts import render
from django.views import View

from users.forms import LoginForm


class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario de login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'form': login_form}

        return render(request, 'users/login.html', context)

class LogoutView(View):
    pass
