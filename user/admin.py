from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'phone')
    list_filter = ('address',)

# Register your models here.
admin.site.register(Profile, ProfileAdmin)