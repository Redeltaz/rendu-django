from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = "__all__"

        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'placeholder': 'Price'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Quantity'}),
        }