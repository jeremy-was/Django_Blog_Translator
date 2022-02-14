from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin): # JW Created to display more info on blog list screen
    list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin) # JW Created