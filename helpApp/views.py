from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import get_object_or_404, redirect, render
from . forms import ProblemForm, SolutionsForm
from . models import PostProblem, Solution_to_problems
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    problems = PostProblem.objects.order_by('-date_posted')
    return render(request, 'home.html',{'problems': problems})
 

def solution(request):
    if request.method == 'POST': 
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            problems = problem_form.save(commit=False)
            problems.author = request.user
            problems.save()
            return redirect('home')
        else:
            messages.error(request, forms.error)
            return redirect('solution')
    else:
        problem_form = ProblemForm()
    return render(request, 'solution.html', {'problem_form': problem_form})

def delete_problem(request, pk):
    problem = get_object_or_404(PostProblem, pk=pk)
    problem.delete()
    return redirect('home')

def delete_solution(request, pk):
    solution = get_object_or_404(Solution_to_problems, pk=pk)
    solution.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        creation_form = UserCreationForm(request.POST)
        if creation_form.is_valid():
            form = creation_form.save()
            return redirect('login')
        else:
            messages.error(request, forms.error)
    else:
        creation_form = UserCreationForm()
    return render(request, 'registration/register.html', {'forms':creation_form})

def details(request, pk):
    problem = get_object_or_404(PostProblem, pk=pk)
    sol = Solution_to_problems.objects.filter(post_problem_id = pk)
    pk = pk
    if request.method == 'POST':
        solution_form = SolutionsForm(request.POST)
        if solution_form.is_valid():
            ex = solution_form.cleaned_data['short_note']
            co = solution_form.cleaned_data['correct_code']
            
            prob = problem

            Solution_to_problems.objects.create(
                short_note=ex,
                correct_code=co,
                solution_author=request.user,
                post_problem=prob

            )
            return redirect('details', pk=pk)
        else:
            messages.error(request, forms.error)
            return redirect('details')
    else:
        solution_form = SolutionsForm()
    return render(request, 'solutionDetails.html',{'problem':problem, 'solutionsForm':solution_form, 'solutions':sol})


def edit_solution(request, pk):
    solution = get_object_or_404(Solution_to_problems, pk=pk)
    id = solution.post_problem.id
    if request.method == 'POST':
        form = SolutionsForm(request.POST, instance=solution)
        if form.is_valid():
            form.save()
            #url = reverse('details/', kwargs={'key': pk })
            return redirect('details', pk=id)
        else:
            form = SolutionsForm(instance=solution)
    else:
        form = SolutionsForm(instance=solution)
    return render(request, 'solutionEdit.html',{'form':form, 'solution': solution})

def edit_problem(request, pk):
    problem = get_object_or_404(PostProblem, pk=pk)
    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            # url = reverse('details/', kwargs={'key': pk })
            return redirect('home')
        else:
            form = ProblemForm(instance=problem)
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'problemEdit.html',{'form':form, 'solution': problem})
