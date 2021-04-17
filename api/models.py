from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

ROLES = (
    ("BOSS", "BOSS",),
    ("ACCOUNTING", "ACCOUNTING",),
    ("GENERAL", "GENERAL",),
)

TIMES = (
    ("StartWorkingTime", "StartWorkingTime"),
    ("EndWorkingTime", "EndWorkingTime"),
)


class BranchLocation(models.Model):
    """Create a Branch Location model."""

    branch_name = models.CharField(max_length=75, unique=True)
    country = models.CharField(max_length=75)
    city = models.CharField(max_length=75, null=True)

    class Meta:
        verbose_name = "Branch Location"

    def __str__(self):
        return self.branch_name.title()


class NewUser(models.Model):
    """Create a custom user model."""

    username = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=75)
    role = models.CharField(max_length=75, choices=ROLES)
    branch = models.ForeignKey(BranchLocation, on_delete=models.CASCADE)

    class Meta:
        db_table = "Employees"
        verbose_name = "User"

    def __str__(self):
        return self.username


class WorkingTime(models.Model):
    """Create an employee working-time model."""

    employee = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    event_record = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=75, choices=TIMES)

    def get_date(self):
        time = datetime.now()
        if self.event_record.day == time.day:
            return str(time.hour - self.event_record.hour) + "hours ago"
        else:
            if self.event_record.month == time.month:
                return str(time.day - self.event_record.day) + "days ago"

        return self.event_record

    class Meta:
        verbose_name = "Working Time"

    def __str__(self):
        return str(self.event_record).title()
