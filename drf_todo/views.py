from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from drf_todo.models import TodoDRF
from drf_todo.serializers import TodoDRFSerializer
from rest_framework import status

#dev_drf_todo_1
class TodoAPIView(APIView):
    def get(self, request):
        todos = TodoDRF.objects.all()
        serializer = TodoDRFSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)