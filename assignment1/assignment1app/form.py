from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
          Password=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2)
          ConfirmPassword=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2, label='Confirm Password')
          class Meta:
                  model = User
                  fields = ('name', 'age', 'place', 'photo', 'email',)


class LoginForm(forms.ModelForm):
        Password=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2)
        class Meta:
                model = User
                fields = ('email',)


class UpdateForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ('name', 'age', 'place', 'email')


class ChangepasswordForm(forms.ModelForm):
        OldPassword=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2)
        NewPassword=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2)
        ConfirmPassword=forms.CharField(widget=forms.PasswordInput, max_length=8, min_length=2)
        class Meta:
                model = User
                fields = ('password',)