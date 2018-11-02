from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name="post_list"),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('post/new/', views.post_new, name='post_new'),
  path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
  path('post/remove/<int:pk>/', views.post_remove, name='post_remove'),
  path('post/comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
  path('post/comment/remove/<int:pk>/', views.remove_comment ,name='remove_comment'),
  path('post/like/<int:pk>/', views.like_post, name="like_post"),
  path('post/commentlike/<int:pk>', views.like_comment, name="like_comment"),
  ]

