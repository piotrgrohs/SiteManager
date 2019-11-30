
from django.urls import path
from .views import HomePageView, AboutPageView, file_detail

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('file/<int:pk>/', file_detail, name='file'),
    path('', HomePageView.as_view(), name='home')
]