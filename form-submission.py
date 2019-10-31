# FORM SUBMISSIONS -------------------------------------------------

# Define a new url in web
    url(r'^registration$', views.registration,name="registration"),

# add name to input fields, update action and method
<form action="{% url 'web:registration' %}" method="post">
{% csrf_token %}

#Import Registration in view
from web.models import About, Registration
# Define a new view
def registration(request):
    if request.method:

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        message = request.POST.get('message')

        Registration.objects.create(
            name = name,
            email = email,
            phone = phone,
            dob = dob,
            education = education,
            message = message
        )

        return HttpResponse("Form Submitted")
    else:
        return HttpResponse("Invalid Request")

# DJANGO FORM SUBMISSION-------------------------------------------------

# Create a file web/forms.py
from django import forms
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _
from web.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

# Import RegistrationForm to views.py
from web.forms import RegistrationForm
# Pass form variable and update context in views.py
def index(request):
    about_datas = About.objects.all()
    form = RegistrationForm()
    context = {
        "title" : "Home",
        "caption" : "Femme Caption",
        "about_datas" : about_datas
        "form" : form
    }
    return render(request, 'web/index.html',context)

# Replace input tag in html
        <p class="first">
            <label for="{{form.name.id_for_label}}">{{form.name.label}}</label>
            {{form.name}}
        </p>

    # Alternative 1
            {% for field in form %}
                <p class="first">
                    <label for="{{field.id_for_label}}">{{field.label}}</label>
                    {{field}}
                </p>
            {% endfor %}

    # Alternative 2
            {{form.as_p}}

# Adding classes and placeholder, Updating error messages and labels in forms.py
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
            'email': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'education': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Education'}),
            'message': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Message'}),
            'dob': TextInput(attrs={'class': 'required form-control', 'placeholder': 'DOB'} blank=True,null=True),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'email': {
                'required': _("Email field is required."),
            },
            'phone': {
                'required': _("Phone field is required."),
            },
            'education': {
                'required': _("Education field is required."),
            },
            'dob': {
                'required': _("DOB field is required."),
            },
            'message': {
                'required': _("Message field is required."),
            },
        }
        labels = {
            'name' : "What we should call you ?",
            'phone' : "And your phone number ?",
            'message' : "What is in your mind ?",
        }

# Registration can be redefined simply when using django forms
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print form.errors
            return HttpResponse("Validation Error")

        return HttpResponse("Form Submitted")
    else:
        return HttpResponse("Invalid Request")

# Customising Error messages
    # Create a new file web/functions.py

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

    # Import in views
    from web.functions import generate_form_errors

    # Update registration function
    def registration(request):
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print form.errors
                errors = generate_form_errors(form,formset=False)
                return HttpResponse(errors)

            return HttpResponse("Form Submitted")
        else:
            return HttpResponse("Invalid Request")

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
    # Update registration model in views.py

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
                    message = generate_form_errors(form,formset=False)

                    response_data = {
                        "status" : "false",
                        "stable" : "true",
                        "title" : "Form validation error",
                        "message" : message
                    }

                return HttpResponse(json.dumps(response_data), content_type='application/javascript')
            else:
                return HttpResponse("Invalid Request")

    # Import json in views.py
         import json

    # Add sweatalert.css and sweatalert.min.js to static folder
    # Link in html head tag
    # Add loader form styles of popup in style.css

# Removing Required fields -------------------------------------------------

    # Add  (blank=True, null=True) to models.py
    # Remove required class and associated error messages from forms.py
    # Migrate changes
