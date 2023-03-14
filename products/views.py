from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import SingleProduct, Category
# Create your views here.

class SingleProductPageDetailView(DetailView):
    template_name = 'products/single_product.html'
    context_object_name = 'product'
    model = SingleProduct   


class CategoryDetailView(DetailView):
    template_name = 'products/category_view.html'
    context_object_name = 'category'
    model = Category