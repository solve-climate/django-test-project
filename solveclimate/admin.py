# Register your models here.
from django.contrib import admin
from .models import User, UserDetails, Problem, Team, Participant

# Basic admin registration
admin.site.register(User)
admin.site.register(UserDetails)
admin.site.register(Problem)
admin.site.register(Team)
admin.site.register(Participant)

