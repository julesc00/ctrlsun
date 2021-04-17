from django.contrib import admin

from .models import NewUser, BranchLocation, WorkingTime


@admin.register(BranchLocation)
class BranchAdmin(admin.ModelAdmin):
    """Personalize the BranchLocation panel."""

    ordering = ("-branch_name",)
    search_fields = ("branch_name", "country", "city",)
    list_display = ("branch_name", "city", "country",)
    fieldsets = (
        (None, {"fields": ("branch_name", "city", "country")}),
    )


@admin.register(NewUser)
class EmployeeAdmin(admin.ModelAdmin):
    """Personalize the custom user panel."""

    search_fields = ("username", "branch", "role",)
    ordering = ("-username",)
    list_display = ("username", "password", "role", "branch",)
    fieldsets = (
        (None, {"fields": ("username", "password", "branch", "role")}),
    )


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    """Personalize the employee working-time panel"""
    ordering = ("-event_record",)
    search_fields = ("employee", "event_record", "action",)
    list_display = ("employee", "event_record", "action",)
    fieldsets = (
        (None, {"fields": ("employee", "action")}),
    )



