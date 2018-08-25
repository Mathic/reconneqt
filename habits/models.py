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
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    motives = models.ManyToManyField('Motive')
    action_start = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    action_end = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.action_name

class Motive(models.Model):
    motive_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.motive_name

    class Meta:
        ordering = ('motive_name',)
