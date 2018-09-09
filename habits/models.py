from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    entry_title = models.CharField(max_length=100)
    entry = models.CharField(max_length=3000)
    entry_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    entry_edit_date = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.entry_title

class Mood(models.Model):
    mood_name = models.CharField(max_length=30)
    mood_weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mood_name

class MoodTracking(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    mood_start = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    mood_end = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

class Habit(models.Model):
    habit_name = models.CharField(max_length=30)
    good_habit = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_name

    class Meta:
        ordering = ('habit_name',)

class Action(models.Model):
    # action_name = models.CharField(max_length=100)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    entry = models.ForeignKey('JournalEntry', blank=True, null=True,  on_delete=models.CASCADE)
    motives = models.ManyToManyField('Motive')
    action_start = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    action_end = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)

class Motive(models.Model):
    motive_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.motive_name

    class Meta:
        ordering = ('motive_name',)
