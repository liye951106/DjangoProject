from django.shortcuts import render
from django.contrib.auth.models import User,Group
from api.serializers import UserSerializer,GroupSerializer
from rest_framework import viewsets
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all().order_by('-date_joined')
	serializer_class=UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
	queryset=Group.objects.all()
	serializer_class=GroupSerializer

