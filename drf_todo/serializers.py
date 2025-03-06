from drf_todo.models import TodoDRF
from rest_framework import serializers

#dev_drf_todo_1
class TodoDRFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDRF
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')
