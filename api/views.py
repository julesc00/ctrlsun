from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .models import BranchLocation, NewUser, WorkingTime
from .serializers import BranchLocationSerializer, UserSerializer, WorkingTimeSerializer


class BranchLocationViewSet(viewsets.ModelViewSet):
    queryset = BranchLocation.objects.all()
    serializer_class = BranchLocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer


class WorkingTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
