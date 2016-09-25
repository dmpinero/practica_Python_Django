from rest_framework import serializers


class BlogSerializer(serializers.Serializer):

    # Campos a devolver en la respuesta
    # TODO. Falta por devolver la URL de cada blog
    name = serializers.CharField()
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return "http://url.com"