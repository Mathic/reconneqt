from django.contrib import admin

from .models import Habit, Trigger

# Register your models here.
admin.site.register(Habit)
admin.site.register(Trigger)
