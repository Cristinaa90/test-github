from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ['title', 'created_date', 'published_date']


admin.site.register(Post, PostAdmin)

