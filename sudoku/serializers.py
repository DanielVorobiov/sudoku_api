from rest_framework import serializers

from sudoku.models import Sudoku


class SudokuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sudoku
        fields = '__all__'
