from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = CustomUser
		fields = ["username", "email", "password1", "password2"]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')