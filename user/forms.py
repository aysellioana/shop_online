from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from user.models import ExtendUser


class UserForm(UserCreationForm):
    model = ExtendUser
    fields = ['first_name', 'last_name','username', 'email', 'date_of_birth', 'phone', 'address','postal_code']
    widgets = {
        'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                       'class': 'form-control'}),
        'last_name': TextInput(attrs={'placeholder':'Please enter your last_name', 'class':'form-control'}),
        'username': TextInput(attrs={'placeholder': 'Please enter your username', 'class': 'form-control'}),
        'email': TextInput(attrs={'placeholder': 'Please enter you email', 'class': 'form-control'}),
        'date_of_birth': TextInput(
            attrs={'placeholder': 'Please enter your date of birth', 'class': 'form-control', 'type': 'date'}),
        'phone': TextInput(attrs={'placeholder': 'Please enter your phone', 'class': 'form-control'}),
        'address': TextInput(attrs={'placeholder': 'Please enter your address', 'class': 'form-control'}),
        'postal_code': TextInput(attrs={'placeholder': 'Please enter your postal code', 'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password confirmation'
