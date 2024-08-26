from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('image/<int:pk>/', views.image_details, name='image_details'),
    path('post/new/', views.post_image, name='post_image'),
]