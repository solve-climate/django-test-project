from django import forms

from .models import Problem, Solution


class ProblemProposalForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['event_date', 'statement']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['description']
