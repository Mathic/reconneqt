from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Habit(models.Model):
    habit_name = models.CharField(max_length=30)
    good_habit = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_name

    class Meta:
        ordering = ('habit_name',)

class Action(models.Model):
    action_name = models.CharField(max_length=100)
    habit_action = models.ForeignKey('Habit', on_delete=models.CASCADE)
    action_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.action_name

class Trigger(models.Model):
    trigger_name = models.CharField(max_length=100)
    actions = models.ManyToManyField('Action')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.trigger_name

    class Meta:
        ordering = ('trigger_name',)
