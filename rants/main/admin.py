from django.contrib import admin
from .models import Rant, Category


class RantAdmin(admin.ModelAdmin):
    prepopulated_fields = ({'slug': 'title'})

admin.site.register(Rant)
admin.site.register(Category)
