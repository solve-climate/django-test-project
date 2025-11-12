# Create your models here.

from django.db import models

class User(models.Model):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{'Admin' if self.is_admin else 'User'} #{self.id}"


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        status = 'active' if self.is_active else 'inactive'
        return f"{self.name} ({status})"


class Problem(models.Model):
    event_date = models.DateField()
    statement = models.TextField()

    def __str__(self):
        return f"{self.statement} ({self.event_date})"


class Team(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team #{self.id} - Problem: {self.problem.statement}"


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} in {self.team}"

