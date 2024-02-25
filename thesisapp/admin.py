from django.contrib import admin
from .models import Thesis, Author, Panelist, Adviser

# Register your models here.

admin.site.register([Author, Panelist, Adviser])


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    filter_horizontal = ["authors", "panelists"]
