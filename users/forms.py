from django import forms

class LoginForm(forms.Form):

    """
    Formulario para autenticar usuarios en el sistema
    """
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    """
    Formulario para dar de alta usuarios en el sistema
    """
    name = forms.CharField(label="Nombre del usuario")
    surname = forms.CharField(label="Apellidos del usuario")
    username = forms.CharField(label="Nombre de usuario")
    email = forms.CharField(label="Correo electrónico del usuario", widget=forms.EmailInput())
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())