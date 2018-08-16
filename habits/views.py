from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView

from .forms import HabitForm, ActionForm
from .models import Habit, Action, Trigger

# Create your views here.
def reconneqt(request):
    return render(request, 'habits/cover.html')

def index(request):
    return render(request, 'habits/index.html')

def login(request):
    return render(request, 'habits/login.html')

def habits(request):
    try:
        user_id = int(request.user.id)
        habit_list = Habit.objects.filter(user_id=user_id)
        action_list = Action.objects.filter(user_id=user_id)
        trigger_list = Trigger.objects.filter(user_id=user_id)
        context = {
            'habit_list': habit_list,
            'action_list': action_list,
            'trigger_list': trigger_list
        }
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
            return redirect('habit_detail', pk=habit.pk)
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
        user_id = int(request.user.id)
        habit = Habit.objects.get(pk=habit_id)
        action_list = Action.objects.filter(habit_action=habit_id)
        trigger_list = Trigger.objects.filter(user_id=user_id)

        context = {
            'habit_id': habit_id,
            'habit': habit,
            'action_list': action_list,
            'trigger_list': trigger_list
        }
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
