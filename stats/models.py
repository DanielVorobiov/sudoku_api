from django.db import models
from django.contrib.auth import get_user_model


class Statistics(models.Model):
    games_number = models.IntegerField(default=0)
    best_time = models.DurationField(default=0)
    puzzle_created_number = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
