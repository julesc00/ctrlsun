from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from .models import BranchLocation, NewUser, WorkingTime
from .serializers import BranchLocationSerializer, UserSerializer, WorkingTimeSerializer, StaffSerializer


class BranchLocationViewSet(viewsets.ModelViewSet):
    """Perform CRUD operations for BranchLocation Model."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = BranchLocation.objects.all()
    serializer_class = BranchLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^branch_name", "^city", "^country"]


class UserViewSet(viewsets.ModelViewSet):
    """Perform CRUD operations for custom user model."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^username", "^role", "^branch__branch_name"]


class StaffViewSet(viewsets.ModelViewSet):
    """Perform CRUD operations for user model."""

    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = StaffSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^username", "^email"]


class WorkingTimeViewSet(viewsets.ModelViewSet):
    """Perform CRUD operations for WorkingTime model."""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^employee__username", "^event_record", "^action"]
