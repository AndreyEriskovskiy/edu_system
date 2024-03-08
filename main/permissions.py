from django.http import HttpRequest
from rest_framework import permissions

from .models import Group, Product, Lesson, User


class ProductAndLessonViewPermission(permissions.BasePermission):

    def has_permission(self, request: HttpRequest, view):

        if request.user.is_authenticated:
            user = User.objects.select_related("user_type").get(id=request.user.id)

            if user.user_type.type == "Преподаватель":
                return True
            if request.method in permissions.SAFE_METHODS:
                return True

        return False

    def has_object_permission(self, request: HttpRequest, view, obj):

        def check_group_access(user, author):
            groups = Group.objects.filter(product=author)
            if groups.exists():
                for group in groups:
                    if user in group.users.all():
                        return True
            return False

        if isinstance(obj, Product):
            if check_group_access(request.user, obj):
                if request.method in permissions.SAFE_METHODS:
                    return True
                else:
                    return request.user == obj.author
            else:
                return request.user == obj.author

        elif isinstance(obj, Lesson):
            if check_group_access(request.user, obj.product):
                if request.method in permissions.SAFE_METHODS:
                    return True
                else:
                    return request.user == obj.product.author
            else:
                return request.user == obj.product.author
            

class GroupViewPermission(permissions.BasePermission):
    
    def has_permission(self, request: HttpRequest, view):
        if request.user.is_authenticated:
            if request.user.is_staff or request.user.is_superuser:
                return True
            return request.method in permissions.SAFE_METHODS
