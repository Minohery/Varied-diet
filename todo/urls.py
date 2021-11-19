from django.urls import path, include
from . import views

app_name='todo'

urlpatterns=[
    path('add/<int:break_bool>/<int:number>/', views.add, name="add"),
    path('liste/<int:break_bool>/', views.liste, name="liste"),
    path('delete/<int:num>/<int:break_bool>/', views.delete, name="delete"),
    path('draw/', views.draw, name="draw"),
]
