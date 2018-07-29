# Импортируется родительский класс моделей
from django.db import models
from django.contrib.auth.models import User

# Создаем базовую модель нашего продукта


class Product(models.Model):
    title = models.CharField(max_length=200)  # и указываем максимальную длину
    description = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name="products") 

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title

class Order(models.Model): 
    product = models.ForeignKey(Product, on_delete='CASCADE') 
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    User = models.ForeignKey(User,on_delete='CASCADE',null=True)

    def __str__(self):
        return self.customer_name+" тел.:"+self.customer_phone



