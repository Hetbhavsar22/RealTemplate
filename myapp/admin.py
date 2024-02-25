from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','comment']

@admin.register(register)
class registerAdmin(admin.ModelAdmin):
    list_display = ['Name', 'email', 'pwd', 'cpwd']