from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from .forms import ContactPageForm
from .models import ContactPage

# Create your views here.

class ContactPageFormView(FormView):
    template_name = 'contacts/contact_page.html'
    form_class = ContactPageForm
    success_url = reverse_lazy('contacts:contact_page_form_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['contacts'] = ContactPage.objects.get(pk=1)


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
