from django.urls import path
from . import views


urlpatterns = [
    path('', views.drill, name='xword-drill'),
    path('answer/<pk>/', views.answer, name='xword-answer')
]