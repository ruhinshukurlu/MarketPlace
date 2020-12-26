from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.db import transaction
from .models import *
from datetime import datetime

class CustomerRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder' : 'First Name',
                }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder' : 'Last Name',
                }))
    username = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder' : 'Email',
                }))
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder' : 'Password',
                }))
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-control height',
                    'placeholder' : 'Re-enter Password',
                }))
                
    # profile_image = forms.FileField('Profile', max_length=, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_active = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('username')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        # customer.location=self.cleaned_data.get('location')
        customer.save()
        return user


class WorkerRegisterForm(UserCreationForm):

    LANGUAGES = (
        ('Azerbaijan', 'Azerbaijan'),
        ('English', 'English'),
        ('Russian', 'Russian'),
        ('Turkish', 'Turkish'),
    )

    EXPERIENCE = (
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('4 years', '4 years'),
        ('5+ years', '5+ years'),

    )

    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-control register-input',
                    
                }), label = 'Password')
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-control register-input',
                    
                }), label = 'Confirm Password')
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-control register-input',
                }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-control register-input',
                }))
    username = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                    'class': 'form-control register-input',
                }), label='Email Address')

    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-control register-input',
                }))

    work_place = forms.ChoiceField(choices=[(work_place.title, work_place.title) for work_place in WorkPlace.objects.all()], widget=forms.Select(attrs={
                    'class': 'form-control register-input',
                }))
    
    about = forms.CharField(widget=forms.Textarea(attrs={
                    'class': 'form-control register-input',
                    'rows' : '5'
    }))

    languages = forms.ChoiceField(choices=LANGUAGES, widget=forms.Select(attrs={
                    'class': 'form-control register-input',
    }))

    experience = forms.ChoiceField(choices=EXPERIENCE, widget=forms.Select(attrs={
                    'class': 'form-control register-input',
    }))

    birth_date = forms.DateField(widget=forms.SelectDateWidget(attrs={
                    'class': 'form-control register-input',
    }, years=range(1950, datetime.now().year+1 )))

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_worker = True
        user.is_active = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('username')
        user.save()
        company = Worker.objects.create(user=user)
        company.phone_number=self.cleaned_data['phone_number']
        company.work_place=self.cleaned_data['work_place']
        company.about=self.cleaned_data['about']
        company.languages=self.cleaned_data['languages']
        company.experience=self.cleaned_data['experience']
        company.birth_date=self.cleaned_data['birth_date']

        company.save()
        return user
 
  
class LoginForm(forms.Form):
    username = forms.EmailField(widget = forms.EmailInput(attrs = {
        'placeholder' : 'Email',
        'class' : 'form-control',
    }), label='Email')
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'placeholder' : 'Password',
        'class' : 'form-control',
    }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Old password'
    }), required=True)

    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'New password'
    }), required=True)

    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Re-enter new password'
    }), required=True)
    
    
class UserEditForm(forms.ModelForm):
    # profile_img = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','profile_img']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control height mb-4',
                'placeholder' : 'First Name',
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control height mb-4',
                'placeholder' : 'Last Name',
                }),
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control height mb-4',
                'placeholder' : 'Email'
            })
        }