from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import DetalheTurma
from .DetalheTurmaSerializer import DetalheTurmaSerializer

class DetalheTurmaViewSets(viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer
