from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import NewUser, BranchLocation, WorkingTime


class BranchLocationSerializer(serializers.ModelSerializer):
    """Serialize data for the BranchLocation model."""

    url = serializers.HyperlinkedIdentityField(view_name="branches-detail")

    class Meta:
        model = BranchLocation
        fields = ("branch_name", "city", "country", "url")


class UserSerializer(serializers.ModelSerializer):
    """Serialize data for the custom user model."""

    url = serializers.HyperlinkedIdentityField(view_name="users-detail")

    class Meta:
        model = NewUser
        fields = ("username", "password", "role", "branch", "url")


class StaffSerializer(serializers.ModelSerializer):
    """Serialize data for the default User model."""

    url = serializers.HyperlinkedIdentityField(view_name="staff-detail")

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "url")


class WorkingTimeSerializer(serializers.ModelSerializer):
    """Serialize data for the employee working-time model."""

    url = serializers.HyperlinkedIdentityField(view_name="working-time-detail")

    class Meta:
        model = WorkingTime
        fields = ("employee", "event_record", "action", "url")



