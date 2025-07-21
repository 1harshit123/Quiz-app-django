from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    fullname = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('fullname', 'username', 'email', 'password1', 'password2', )


    def save(self, commit=True):
        user = super().save(commit=False)
        fullname = self.cleaned_data['fullname']
        # Example: split full_name into first and last name
        names = fullname.split(' ', 1)
        user.first_name = names[0]
        if len(names) > 1:
            user.last_name = names[1]
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CreateQuizForm(forms.Form):
    title = forms.CharField(label='Quiz Title', max_length=100)
    
    description = forms.CharField(label='Description')
    
    num_questions = forms.IntegerField(
        label='Number of Questions',
        min_value=1,
        max_value=50
    )
    
    duration = forms.IntegerField(
        label='Time Duration (minutes)',
        min_value=1,
        max_value=180
    )

    