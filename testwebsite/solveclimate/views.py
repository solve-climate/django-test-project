from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Profile, Team
from .forms import ProfileForm, SolutionForm
import uuid


def index(request):
    return JsonResponse({'message': "You're at the solve climate index."})


@login_required
def dashboard(request):
    try:
        profile = request.user.profile
        if profile.team:
            return JsonResponse({'message': 'Redirecting to team dashboard'})
        return JsonResponse({'message': 'Redirecting to create team'})
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        return JsonResponse({'errors': form.errors}, status=400)

    # GET request — return profile data
    return JsonResponse({
        'name': getattr(profile, 'name', ''),
        'email': request.user.email,
        'team': profile.team.name if profile.team else None,
    })


@login_required
def create_team(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

    # Create a unique team name
    team_name = f"Team-{uuid.uuid4().hex[:6]}"
    team = Team.objects.create(name=team_name)
    team.members.add(request.user)

    profile.team = team
    profile.save()

    return JsonResponse({'message': f'Team created: {team.name}'})


@login_required
def team_dashboard(request):
    try:
        profile = request.user.profile
        team = profile.team
        if not team:
            return JsonResponse({'error': 'No team found.'}, status=400)

        members = list(team.members.values('username', 'email'))
        return JsonResponse({
            'team_name': team.name,
            'members': members
        })
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@require_POST
@login_required
def submit_solution(request):
    try:
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.save()
            return JsonResponse({'message': 'Solution submitted successfully'})
        return JsonResponse({'errors': form.errors}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
