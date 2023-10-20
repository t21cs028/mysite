'''
Created on 2023/10/20

@author: t21cs028
'''
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]