from msilib.schema import ListView
from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from products.models import SingleProduct, Category
# Create your views here.

class MainPageTemplateView(ListView):
    template_name = 'mainpage/index.html'
    model = Category
    context_object_name = 'categories'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = SingleProduct.latest_products.all()
        return context
    

