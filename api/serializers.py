from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import NewUser, BranchLocation, WorkingTime


class BranchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchLocation
        fields = ("branch_name", "city", "country")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("username", "password", "role", "branch")


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")


class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = ("employee", "event_record", "action")



