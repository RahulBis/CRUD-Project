from django.contrib import admin
from . models import Signup
# Register your models here.
@admin.register(Signup)
class UserAdmin(admin.ModelAdmin):
    list_display =('id','username','first_name','last_name','email','password')