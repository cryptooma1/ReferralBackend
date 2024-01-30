from django.shortcuts import render
from .serializers import NomaUserSerializer
from rest_framework import viewsets
from .models import NomaUser

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = NomaUser.objects.all()
    serializer_class = NomaUserSerializer