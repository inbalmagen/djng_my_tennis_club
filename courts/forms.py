# courts/forms.py
from django import forms
from .models import CourtOrder, Court
from members.models import Member

class CourtOrderForm(forms.ModelForm):
    court = forms.ModelChoiceField(queryset=Court.objects.filter(is_occupied=False))
    member1 = forms.ModelChoiceField(queryset=Member.objects.all())
    member2 = forms.ModelChoiceField(queryset=Member.objects.all())

    class Meta:
        model = CourtOrder
        fields = ['court', 'member1', 'member2']
