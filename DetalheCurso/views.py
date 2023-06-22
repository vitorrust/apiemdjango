from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import DetalheCurso
from .DetalheCursoSerializer import DetalheCursoSerializer

class DetalheCursoViewSets(viewsets.ModelViewSet):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer
