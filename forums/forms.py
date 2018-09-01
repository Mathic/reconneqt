from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import Subject, Thread, Post

class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title',)

class NewThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'subject_fk')

    def __init__(self, *args, **kwargs):
        super(NewThreadForm, self).__init__(*args, **kwargs)
        self.fields['subject_fk'].label = "Subject"

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'style': 'width: 100%'})
        }
