from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Aluno
from .AlunoSerializer import AlunoSerializer

class AlunoViewSets(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
