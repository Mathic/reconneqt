from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.subject_name

class Thread(models.Model):
    title = models.CharField(max_length=100)
    thread_created = models.DateTimeField(auto_now_add=True)
    thread_edited = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_fk = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='threads')

    def __str__(self):
        return self.title

class Post(models.Model):
    content = models.CharField(max_length=1000)
    original = models.BooleanField(default=False)
    post_created = models.DateTimeField(auto_now_add=True)
    post_edited = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_fk = models.ForeignKey('Thread', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.content
