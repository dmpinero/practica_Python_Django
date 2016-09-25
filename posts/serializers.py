from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)


class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('title', 'url_image_or_video', 'head',  'published_at')
