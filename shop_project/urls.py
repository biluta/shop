"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# стандартный вью для админки
from django.contrib import admin
# модуль Джанго для определения URL'ов
from django.urls import path 
# импортируем наш файл views из shop_app
from shop_app import views 

from django.conf.urls import include

urlpatterns = [ 
  path('', views.AllListView.as_view(), name='index'), 
  path('admin/', admin.site.urls), 
  path('product/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
  path('category/<int:pk>/', views.CategoryDetail.as_view(), name='categories'),
  path('product/<int:pk>/order', views.OrderFormView.as_view(), name='product_order'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.SignUpView.as_view(), name='sign_up'),
  path('kek/', views.SecretAdminView.as_view()),
]