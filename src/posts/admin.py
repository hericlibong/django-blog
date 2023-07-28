from django.contrib import admin
from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published','slug', 'created_on', 'last_updated',)
    list_editable = ('published',)

admin.site.register(BlogPost, BlogPostAdmin)
