from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20 , required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20 , required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=25 , required = True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['first_name'
         , 'last_name' , 'username'
          , "email" , 'password1'  , 'password2' ]

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user  = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
            
        if(user is not None):
            raise ValidationError("User Already Exists");
        