
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.starting_page, name= 'startig-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page')
    
]