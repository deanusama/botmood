from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone = forms.CharField(required=True, max_length=20)
    class Meta:
        model = User

        fields = ('username', 'email', 'phone', 'password1', 'password2', )

class EditProfile(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',  'email',)