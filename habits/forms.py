from django import forms
from django.forms import inlineformset_factory
from django.forms.widgets import CheckboxSelectMultiple

from .models import Habit, Action, Trigger

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('habit_name', 'good_habit')


class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ('action_name', 'triggers')

    def __init__(self, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields['triggers'].widget = CheckboxSelectMultiple()
        self.fields['triggers'].queryset = Trigger.objects.all()

class TriggerForm(forms.ModelForm):

    class Meta:
        model = Trigger
        fields = ('trigger_name',)
