from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from api.models import BranchLocation, NewUser, WorkingTime

User = get_user_model()


class BranchLocationForm(forms.ModelForm):
    class Meta:
        model = BranchLocation
        fields = "__all__"

        widgets = {
            "branch_name": forms.TextInput(attrs={
                "class": "validate",
                "id": "branch_name",
                "type": "text"
            }),
            "country": forms.TextInput(attrs={
                "class": "validate",
                "id": "country",
                "type": "text"
            }),
            "city": forms.TextInput(attrs={
                "class": "validate",
                "id": "country",
                "type": "text"
            })
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "validate",
                "id": "username",
                "type": "text",
            }),
            "email": forms.EmailInput(attrs={
                "class": "validate",
                "id": "email",
                "type": "text",
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password1",
                "type": "password",
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password2",
                "type": "password",
            })
        }


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "validate",
                "id": "username",
                "type": "text",
            }),
            "password": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password",
                "type": "password",
            })
        }
