from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView

from .forms import HabitForm, ActionForm, MotiveForm
from .models import Habit, Action, Motive

# Create your views here.
def reconneqt(request):
    return render(request, 'habits/cover.html')

def forum(request):
    return render(request, 'habits/forums.html')

def index(request):
    return render(request, 'habits/index.html')

def login(request):
    return render(request, 'habits/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'habits/signup.html', {'form': form})

def habits(request):
    try:
        if request.user.is_authenticated:
            user_id = int(request.user.id)
            habit_list = Habit.objects.filter(user_id=user_id)
            action_list = Action.objects.filter(user_id=user_id)
            motive_list = Motive.objects.filter(user_id=user_id)
            context = {
                'habit_list': habit_list,
                'action_list': action_list,
                'motive_list': motive_list
            }
        else:
            context = {}
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'habits/habits.html', context)

def habit_new(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_detail', habit_id=habit.pk)
    else:
        form = HabitForm()
        return render(request, 'habits/habit_edit.html', {'form': form})

def habit_edit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_detail', habit_id=habit_id)
    else:
        form = HabitForm(instance=habit)
    context = {
        'form': form,
        'habit': habit
    }
    return render(request, 'habits/habit_edit.html', context)

class HabitDelete(DeleteView):
    model = Habit
    success_url = reverse_lazy('habits')

def habit_detail(request, habit_id):
    try:
        if request.user.is_authenticated:
            user_id = int(request.user.id)
            habit_list = Habit.objects.filter(user_id=user_id)
            habit = Habit.objects.get(pk=habit_id)
            action_list = Action.objects.filter(user_id=user_id).filter(habit_action=habit_id).order_by('-action_time')
            motive_list = Motive.objects.filter(user_id=user_id)
            context = {
                'habit_id': habit_id,
                'habit': habit,
                'habit_list': habit_list,
                'action_list': action_list,
                'motive_list': motive_list
            }
        else:
            context = {}
    except Habit.DoesNotExist:
        raise Http404("Habit does not exist")
    return render(request, 'habits/habit_detail.html', context)

def action_new(request, habit_id):
    habit = Habit.objects.get(pk=habit_id)
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.habit_action = habit
            action.action_time = timezone.now()
            action.user = request.user
            action.save()
            form.save_m2m()
            return redirect('habit_detail', habit_id=habit_id)
    else:
        form = ActionForm()
    context = {
        'form': form,
        'habit': habit
    }
    return render(request, 'habits/action_edit.html', context)

def action_edit(request, habit_id, pk):
    action = get_object_or_404(Action, pk=pk)
    habit = Habit.objects.get(pk=habit_id)
    if request.method == "POST":
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            action = form.save(commit=False)
            action.habit_action = habit
            action.action_time = timezone.now()
            action.user = request.user
            action.save()
            form.save_m2m()
            return redirect('habit_detail', habit_id=habit_id)
    else:
        form = ActionForm(instance=action)

    context = {
        'form': form,
        'habit': habit,
        'action': action
    }
    return render(request, 'habits/action_edit.html', context)

class ActionDelete(DeleteView):
    model = Action
    success_url = reverse_lazy('habits')

def motives(request):
    try:
        if request.user.is_authenticated:
            user_id = int(request.user.id)
            motive_list = Motive.objects.filter(user_id=user_id)
            context = {
                'motive_list': motive_list
            }
        else:
            context = {}
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'habits/motive_detail.html', context)

def motive_new(request):
    if request.method == "POST":
        form = MotiveForm(request.POST)
        if form.is_valid():
            motive = form.save(commit=False)
            motive.user = request.user
            motive.save()
            return redirect('motives')
    else:
        form = MotiveForm()
        return render(request, 'habits/motive_edit.html', {'form': form})

def motive_edit(request, pk):
    motive = get_object_or_404(Motive, pk=pk)
    if request.method == "POST":
        form = MotiveForm(request.POST, instance=habit)
        if form.is_valid():
            motive = form.save(commit=False)
            motive.user = request.user
            motive.save()
            return redirect('motives')
    else:
        form = MotiveForm(instance=motive)
    context = {
        'form': form,
        'motive': motive
    }
    return render(request, 'habits/motive_edit.html', context)

class MotiveDelete(DeleteView):
    model = Motive
    success_url = reverse_lazy('motives')

def error_404(request):
    data = {}
    return render(request, 'habits/error_404.html', data)

def error_500(request):
    data = {}
    return render(request, 'habits/error_500.html', data)
