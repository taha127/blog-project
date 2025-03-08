from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list_view, name='posts_list'),
]