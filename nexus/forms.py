from django import forms
from .models import Nux

class NuxForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            'placeholder':'Enter your Nex',
            'class':'form-control',
        }
    ), label='')

    class Meta:
        model = Nux
        exclude = ('user',)