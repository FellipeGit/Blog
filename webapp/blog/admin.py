from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_date', 'updated_date', 'status')
    list_filter = ('author', 'slug', 'created_date', 'updated_date', 'status')
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': 'title'}

admin.site.register(Post, PostAdmin)
