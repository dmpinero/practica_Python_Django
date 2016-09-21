from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    Clase que representa un blog en el sistema.
    Cada blog pertenece a un usuario.
    """
    name = models.CharField(max_length=50)                   # Nombre del blog
    description = models.TextField(null=True, blank=True)    # Descripción del blog
    created_at = models.DateTimeField(auto_now_add=True)     # Fecha de creación del Blog
    modified_at = models.DateTimeField(auto_now=True)        # Fecha de última modificación del blog
    owner = models.ForeignKey(User)                          # Clave ajena al usuario propietario del blog

    """
    Descripción de la entidad Post como cadena
    """
    def __str__(self):
        return self.name
