from django.urls import path
from .views import ContactPageFormView
app_name = 'contacts'
urlpatterns = [
    path('', ContactPageFormView.as_view() , name='contact_page_form_view'),
    
]