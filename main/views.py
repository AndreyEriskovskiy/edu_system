from django.shortcuts import render

from rest_framework import viewsets, generics


from .permissions import ProductAndLessonViewPermission, GroupViewPermission
from .serializers import ProductSerializer, LessonSerializer, GroupSerializer, ProductAvailableSerializer
from .models import Product, Lesson, Group
from datetime import datetime



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductAndLessonViewPermission]
    


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [GroupViewPermission]
    
   
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [ProductAndLessonViewPermission]
    

class ProductAvailableViewSet(generics.ListAPIView):
    queryset = Product.objects.filter(datetime_started__gte=datetime.now())
    serializer_class = ProductAvailableSerializer
    permission_classes = [ProductAndLessonViewPermission]
    
class LessonListViewSet(generics.RetrieveAPIView):
    
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [ProductAndLessonViewPermission]
    lookup_field = 'product_id'
    
        
    
    
    
