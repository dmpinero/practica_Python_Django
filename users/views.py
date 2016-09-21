from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignUpForm


class HomeUserView(View):
    def get(self, request):
        """
        Renderiza el home del usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        return render(request, 'users/login.html', None)

class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario de login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = ""
        login_form = LoginForm()
        context = {'message': message, 'form': login_form}

        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login de usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = ""                                            # Mensaje de respuesta
        login_form = LoginForm(request.POST)                    # Crea objeto de login con los datos del formulario
        if login_form.is_valid():                               # Django recorre los campos del formulario y aplica a
                                                                # cada uno los validadores
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Autenticación del usuario del formulario

            if user is None:
                message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)                  # Cambiar el usuario autenticado en el sistema
                    return redirect(
                        request.GET.get('next', 'users_home'))   # Si existe el atributo next redirige a la página de
                                                                 # la que viene, en otro caso redirige a la raiz
                else:
                    message = "Cuenta de usuario inactiva"

        context = {'message': message, 'form': login_form}

        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        """
        Hace el logout de un usuario y redirige al inicio
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated():
            django_logout(request)

        return redirect('users_home')

# TODO: Validaciones sobre los campos
# TODO: El nombre del usuario ...
# TODO: Los apellidos del usuario ...
# TODO: El nombre de usuario no debe existir ya en el sistema
# TODO: El formato del email debe ser válido
# TODO: La contraseña debe tener...
# TODO: Comprobar si hay algún error en la creación del usuario
class SignUpView(View):
    def get(self, request):
        """
        Renderiza el formulario SignUpForm para dar de alta usuarios en el sistema
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = "Introduzca los datos del nuevo usuario"
        signup_form = SignUpForm()
        context = {'message': message, 'form': signup_form}

        return render(request, 'users/signup.html', context)


    def post(self, request):
        """
        Gestiona el alta de usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = ""                            # Mensaje de respuesta
        signup_form = SignUpForm(request.POST)  # Crea objeto de login con los datos del formulario
        if signup_form.is_valid():              # Django recorre los campos del formulario y aplica a
                                                # cada uno los validadores
            name = signup_form.cleaned_data.get('name')
            surname = signup_form.cleaned_data.get('surname')
            username = signup_form.cleaned_data.get('username')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')

            user = User.objects.create_user(first_name = name,
                                            last_name = surname,
                                            username = username,
                                            email = email,
                                            password = password)
        user.is_active = True       # El usuario está activo

        message = 'Usuario {0} creado con éxito'.format(username)
        user.save()     # Guardar nuevo usuario

        #if user.save():
        #    message = 'Usuario {0} creado con éxito'.format(username)
        #else:
        #    message = 'Ha ocurrido un problema al crear el usuario'

        context = {'message': message, 'form': signup_form}

        return render(request, 'users/login.html', context)