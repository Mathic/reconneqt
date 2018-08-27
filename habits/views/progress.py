from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core import serializers

from django.shortcuts import render
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view, schema
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from ..forms import ProgressForm
from ..models import Habit, Action

@login_required
@csrf_protect
@api_view(['GET', 'POST'])
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
            action_list = Action.objects.filter(action_start__date=datetime.today()).order_by('action_start')
    except User.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        'habit_list': habit_list,
        'action_list': action_list,
    }
    return render(request, 'habits/progress.html', context)

class Progress(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user_id = int(request.user.id)
        action_list = Action.objects.filter(action_start__date=datetime.today()).order_by('action_start')
        occurence = {}
        num_motives = 0
        for a in action_list:
            for m in a.motives.all():
                num_motives += 1
                if m.motive_name in occurence:
                    occurence[m.motive_name] += 1
                else:
                    occurence[m.motive_name] = 1

        data = {
            'labels': occurence.keys(),
            'default': occurence.values(),
        }
        return Response(data)

    def post(self, request, format=None):
        user_id = int(request.user.id)
        data = request.POST
        date = datetime.strptime(data.get('date', False).replace('/', '-'), '%m-%d-%Y')
        action_list = Action.objects.filter(user_id=user_id).filter(action_start__date=date).order_by('action_start')
        occurence = {}
        num_motives = 0
        for a in action_list:
            for m in a.motives.all():
                num_motives += 1
                if m.motive_name in occurence:
                    occurence[m.motive_name] += 1
                else:
                    occurence[m.motive_name] = 1

        print("date: {} occurence: {}\n".format(date, occurence))
        data = {
            'labels': occurence.keys(),
            'default': occurence.values(),
            'action_list':  serializers.serialize('json', action_list),
        }
        return Response(data)
