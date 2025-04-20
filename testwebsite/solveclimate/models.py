# Create your models here.

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)


class Basic_User_Details(models.Model):
    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToOneRel(to=User, field='id', field_name='user id')
    team_id = models.ForeignKey(to=Team, to_field='id', on_delete=models.CASCADE)
