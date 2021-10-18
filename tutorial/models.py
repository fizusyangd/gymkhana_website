from django.db import models

# Create your models here.

class OutlookUser(models.Model):
    name = models.CharField(default="No Title", max_length=264)
    email = models.CharField(default="No Title", max_length=264)

class Team(models.Model):
    team_name = models.CharField(default="No Title", max_length=264)
    start_date = models.DateTimeField(default="no date")
    end_date = models.DateTimeField(default="no date")

