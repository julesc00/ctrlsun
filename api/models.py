from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

ROLES = (
    ("BOSS", "BOSS",),
    ("ACCOUNTING", "ACCOUNTING",),
    ("ACCOUNTING", "GENERAL",),
)

TIMES = (
    (1, "StartWorkingTime"),
    (2, "EndWorkingTime"),
)


class BranchLocation(models.Model):
    branch_name = models.CharField(max_length=75, default=1, unique=True)
    country = models.CharField(max_length=75)
    city = models.CharField(max_length=75, null=True)

    def __str__(self):
        return self.branch_name


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
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    event_record = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=75, choices=TIMES)

    def __str__(self):
        return self.event_record
