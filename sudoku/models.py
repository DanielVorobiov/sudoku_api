from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField


class Sudoku(models.Model):
    class ComplexityLevels(models.TextChoices):
        EASY = 'easy'
        MEDIUM = 'medium'
        HARD = 'hard'

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    complexity = models.CharField(choices=ComplexityLevels.choices, max_length=6)
    puzzle = ArrayField(ArrayField(models.CharField(max_length=1, blank=True), max_length=9), max_length=9)
    created_on = models.DateTimeField(auto_now=True)
