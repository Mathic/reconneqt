from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(JournalEntry)

admin.site.register(Mood)
admin.site.register(MoodTracking)

admin.site.register(Habit)
admin.site.register(Action)
admin.site.register(Motive)
