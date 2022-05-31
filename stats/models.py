from datetime import timedelta

from django.db import models
from django.contrib.auth import get_user_model


class Statistics(models.Model):
    games_number_easy = models.IntegerField(default=0)
    games_number_medium = models.IntegerField(default=0)
    games_number_hard = models.IntegerField(default=0)
    best_time_easy = models.DurationField(default="00:00:00")
    best_time_medium = models.DurationField(default="00:00:00")
    best_time_hard = models.DurationField(default="00:00:00")
    puzzle_created_number_easy = models.IntegerField(default=0)
    puzzle_created_number_medium = models.IntegerField(default=0)
    puzzle_created_number_hard = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
