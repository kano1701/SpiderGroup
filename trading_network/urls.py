from django.urls import path
from .views import *


urlpatterns = [
    path('companies/create', CompanyCreateView.as_view()),
    path('companies/all', CompanyListView.as_view()),
    path('companies/detail/<int:pk>/', CompanyDetailView.as_view()),
    path('products/create', ProductCreateView.as_view()),
    path('products/all', ProductListView.as_view()),
    path('products/detail/<int:pk>/', ProductDetailView.as_view()),
]