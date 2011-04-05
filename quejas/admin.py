from quejas.models import Queja
from django.contrib import admin

class QuejaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    
    
admin.site.register(Queja, QuejaAdmin)