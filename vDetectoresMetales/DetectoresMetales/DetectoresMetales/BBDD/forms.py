from django import forms

from DetectoresMetales.BBDD.models import Expedientes


class ExpedientesForm(forms.ModelForm):

    class Meta:
        model = Expedientes
        fields = '__all__'
