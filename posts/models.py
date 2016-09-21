from django.contrib.auth.models import User
from django.db import models
from categories.models import Category

from blogs.models import Blog

class Post(models.Model):
    """
    Clase que representa un post en el sistema.
    """
    title = models.CharField(max_length=50)                  # Título del post
    head = models.CharField(max_length=150)                  # Texto a modo de introducción
    body = models.TextField()                                # Cuerpo del post
    url_image_or_video = models.URLField(null=True,
                                        blank=True)          # URL de imagen o vídeo destacado (opcional)
    published_at = models.DateTimeField()                    # Fecha y hora de publicación del post
    created_at = models.DateTimeField(auto_now_add=True)     # Fecha y hora de creación del post
    modified_at = models.DateTimeField(auto_now=True)        # Fecha y hora de última modificación del post
    categories = models.ManyToManyField(Category)            # Categorías en las que se publican (un post puede
                                                             # publicarse en una o varias categorías)
    owner = models.ForeignKey(User)                          # Clave ajena al usuario propietario del blog

    """
    Descripción de la entidad Post como cadena
    """
    def __str__(self):
        return self.title