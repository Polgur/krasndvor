from django import forms

tech_choices = (
    (1, 'Термопанели'),
    (2, 'СИП панели'),
    (3, 'Каркасные'),
)
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
    tech = forms.ChoiceField(choices = tech_choices, label='Технология', widget=forms.Select(), required=True)
    vid  = forms.ChoiceField(choices = vid_choices, label='Тип', widget=forms.Select(), required=True)
    search = forms.CharField(widget = forms.HiddenInput(), required = False, initial = 1)