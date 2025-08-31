from django.db import models


class User(models.Model):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return ('id: ' + str(self.id)
                + ' ' + str(self.get_admin_status()))

    def get_admin_status(self) -> str:
        if self.is_admin:
            return 'admin'
        else:
            return 'non-admin'


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return ('id: ' + str(self.id)
                + ', name: ' + self.name
                + ', date joined: ' + str(self.date_joined)
                + ', activity status: ' + self.get_activity_status__())

    def get_activity_status__(self) -> str:
        if self.is_active:
            return 'active'
        else:
            return 'inactive'


class Problem(models.Model):
    event_date = models.DateField()
    statement = models.TextField()

    def __str__(self) -> str:
        return ('id: ' + str(self.id)
                + ', event_date: ' + str(self.event_date)
                + ', statement: ' + self.statement)


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
