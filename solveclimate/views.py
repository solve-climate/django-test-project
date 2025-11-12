from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserDetails, Team
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("You're at the Solve Climate index page.")


@login_required
def dashboard(request):
    # Get the logged-in user's details
    user_details = UserDetails.objects.filter(user=request.user).first()
    
    if user_details and hasattr(user_details, 'team'):
        return JsonResponse({'message': 'Redirecting to team dashboard'})
    return JsonResponse({'message': 'Redirecting to create team'})


@csrf_exempt
@login_required
def edit_profile(request):
    user_details = UserDetails.objects.filter(user=request.user).first()

    if request.method == 'POST':
        name = request.POST.get('name')
        if user_details:
            user_details.name = name
            user_details.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        else:
            return JsonResponse({'error': 'User profile not found'}, status=404)

    if user_details:
        return JsonResponse({
            'name': user_details.name,
            'is_active': user_details.is_active,
            'date_joined': user_details.date_joined,
        })
    return JsonResponse({'error': 'No profile found'}, status=404)


@csrf_exempt
@login_required
def create_team(request):
    # For demo purposes, always creates or joins a "Default Team"
    team, created = Team.objects.get_or_create(problem_id=1)  # assuming a problem exists
    user_details = UserDetails.objects.filter(user=request.user).first()
    if not user_details:
        return JsonResponse({'error': 'User details not found'}, status=404)

    user_details.name = user_details.name or request.user.username
    user_details.save()

    return JsonResponse({
        'message': f'Team {"created" if created else "joined"} successfully'
    })


@login_required
def team_dashboard(request):
    team = Team.objects.first()
    if not team:
        return JsonResponse({'error': 'No team found'}, status=404)

    members = list(UserDetails.objects.all().values('name', 'is_active'))
    return JsonResponse({
        'team': str(team),
        'members': members
    })


@csrf_exempt
@login_required
def submit_solution(request):
    if request.method == 'POST':
        data = request.POST.get('solution')
        if not data:
            return JsonResponse({'error': 'No solution data provided'}, status=400)
        return JsonResponse({'message': 'Solution submitted successfully'})
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

