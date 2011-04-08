# coding=utf-8
from claims.models import Claim
from django.contrib import admin

class ClaimAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    
admin.site.register(Claim, ClaimAdmin)