from django.urls import path

from .views import SignUpView, User_Profile, User_Profile_Edit_View

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", User_Profile.as_view(), name="profile"),
    path("editprofile/", User_Profile_Edit_View.as_view(), name="editprofile")
]