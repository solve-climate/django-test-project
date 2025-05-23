from django import forms
from .models import Profile, ProblemProposal, Solution

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class ProblemProposalForm(forms.ModelForm):
    class Meta:
        model = ProblemProposal
        fields = ['title', 'description']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['content']
