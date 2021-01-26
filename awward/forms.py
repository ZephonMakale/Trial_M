from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Profile, Project,Review,Image
from django.forms import ModelForm, Textarea, IntegerField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email') 
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user',]
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating']
class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user',]               