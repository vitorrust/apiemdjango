from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import DetalheDisciplina
from .DetalheDisciplinaSerializer import DetalheDisciplinaSerializer

class DetalheDisciplinaViewSets(viewsets.ModelViewSet):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer
