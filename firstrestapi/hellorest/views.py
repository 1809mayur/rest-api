from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,GroupSerializer
from django.contrib.auth.models import User,Group

# Create your views here.

def hello(request):
	return HttpResponse("Hello here")


class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to viewed or edited.

	queryset = User.objects.all().order_by("-date_joined") 
	serializer_class = UserSerializer
	permission_class = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
	# API endpoints that allows groups to be viewed or edited.

	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_class = [permissions.IsAuthenticated]