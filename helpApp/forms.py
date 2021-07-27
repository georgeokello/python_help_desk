
from django import forms
from django.forms import fields
from django.forms.models import ModelForm

from . models import PostProblem, Solution_to_problems


class ProblemForm(ModelForm):
    class Meta:
        model = PostProblem
        fields = ['topic','describe_problem','code_to_debug']

class SolutionsForm(ModelForm):
    class Meta:
        model = Solution_to_problems
        fields = ['short_note','correct_code']