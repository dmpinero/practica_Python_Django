from rest_framework import serializers

class BlogSerializer(serializers.Serializer):

    # Campos a devolver en la respuesta
    username = serializers.CharField()
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        host = self.context['request'].META.get('HTTP_HOST')
        path_info = self.context['request'].META.get('PATH_INFO')

        return 'http://' + host + path_info + obj.username + '/'