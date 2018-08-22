from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from ..forms import MotiveForm
from ..models import Habit, Motive

@login_required
def motives(request):
    try:
        user_id = int(request.user.id)
        habit_list = Habit.objects.filter(user_id=user_id)
        motive_list = Motive.objects.filter(user_id=user_id)
        context = {
            'habit_list': habit_list,
            'motive_list': motive_list
        }
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'habits/motive_detail.html', context)

@login_required
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

@login_required
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
