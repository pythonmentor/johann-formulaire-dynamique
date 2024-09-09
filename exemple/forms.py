from django import forms 
from django.urls import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field

from . import models

class BrandFormLayout(Layout):
    def __init__(self):
        super().__init__(
            Row(
                Column('name', css_class="flex-1"),
                Column(
                    'supplier', 
                    css_class="flex-1", 
                    hx_get=reverse('hx-get-country'), 
                    hx_trigger="change", 
                    hx_target="#id_country", 
                    hx_swap="outerHTML",
                    hx_include="#id_supplier",
                ),
                Column(
                    Field('country', disabled="disabled", css_class="bg-gray-100"),
                    css_class="flex-1"
                ),
                css_class='flex space-x-2 w-full'
            ),
            Submit("submit", 'Enregistrer', css_class="bg-amber-600 text-white hover:bg-amber-500")
        )

class BrandForm(forms.ModelForm):
    country = forms.CharField(label="pays", required=False)

    class Meta:
        model = models.Brand
        fields = ("name", "supplier")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = BrandFormLayout()