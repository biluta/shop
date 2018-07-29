from django.shortcuts import render

# Create your views here.

# импортируем модель для CBV
from django.views import generic

# импортируем нашу модель
from .models import Product
from .models import Category
from .models import Order
from .models import User

# Вью для авторизации
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Подключаем миксины для верификации пользователя
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .form import SignUpForm


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


class OrderFormView(LoginRequiredMixin, generic.CreateView):
	model = Order
	template_name = 'order_form.html'
	success_url = '/'
	# выведем только поля, которые нужно заполнить самому человеку
	fields = ['customer_name', 'customer_phone', 'customer_email']

	def form_valid(self, form):
		product = Product.objects.get(id=self.kwargs['pk'])
		user = self.request.user
		form.instance.user = user
		form.instance.product = product
		form.instance.order.customer_name = user.username
		return super().form_valid(form)

	def get_initial(self):
		first_name = self.request.user.first_name
		email = self.request.user.email
		return {"customer_name": first_name, "customer_email": email}


class SignUpView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'signup.html'
	success_url = reverse_lazy('login')


# наш секретный Вью
class SecretAdminView(UserPassesTestMixin, generic.TemplateView):
	# секретное содержимое
	template_name = 'admins.html'
	# проверяем условие, если пользователь — админ, то вернет True и пустит пользователя

	def test_func(self):
		return self.request.user.is_superuser
