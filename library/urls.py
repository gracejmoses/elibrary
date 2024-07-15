from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome page'),
    path('books/', views.books, name='Books'),
    path('users/',views.users, name='users'),
    path('students/', views.students, name='students'),
]