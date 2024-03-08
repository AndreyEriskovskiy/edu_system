"""
URL configuration for edu_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, GroupViewSet, LessonViewSet, ProductAvailableViewSet, LessonListViewSet

product_router = routers.SimpleRouter()
product_router.register('products', ProductViewSet, basename='products')

group_router = routers.SimpleRouter()
group_router.register('groups', GroupViewSet, basename='groups')

lesson_router = routers.SimpleRouter()
lesson_router.register('lessons', LessonViewSet, basename='lessons')

app_name = 'main'



urlpatterns = [
    path('api/', include(product_router.urls)),
    path('api/', include(group_router.urls)),
    path('api/', include(lesson_router.urls)),
    path('api/available/', ProductAvailableViewSet.as_view()),
    path('api/lessonlist/<int:product_id>/', LessonListViewSet.as_view())
]