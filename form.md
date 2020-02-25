**models.py**
```
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDER_TYPES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Registration(models.Model):
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
    choice = models.CharField(max_length=128,choices=GENDER_TYPES,default="male")
    notes = models.TextField(blank=True,null=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'web_registration'
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')
        ordering = ('auto_id',)

    class Admin:
        list_display = ('name','email','notes')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
```
**forms.py**
```
from django import forms
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _
from web.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'message': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Message'}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'message': {
                'required': _("Message field is required."),
            },
        }
        labels = {
            'name' : "What we should call you ?",
            'message' : "What is in your mind ?",
        }
```
**views.py**
```
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from web.functions import generate_form_errors
import json


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Registration successfully updated"
            }
        else:
            message = generate_form_errors(form)

            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponse("Invalid Request")
```

**functions.py**
```
def generate_form_errors(args,formset=False):
    message = ''
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors
        for err in args.non_field_errors():
            message += str(err)

    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message +=field.errors
            for err in form.non_field_errors():
                message += str(err)
    return message
```
**Template**
```
<form action="" method="post">

    {% csrf_token %}

    {{form.as_p}}

    <button type="submit">Submit</button>

<form>
```
```
<form action="" method="post">

    {% csrf_token %}

    {% for field in form %}
        <p class="first">
            <label for="{{field.id_for_label}}">{{field.label}}</label>
            {{field}}
        </p>
    {% endfor %}

    <button type="submit">Submit</button>

<form>
```
```
<form action="" method="post">

    {% csrf_token %}

    <p class="first">
        <label for="{{form.name.id_for_label}}">{{form.name.label}}</label>
        {{form.name}}
    </p>

    <p class="first">
        <label for="{{form.name.id_for_label}}">{{form.name.label}}</label>
        {{form.name}}
    </p>

    <button type="submit">Submit</button>

<form>
```


# AJAX Form submission
    # Upadate script.js with ajax function
    # add ajax,reload class to form tag

    # add show_loader(),remove_popup() functions to script.js
        function show_loader(){
            $('.popup-bg').show();
            $('.popup-box').remove();
            $('body').append('<div class="popup-box"><div class="preloader pl-xxl"><svg viewBox="25 25 50 50" class="pl-circular"><circle r="20" cy="50" cx="50" class="plc-path"/></svg></div></div><span class="popup-bg"></span>');
        }

        function remove_popup(){
            $('.popup-box,.popup-bg').remove();
        }


    # Add sweatalert.css and sweatalert.min.js to static folder
    # Link in html head tag
    # Add loader form styles of popup in style.css
