from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions

from .models import BranchLocation, NewUser, WorkingTime
from .serializers import BranchLocationSerializer, UserSerializer, WorkingTimeSerializer, StaffSerializer


class BranchLocationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BranchLocation.objects.all()
    serializer_class = BranchLocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer


class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = StaffSerializer


class WorkingTimeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
