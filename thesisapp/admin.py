from django.contrib import admin
from .models import Thesis, Author, Panelist, Adviser, Comment

# Register your models here.

admin.site.register([Author, Panelist, Adviser])


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    filter_horizontal = ["authors", "panelists"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']