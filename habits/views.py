from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse

from .models import Habit, Trigger

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
        trigger_list = Trigger.objects.filter(user_id=user_id)
        context = {
            'habit_list': habit_list,
            'trigger_list': trigger_list
        }
    except User.DoesNotExist:
        return render(request, 'habits/habits.html')
    return render(request, 'habits/habits.html', context)

def detail(request, habit_id):
    try:
        user_id = int(request.user.id)
        habit = Habit.objects.get(pk=habit_id)
        trigger_list = Trigger.objects.filter(user_id=user_id)
        habit_triggers = []
        for trigger in trigger_list:
            for h in trigger.habits.all():
                if h.id == habit_id:
                    habit_triggers.append(trigger)

        context = {
            'habit_id': habit_id,
            'habit': habit,
            'habit_triggers': habit_triggers
        }
    except Habit.DoesNotExist:
        raise Http404("Habit does not exist")
    return render(request, 'habits/habit_detail.html', context)
