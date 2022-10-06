from dataclasses import field
from unicodedata import name
from rest_framework import serializers

from .models import Questions

class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questions
        fields = ('name',)
    
