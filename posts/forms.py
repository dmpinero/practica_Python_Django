from django import forms
from categories.models import Category


class PostForm(forms.Form):

    """
    Formulario para alta de post en el blog
    """
    title = forms.CharField(label="Título")
    head = forms.CharField(label="Cabecera")
    body = forms.Field(label="Cuerpo", widget=forms.Textarea)
    url_image_or_video = forms.URLField(label="URL de imagen o video")
    published_at = forms.DateField(label="Fecha y hora de publicación")
    categories = forms.ModelMultipleChoiceField(label="Categorías",
                                                queryset = Category.objects.all())