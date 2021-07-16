from django.forms import ModelForm, models

from .models import todomodel
class todoform(ModelForm):
    class Meta:
        model=todomodel
        fields=['title','Priority','status']


 
from django.contrib.auth.models import User 
class SignUpForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']