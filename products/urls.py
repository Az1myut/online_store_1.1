from django.urls import path
from .views import (
    SingleProductPageDetailView,
    CategoryDetailView
)
app_name = 'products'

urlpatterns = [
    path('single_product/<int:pk>', SingleProductPageDetailView.as_view(), name='show_single_product_page'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_view'),
    
]