from django.db import models

from django.contrib.auth.models import AbstractUser 


class UserType(models.Model):
    type = models.CharField(max_length=255, unique=True, null=True, blank=True)
    
    class Meta:
        db_table = 'UserType'
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователей'
        
    def __str__(self) -> str:
        return self.type
    
class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    datetime_started = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'Product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
    def __str__(self) -> str:
        return self.name
        
class Lesson(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)
    
    class Meta:
        db_table = 'Lesson'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        
    def __str__(self) -> str:
        return self.title
    
class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, related_name='group_users')
    
    class Meta:
        db_table = 'Group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        
    def __str__(self) -> str:
        return self.title

