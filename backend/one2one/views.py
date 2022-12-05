from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, OkrSerializer, One2OneSerializer
from .models import Project, Okr, One2One

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
  

class One2OneViewSet(viewsets.ModelViewSet):
    queryset = One2One.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = One2OneSerializer


class OkrViewSet(viewsets.ModelViewSet):
    queryset = Okr.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OkrSerializer
