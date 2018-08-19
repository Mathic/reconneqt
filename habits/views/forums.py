from django.shortcuts import render

def forum(request):
    return render(request, 'habits/forums.html')
