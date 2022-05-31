from datetime import datetime

from rest_framework import serializers

from sudoku.models import Sudoku


class SudokuSerializer(serializers.ModelSerializer):
    created_on = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Sudoku
        fields = ['id', 'puzzle', 'created_on', 'created_at', 'owner']
        extra_kwargs = {'owner': {'read_only': True}, 'created_at': {'read_only': True}}

    def get_created_on(self, obj):
        return datetime.strftime(obj.created_on, '%d.%m.%Y')

    def get_created_at(self, obj):
        return datetime.strftime(obj.created_on, '%H:%M')
