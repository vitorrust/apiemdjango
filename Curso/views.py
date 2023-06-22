from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Curso
from .CursoSerializer import CursoSerializer

class CursoViewSets(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
