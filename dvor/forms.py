from django import forms
from .models import Techno, Calculation, PhoneCall


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

class BaseCalcForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = '__all__'

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        if not (email or phone):
            self.add_error('email','Должна быть заполнена почта или телефон')
            self.add_error('phone','Должна быть заполнена почта или телефон')
        return self.cleaned_data

class MainCalc (BaseCalcForm):
    class Meta:
        model = Calculation
        exclude = (
            'kit',
            'kit_numb',
            'created',
        )
        labels = {
            'fio': 'Ваше имя',
            'email': 'Ваш email',
            'phone': 'Ваш телефон',
            'note': 'Пожелания',
            'file': 'Прикрепить файл',
        }
        widgets = {
            'fio' : forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваше имя', 'class' : 'col-md-12 form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Пожалуйста, введите Ваш email адрес', 'class' : 'col-md-12 form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваш номер телефона', 'class' : 'col-md-12 form-control'}),
            'note': forms.Textarea(attrs={ 'class' : 'col-md-12 form-control'}),
            'file': forms.FileInput(attrs={'class': 'col-md-12 form-control'}),
        }

class PrjCalc (BaseCalcForm):
    class Meta:
        model = Calculation
        exclude = (
            'created',
        )
        labels = {
            'fio': 'Ваше имя',
            'email': 'Ваш email',
            'phone': 'Ваш телефон',
            'note': 'Сообщение',
        }
        widgets = {
            'fio' : forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваше имя', 'class' : 'col-md-12 form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Пожалуйста, введите Ваш email адрес', 'class' : 'col-md-12 form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваш номер телефона', 'class' : 'col-md-12 form-control'}),
            'note': forms.Textarea(attrs={ 'class' : 'col-md-12 form-control'}),
        }

class PhoneForm (forms.ModelForm):
    class Meta:
        model = PhoneCall
        exclude = (
            'created',
        )
        labels = {
            'fio': 'Ваше имя',
            'email': 'Ваш email',
            'phone': 'Ваш телефон',
            'wtime': 'Желаемое время звонка',
        }
        widgets = {
            'fio' : forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваше имя', 'class' : 'col-md-12 form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Пожалуйста, введите Ваш email адрес', 'class' : 'col-md-12 form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите Ваш номер телефона', 'class' : 'col-md-12 form-control'}),
            'wtime': forms.TextInput(attrs={'placeholder': 'Пожалуйста, введите желаемое время звонка', 'class' : 'col-md-12 form-control'}),
        }