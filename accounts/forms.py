from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class  RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError('This email already exists')
        return email