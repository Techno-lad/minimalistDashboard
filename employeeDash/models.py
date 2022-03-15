from django.db import models

# Create your models here.


class Supervisor(models.Model):

    SupervisorId = models.CharField(max_length=10, primary_key=True)
    Firstname = models.CharField(max_length=10)
    Lastname = models.CharField(max_length=10)
    Hourly_rate = models.IntegerField()
    TeamName = models.CharField(max_length=10)
    TeamAvg_HandleTime = models.FloatField(default=0)
    TeamAvg_Cx_rating = models.FloatField(default=0)
    location = models.CharField(max_length=10)

    def __str__(self):
        return "{}-{}".format(
            self.SupervisorId,
            self.Firstname,
            self.Lastname,
            self.Hourly_rate,
            self.TeamName,
            self.TeamAvg_HandleTime,
            self.TeamAvg_Cx_rating,
            self.location,
        )


class Employees(models.Model):

    Empid = models.CharField(max_length=10, primary_key=True)
    Firstname = models.CharField(max_length=10)
    Lastname = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    Avg_HandleTime = models.FloatField(default=0)
    Avg_Cx_rating = models.FloatField(default=0)
    Total_Chats = models.IntegerField(default=0)
    Hourly_rate = models.IntegerField(default=0)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(
            self.Empid,
            self.Firstname,
            self.Lastname,
            self.location,
            self.Avg_HandleTime,
            self.Avg_Cx_rating,
            self.Total_Chats,
            self.supervisor,
        )
