from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Habit(models.Model):
    habit_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_name

    class Meta:
        ordering = ('habit_name',)

class Trigger(models.Model):
    trigger_name = models.CharField(max_length=100)
    habits = models.ManyToManyField('Habit')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.trigger_name

    class Meta:
        ordering = ('trigger_name',)
