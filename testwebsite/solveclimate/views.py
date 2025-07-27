from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import SolutionForm
from .models import Team


@login_required
def dashboard(request):
    profile = request.user.profile
    if profile.team:
        return JsonResponse({'message': 'Redirecting to team dashboard'})
    return JsonResponse({'message': 'Redirecting to create team'})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Profile updated successfully'})
#         return JsonResponse({'errors': form.errors}, status=400)
#
#     # For GET requests, return current profile data
#     profile = request.user.profile
#     return JsonResponse({
#         'name': profile.name,
#         'email': profile.email,
#         'team': profile.team.name if profile.team else None,
#     })


@login_required
def create_team(request):
    team, created = Team.objects.get_or_create(name="Random Team")
    team.members.add(request.user)
    profile = request.user.profile
    profile.team = team
    profile.save()
    return JsonResponse({'message': f'Team {"created" if created else "joined"}: {team.name}'})


@login_required
def team_dashboard(request):
    team = request.user.profile.team
    if not team:
        return JsonResponse({'error': 'No team found.'}, status=400)

    members = list(team.members.values('username', 'email'))
    return JsonResponse({
        'team_name': team.name,
        'members': members
    })


@login_required
def submit_solution(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.save()
            return JsonResponse({'message': 'Solution submitted'})
        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
