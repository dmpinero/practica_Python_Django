from django.db import models

class File(models.Model):

    url = models.FileField(upload_to="uploads")
    name = models.CharField(max_length=100)
