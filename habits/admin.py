from django.contrib import admin

from .models import Habit, Action, Trigger

# Register your models here.
admin.site.register(Habit)
admin.site.register(Action)
admin.site.register(Trigger)
