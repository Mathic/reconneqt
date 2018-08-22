from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from .forms import ThreadForm, PostForm
from .models import Subject, Thread, Post

# Create your views here.
def forum(request):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        context = {
            'parents': parents,
            'children': children
        }
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    return render(request, 'forums/forums.html', context)

def threads(request, subject):
    try:
        threads = Thread.objects.filter(subject_fk__id=subject)
        # posts = Post.objects.filter(thread_fk=threads)

        context = {
            'threads': threads
        }
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'forums/thread.html', context)

def thread_detail(request, pk):
    try:
        thread = Thread.objects.get(pk=pk)
        posts = Post.objects.filter(thread_fk=thread)

        context = {
            'thread': thread,
            'posts': posts
        }
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'forums/thread.html', context)
