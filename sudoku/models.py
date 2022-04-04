from django.db import models
from django.contrib.auth import get_user_model


class Sudoku(models.Model):
    class ComplexityLevels(models.TextChoices):
        EASY = 'easy'
        MEDIUM = 'medium'
        HARD = 'hard'

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    complexity = models.CharField(choices=ComplexityLevels.choices, max_length=6)
    puzzle = models.CharField(max_length=81)
