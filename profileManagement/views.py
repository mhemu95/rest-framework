from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import profileSerializer


class profile_generic_view(generics.ListAPIView, generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

