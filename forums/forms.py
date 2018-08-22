from django import forms

from django.forms.widgets import CheckboxSelectMultiple

from .models import Subject, Thread, Post

class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content',)
