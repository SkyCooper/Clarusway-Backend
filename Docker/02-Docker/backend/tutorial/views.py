from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Tutorial
from .serializers import TutorialSerializer

#fbv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TutorialMVS(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer