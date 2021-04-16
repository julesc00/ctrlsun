from django.shortcuts import render
from django.contrib.auth import get_user_model

from api.models import BranchLocation, NewUser, WorkingTime


def home_view(request):
    context = {
        "title": "Ctrl-Sun App"
    }

    return render(request, "core/index.html", context)
