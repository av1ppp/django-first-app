"""Конфигурация URL проекта

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),

    path('books/<str:name>', views.books),
    
    re_path(r'^about/$', views.about),
    re_path(r'^about/contact/', views.contact),
    
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productId>\d+)', views.products),
    
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    
    path('admin/', admin.site.urls),
]
