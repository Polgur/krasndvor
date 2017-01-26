from django import forms
from .models import Techno


vid_choices = (
    (0, 'Любые'),
    (1, 'Коттедж'),
    (2, 'Дуплекс'),
    (3, 'Баня'),
)


class ProjectFilterForm (forms.Form):
    pmin = forms.IntegerField(label='Цена от',required=True)
    pmax = forms.IntegerField(label='до',required=True)
    smin = forms.IntegerField(label='Площадь от',required=True)
    smax = forms.IntegerField(label='до',required=True)
    tech = forms.ModelChoiceField(queryset = Techno.objects.filter(main=True),label = 'Технология',empty_label=None,required=False)
    vid  = forms.ChoiceField(choices = vid_choices, label='Тип', required=True)
    search = forms.CharField(widget = forms.HiddenInput(), required = False, initial = 1)