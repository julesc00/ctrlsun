from django.contrib import admin

from .models import NewUser, BranchLocation, WorkingTime


@admin.register(BranchLocation)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(NewUser)
class EmployeeAdmin(admin.ModelAdmin):
    ordering = ("-username",)
    list_display = ("username", "password", "role", "branch")
