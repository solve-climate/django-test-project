# Create your models here.

from django.db import models


class User(models.Model):
    is_admin = models.BooleanField(default=False)

class Basic_User_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Problem(models.Model):
    event_date = models.DateField()


class Team(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
