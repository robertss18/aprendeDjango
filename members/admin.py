from django.contrib import admin
from django.contrib import admin
from .models import miModeloTable
# Register your models here.

admin.site.register(miModeloTable)


class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')