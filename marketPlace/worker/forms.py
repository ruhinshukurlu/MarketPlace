from django import forms
from django.db import transaction
from worker.models import *



class AddSkillForm(forms.ModelForm):
    vehicles = forms.ModelMultipleChoiceField(queryset=Vehicle.objects.all(), widget=forms.CheckboxSelectMultiple)
    tools= forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Skill
        fields = ("price",'experience','service','vehicles', 'tools',)

        widgets = {
            'price': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'rows' : '5'
                }),
            'service' : forms.Select(attrs = {
                'class' : 'form-control',
            })
        }

        


class SkillImageForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo', widget = forms.ClearableFileInput(attrs={
        'class' : 'photo-input'
    }))

    class Meta:
        model = SkillPhoto
        fields = ('image', )


class TaskForm(forms.ModelForm):
   
    class Meta:
        model = Task
        fields = ("text", 'date', 'time',)
        
        widgets = {
            'time' : forms.TimeInput(attrs={
                'class' : 'form-control',
                'type' : 'time'
            }),
            'text' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : '5',
                'placeholder' : 'Write short message about your task...'
            }),
            'date' : forms.DateInput(attrs={
                'class' : 'form-control',
                'type' : 'date'
            })
        }


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ("text",)

        widgets = {
            'text' : forms.Textarea(attrs={
                'class' : 'form-control',
                'cols' : "30",
                'rows' : "5",
                'placeholder':"Please, write your review about service quality"
            }),
            

        }
