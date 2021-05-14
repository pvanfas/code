from django import forms
from .models import Comment,Contact
from django.forms.widgets import TextInput, Textarea, EmailInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','time','approved']
        widgets = {
            'name': TextInput(attrs={'class': 'required'}),
            'message': Textarea(attrs={'class': 'required'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required lh-25 mb-30', 'placeholder': 'Your Name *'}),
            'email': EmailInput(attrs={'class': 'required lh-25 mb-30', 'placeholder': 'Your Email Address'}),
            'mobile': TextInput(attrs={'class': 'required lh-25 mb-30', 'placeholder': 'Your Mobile Number *'}),
            'message': Textarea(attrs={'class': 'required','cols':'10', 'rows':'6', 'placeholder': 'Message'}),
        }
