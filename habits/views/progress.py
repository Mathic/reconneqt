from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_protect

from ..forms import ProgressForm
from ..models import Habit, Action

@login_required
@csrf_protect
def progress(request):
    try:
        user_id = int(request.user.id)
        habit_list = Habit.objects.filter(user_id=user_id)
        if request.method == "POST":
            form = ProgressForm(request.POST)
            if form.is_valid():
                date = form.cleaned_data.get('date')
                action_list = Action.objects.filter(user_id=user_id).filter(action_start__date=date).order_by('action_start')
        else:
            form = ProgressForm()
            print(datetime.today())
            action_list = Action.objects.filter(action_start__date=datetime.today())
    except User.DoesNotExist:
        raise Http404("User does not exist")

    print(action_list)
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
        'habit_list': habit_list,
        'action_list': action_list,
        'num_motives': num_motives,
        'occurence': occurence
    }
    return render(request, 'habits/progress.html', context)
