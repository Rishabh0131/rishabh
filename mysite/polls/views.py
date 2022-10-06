from django.shortcuts import render

from rest_framework import viewsets

from .serializer import QuestionSerializer
from .models import Questions

class Questionsviewset(viewsets.ModelViewSet):

    queryset = Questions.objects.all()

    serializer_class =QuestionSerializer

