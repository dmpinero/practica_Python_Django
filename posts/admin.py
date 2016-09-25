from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ('categories', )
    list_display = ('title', 'url_image_or_video', 'head', 'published_at')

    # Detalle de un post
    fieldsets = (
        (None, {
            'fields': ('title', 'url_image_or_video', 'head', 'published_at', 'categories', 'owner'),
            'classes': ('wide'),
        }),
    )

admin.site.register(Post, PostAdmin)
