from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    last_login = forms.CharField()
    is_superuser = forms.CheckboxInput()
    is_staff = forms.CheckboxInput()
    is_active = forms.CheckboxInput()
    date_joined = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','last_login','is_superuser','is_staff','is_active','date_joined')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_login'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_staff'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['date_joined'].widget.attrs['class'] = 'form-control'


class PasswordChangingForm(PasswordChangeForm):
    # old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    # new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    # new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['type'] = 'password'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['type'] = 'password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['type'] = 'password'