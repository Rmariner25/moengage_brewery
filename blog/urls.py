from django.urls import path
from .views import (
    UserPostListView
)
from . import views

urlpatterns = [
    path('', views.br, name='blog-home'),
    path('brewfind', views.br, name='brewfind'),
    path('brewery/<str:id>', views.brewery, name='brewery'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('search/',views.search,name='search' ),
]
