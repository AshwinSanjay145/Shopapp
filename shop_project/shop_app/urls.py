
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('item/<int:pro_id>/',views.detail,name="item"),
    path('update/<int:pro_id>/',views.update,name='update'),
    path('delete/<int:pro_id>/',views.delete,name='delete'),
]
