# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the solve climate index.")

    from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Team
from .forms import ProfileForm, ProblemProposalForm, SolutionForm

@login_required
def dashboard(request):
    profile = request.user.profile
    if profile.team:
        return redirect('team_dashboard')
    return redirect('create_team')

@login_required
def edit_profile(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return HttpResponse(request, 'edit_profile.html', {'form': form})

@login_required
def create_team(request):
    # Randomized team creation logic for now
    team, created = Team.objects.get_or_create(name="Random Team")
    team.members.add(request.user)
    profile = request.user.profile
    profile.team = team
    profile.save()
    return redirect('team_dashboard')

@login_required
def team_dashboard(request):
    return HttpResponse(request, 'team_dashboard.html')

@login_required
def submit_solution(request):
    form = SolutionForm()
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.save()
            return redirect('team_dashboard')
    return HttpResponse(request, 'submit_solution.html', {'form': form})

