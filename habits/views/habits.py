from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from ..forms import HabitForm
from ..models import Habit, Action

# Create your views here.
def index(request):
    return render(request, 'habits/index.html')

@login_required
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

@login_required
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
    success_url = reverse_lazy('progress')

@login_required
def habit_detail(request, habit_id):
    try:
        user_id = int(request.user.id)
        habit_list = Habit.objects.filter(user_id=user_id)
        habit = Habit.objects.get(pk=habit_id)
        action_list = Action.objects.filter(user_id=user_id).filter(habit=habit_id).order_by('-action_start')

        paginator = Paginator(action_list, 8) # Show 8 actions per page
        page = request.GET.get('page')
        actions = paginator.get_page(page)

        occurence = {}
        num_motives = 0
        for a in action_list:
            for m in a.motives.all():
                num_motives += 1
                if m in occurence:
                    occurence[m] += 1
                else:
                    occurence[m] = 1

        context = {
            'habit': habit,
            'habit_list': habit_list,
            'num_motives': num_motives,
            'occurence': occurence,
            'actions': actions,
            'paginator': paginator,
        }
    except Habit.DoesNotExist:
        raise Http404("Habit does not exist")
    except PageNotAnInteger:
        actions = paginator.page(1)
    except EmptyPage:
        actions = paginator.page(paginator.num_pages)
    return render(request, 'habits/habit_detail.html', context)

def error_404(request):
    data = {}
    return render(request, 'habits/error_404.html', data)

def error_500(request):
    data = {}
    return render(request, 'habits/error_500.html', data)

def journal(request):
    try:
        user_id = int(request.user.id)
        habit_list = Habit.objects.filter(user_id=user_id)

        context = {
            'habit_list': habit_list,
        }
    except Habit.DoesNotExist:
        raise Http404("Habit does not exist")
    return render(request, 'habits/journal.html', context)
