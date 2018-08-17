from django.contrib import admin

from .models import Habit, Action, Motive

# Register your models here.
admin.site.register(Habit)
admin.site.register(Action)
admin.site.register(Motive)
