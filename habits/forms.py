from django import forms
from django.forms import inlineformset_factory
from django.forms.widgets import CheckboxSelectMultiple

from .models import Habit, Action, Motive

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('habit_name', 'good_habit')

class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ('motives', 'action_start', 'action_end')

        widgets = {
            'action_start': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'action_end': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

    def __init__(self, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields['motives'].widget = CheckboxSelectMultiple()
        self.fields['motives'].queryset = Motive.objects.all()

class MotiveForm(forms.ModelForm):

    class Meta:
        model = Motive
        fields = ('motive_name',)

class ProgressForm(forms.Form):
    date = forms.DateField()
