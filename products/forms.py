
from django import forms

from django.core.exceptions import ValidationError
from .models import SingleProduct, ProductImage


class ProductForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = SingleProduct
        fields = '__all__'

    def clean(self):
        super().clean()
        errors = {}

        if self.cleaned_data.get('initial_price') < 0:
            # errors['initial_price'] = ValidationError('Цена не может быть меньше нуля')
            self.add_error('initial_price', ValidationError('Price should be more than 0'))
        # if errors:
        #     raise ValidationError(errors)
    
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'