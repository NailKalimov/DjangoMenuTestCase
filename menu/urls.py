from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('news/', views.news, name='news'),
]
