from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes
from .serializers import NotesSerializer


class NotesListCreate(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
