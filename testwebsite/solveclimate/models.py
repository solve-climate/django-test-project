from django.contrib.auth.models import User
from django.db import models


class Problem(models.Model):
    event_date = models.DateField()
    statement = models.TextField()

    def __str__(self) -> str:
        return ('id: ' + str(self.id)
                + ', event_date: ' + str(self.event_date)
                + ', statement: ' + self.statement)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interests = models.TextField()

    def __str__(self):
        return ('id: ' + str(self.id)
                + ', problem id: ' + str(self.problem))


class Team(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ('id: ' + str(self.id)
                + ', problem id: ' + str(self.problem))


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ('id: ' + str(self.id)
                + ', user id: ' + str(self.user)
                + ', team id: ' + str(self.team))


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self) -> str:
        return ('id: ' + str(self.id)
                + ', problem id ' + str(self.problem)
                + ', description: ' + str(self.description))
