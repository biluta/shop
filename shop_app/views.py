from django.shortcuts import render

# Create your views here.

# импортируем модель для CBV
from django.views import generic

# импортируем нашу модель
from .models import Product
from .models import Category


class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    # добавляем объекты модели в контекст под этим именем
    context_object_name = 'products'
    model = Product

# метод для добавления дополнительной информации в контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product


class AllListView(generic.ListView):
    template_name = 'home.html'
    # добавляем объекты модели в контекст под этим именем
    context_object_name = 'category'
    model = Category
# метод для добавления дополнительной информации в контекст

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context

class CategoryDetail(generic.DetailView):
    template_name = 'category_list.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context