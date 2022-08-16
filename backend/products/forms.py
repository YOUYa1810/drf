from socket import fromshare
from django import forms
from .models import Product

class ProducForm(form.class MODELNAMEForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = MODELNAME
        fields = ('',)
):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]
