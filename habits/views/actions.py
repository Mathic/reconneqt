from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView

from ..forms import ActionForm
from ..models import Habit, Action

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
