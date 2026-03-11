# inventory/forms.py

from django import forms
from .models import InventoryItem, Category


class InventoryItemForm(forms.ModelForm):

    class Meta:
        model  = InventoryItem
        fields = [
            'name',
            'sku',
            'category',
            'quantity',
            'unit_price',
            'description',
            'is_active',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'e.g. Wireless Mouse',
            }),
            'sku': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'e.g. WM-001',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min':   0,
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min':   0,
                'step':  '0.01',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows':  3,
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    def clean_sku(self):
        sku = self.cleaned_data['sku'].upper().strip()
        return sku

    def clean_unit_price(self):
        price = self.cleaned_data['unit_price']
        if price <= 0:
            raise forms.ValidationError(
                "Price must be greater than zero."
            )
        return price