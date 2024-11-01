from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    email = forms.EmailField(max_length=50, required=True, label="Email Address")
    username = forms.CharField(max_length=20, required=True, help_text="")
    password1 = forms.CharField(max_length=20, required=True, label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), )
    password2 = forms.CharField( max_length=20, required=True, label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class SignInForm(AuthenticationForm):
    pass


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    email = forms.EmailField(max_length=50, required=True, label="Email Address")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileUpdateForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))
    city = forms.CharField(max_length=20, label="City")
    zip = forms.CharField(max_length=10, label="Zip Code")
    country = forms.CharField(max_length=20, label="Country")
    mobile = forms.CharField(max_length=14, label="Mobile Number")
    class Meta:
        model = Profile
        fields = ["address", "city", "zip", "country", "mobile"]