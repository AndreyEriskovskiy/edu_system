from rest_framework import serializers
from .models import Product, Lesson, Group

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class ProductAvailableSerializer(serializers.ModelSerializer):
    
    lesson_count = serializers.SerializerMethodField()
    
    def get_lesson_count(self, obj):
        return Lesson.objects.filter(product=obj).count()
    class Meta:
        model = Product
        fields = ['id', 'name', 'datetime_started', 'price', 'min_users', 'max_users', 'author', 'lesson_count']
        

    