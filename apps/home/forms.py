from django import forms

from .models import Logo
from django_svg_image_form_field import SvgAndImageFormField


class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        exclude = []
        field_classes = {
            'logo_actual': SvgAndImageFormField,
        }
