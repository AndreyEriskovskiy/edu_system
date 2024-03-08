from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, Lesson, Group, User, UserType

admin.site.register(UserType)
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group)

class UserAdminModel(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'user_type')
    

admin.site.register(User, UserAdminModel)

# Register your models here.
