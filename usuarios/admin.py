from usuarios.models import Usuario
from django.contrib import admin

class UsuarioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nick",)}
    
    
admin.site.register(Usuario, UsuarioAdmin)