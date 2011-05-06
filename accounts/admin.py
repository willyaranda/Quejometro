# coding=utf-8
from accounts.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("user",)}
    
    
admin.site.register(UserProfile, UserProfileAdmin)