from collections import UserString
from django.contrib.auth.forms import UsernameField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class PostProblem(models.Model):
    topic = models.CharField(max_length=200)
    describe_problem = models.CharField(max_length=200)
    code_to_debug = RichTextField(blank=True,null=True)
    #code_to_debug = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pk}{self.topic}"


class Solution_to_problems(models.Model):
    short_note = models.CharField(max_length=200)
    correct_code = RichTextField(blank=True,null=True)
    #correct_code = models.TextField()
    solution_author = models.CharField(max_length=200, null=True, blank=True)
    post_problem = models.ForeignKey(PostProblem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} {self.short_note}"