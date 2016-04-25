from polls.models import UserProfile
from django.contrib.auth.models import User
from django import forms

# two classes: inherit from forms.ModeliForm
class UserForm(forms.ModelForm):
    #widget: hide user's password when they type it in the field
    password = forms.CharField(widget=forms.PasswordInput())

    #Meta class: describes additional props about the particular modelForm class it belongs to
    class Meta:
        model = User #Meta class must have at least this
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'picture') 
        #exclude user field!! don't need the user to see it 
