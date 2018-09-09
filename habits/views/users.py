from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, HttpResponse, redirect

from ..models import Habit, Action, Motive
from forums.models import Thread, Post

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    try:
        user_id = int(request.user.id)
        habit_count = Habit.objects.filter(user_id=user_id).count()
        action_count = Action.objects.filter(user_id=user_id).count()
        motive_count = Motive.objects.filter(user_id=user_id).count()
        thread_count = Thread.objects.filter(user_id=user_id).count()
        post_count = Post.objects.filter(user_id=user_id).count()

        context = {
            'habit_count': habit_count,
            'action_count': action_count,
            'motive_count': motive_count,
            'thread_count':thread_count,
            'post_count': post_count,
        }
    except Habit.DoesNotExist:
        raise Http404("Habit does not exist")
    return render(request, 'habits/profile.html', context)
