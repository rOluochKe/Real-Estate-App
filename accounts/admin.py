from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_staff')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', )
    list_per_page = 25

admin.site.register(UserAccount, UserAccountAdmin)