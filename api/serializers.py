from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import NewUser, BranchLocation, WorkingTime


class BranchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLocation
        fields = ("id", "branch_name", "city", "country")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("id", "username", "password", "role", "branch")


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password")


class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = ("id", "employee", "event_record", "action")



