from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import UserProfile


class User_Profile_Edit_View(UpdateView):
    model = UserProfile
    fields = ['interests']
    success_url = reverse_lazy("login")
    template_name = "solveclimate/edit_user_profile.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class User_Profile(ListView):
    model = UserProfile
    template_name = "solveclimate/user_profile.html"
