from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def usr_name(value):
	pattern = re.compile("^[a-zA-Z]{3,}$")
	#"^[A-Za-z]\\w{5, 29}$"
	if  len(value)>30 or len(value)<3:
		raise ValidationError("Min 4 and Max 12 Characters")
	if not pattern.match(value):
		raise ValidationError("Only Alphabets")
		

class UserLoginForm(forms.Form):
    username = forms.CharField(initial = "username",max_length = 12,validators=[usr_name])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(initial = "username",max_length = 12,validators=[usr_name])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(
        label='Password confirmation',
        help_text='Enter the same password as before, for verification.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Re Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
