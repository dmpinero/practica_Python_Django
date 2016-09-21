from django.db import models

class Category(models.Model):
    """
    Clase que representa una categoría en el sistema.
    """
    name = models.CharField(max_length=50)                  # Nombre de la categoría

    """
    Descripción de la entidad Categoría (Category) como cadena
    """
    def __str__(self):
        return self.name