from django.contrib import admin
from .models import miModeloTable

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("nombre", "apellido", "joined_date",)
  
admin.site.register(miModeloTable, MemberAdmin)