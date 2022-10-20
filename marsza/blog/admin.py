from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
   list_display = ["title", "category", "author", "created", "modified"]
   list_filter = ["author", "category"]
   search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ["name"]
   list_filter = ["name"]
   search_fields = ["name"]

admin.site.register(Category, CategoryAdmin)

class ProfileAdmin(admin.ModelAdmin):
   list_display = ["user"]
   list_filter = ["user"]
   search_fields = ["user"]

admin.site.register(Profile, ProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
   list_display = ["post", "author", "created", "modified"]
   list_filter = ["author"]
   search_fields = ["post"]

admin.site.register(Comment, CommentAdmin)


