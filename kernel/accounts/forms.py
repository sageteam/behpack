from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.hashers import check_password
from django.utils import timezone

from painless.error_messages import Messages


msg = Messages()


class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('confirm_password', )


    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')

    
    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user


class SignInForm(AuthenticationForm):

    username = forms.CharField(
        error_messages = {
            'required': msg.required,
            'max_length': msg.max_length(30)
            },
        max_length = 30, 
        required = True, 
        widget = forms.EmailInput(
            attrs = { 
                'autofocus': True,
                'style': 'direction: rtl;'
                }
            )
        )


    password = forms.CharField(
        error_messages = {
                'required': msg.required
        },
        widget = forms.PasswordInput(
            attrs = {
                'style': 'direction: rtl;'
            }
        ), 
        required = True)


    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'ایمیل'
        self.fields['password'].label = 'رمز عبور'


class SignUpForm(UserCreationForm):
    email = forms.CharField(
        error_messages = {
            'required': msg.required,
            'max_length': msg.max_length(30)
            },
        max_length = 30, 
        required = True, 
        widget = forms.EmailInput(
            attrs = { 
                'autofocus': True,
                'style': 'direction: rtl;'
                }
            )
        )


    password1 = forms.CharField(
        error_messages = {
                'required': msg.required
        },
        widget = forms.PasswordInput(
            attrs = {
                'style': 'direction: rtl;'
            }
        ), 
        required = True)


    password2 = forms.CharField(
        error_messages = {
                'required': msg.required
        },
        widget = forms.PasswordInput(
            attrs = {
                'style': 'direction: rtl;'
            }
        ), 
        required = True)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'ایمیل'
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'

    
    class Meta:
        model = User
        fields = ('email',)
    
