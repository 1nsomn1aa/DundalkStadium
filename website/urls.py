from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('events/', views.events, name='events'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('news/<int:post_id>/', views.news, name='news'),
]