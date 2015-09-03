from django import forms

from DetectoresMetales.BBDD.models import Expedientes
from DetectoresMetales.BBDD.models import Solicitantes


class ExpedientesForm(forms.ModelForm):

    class Meta:
        model = Expedientes
        fields = '__all__'


class SolicitantesForm(forms.ModelForm):

    class Meta:
        model = Solicitantes
        fields = '__all__'
