from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import StatusChoice


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Заголовок")
    description = forms.CharField(max_length=50, required=True, label="Описание")
    details = forms.CharField(max_length=3000, label="Подробное описание",
                              widget=widgets.Textarea)

    deadline = forms.DateField(widget=DateInput, label="Выполнить до")
    status = forms.ChoiceField(choices=StatusChoice.choices, label="Статус")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError('Заголовок должен быть длиннее 3 символов!')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 3:
            raise ValidationError('Описание должно быть длиннее 3 символов!')
        return description
