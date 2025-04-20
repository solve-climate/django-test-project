# Create your models here.

from django.db import models


class User(models.Model):
    is_admin = models.BooleanField(default=False)

class Basic_User_Details(models.Model):
    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Problem(models.Model):
    event_date = models.DateField()


class Team(models.Model):
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)


class Participant(models.Model):
    user_id = models.ManyToOneRel(to=User, field='id', field_name='user id')
    team_id = models.ForeignKey(to=Team, to_field='id', on_delete=models.CASCADE)
