from django import forms
from django.forms import PasswordInput

from author_app.models import Author


class AuthorFormBase(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }
        widgets = {'passcode': PasswordInput(attrs={'placeholder':'Enter 6 digits...'}),
                   'first_name': forms.TextInput(attrs={'placeholder':'Enter your first name...'}),
                   'last_name': forms.TextInput(attrs={'placeholder':'Enter your last name...'}),
                   'pets_number': forms.TextInput(attrs={'placeholder': 'Enter the number of your pets...'})
                   }


class AuthorCreateForm(AuthorFormBase):
    class Meta(AuthorFormBase.Meta):
        model = Author
        fields = ('first_name', 'last_name', 'passcode', 'pets_number')


class AuthorEditForm(AuthorFormBase):
    class Meta(AuthorFormBase.Meta):
        model = Author
        exclude = ('passcode',)