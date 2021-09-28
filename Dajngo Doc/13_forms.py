# web/forms.py
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('timestamp',)
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Phone'}),
            'place': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Location'}),
            'email': EmailInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email Address'}),
            'message': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Type Your Message'}),
        }
        
        
class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		exclude = ('auto_id','slug','timestamp')
		widgets = {
			'title': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title'}),
			'category' : Select(attrs={'class': 'form-control',}),
			'author' : Select(attrs={'class': 'form-control',}),
			'featured_image': FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
			'content': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Content'}),
			'video_url': URLInput(attrs={'class': 'required form-control', 'placeholder': 'Video Link'}),
			'assign_to' : SelectMultiple(attrs={'class': 'required form-control'}),
			'is_active' : CheckboxInput(attrs={}),
		}
		error_messages = {
			'name': {
				'required': _("Name field is required."),
			},
			'content': {
				'required': _("Content field is required."),
			},
		}
		labels = {
			'name' : "What we should name it?",
			'content' : "What is in your mind ?",
		}
	
	
class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		exclude = ('id', 'date_added')
		widgets = {
			'full_name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Full Name'}),
			'phone_number': NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Phone Number'}),
			'whatsapp_number': TextInput(attrs={'class': 'form-control', 'placeholder': ' Whatsapp Number'}),
			'place': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Place'}),
			'gender': Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
		}
		labels = {
			'full_name': "Full Name",
		}
	def clean_username(self):
		username = self.cleaned_data['phone_number']
		if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
			raise forms.ValidationError(u'Phone Number "%s" is already in use.' % username)
		return username
