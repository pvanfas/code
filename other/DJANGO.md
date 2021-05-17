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

```
with if condition
```
    {% if blog_datas %}
        <p>content here</p>
    {% else %}
        <p>Nothing Found</p>
    {% endif %}
```
Get current year
```
    {% now 'Y' %}
```
possible filtering
```
all()
filter(id=1)
filter(name="x")
filter(name__icontains="x")
exclude(name="x")
get()
```
Fix hyperlinks
```
    href="{% url 'web:index' %}
    href="{% url 'web:about' %}
    href="{% url 'web:index' %}#features
```
Including template parts
```
    "is_home" : True
    "is_about" : True
```
```
    {% if is_home %}
        {% include 'web/includes/index-spotlight.html' %}
    {% elif is_about %}
        {% include 'web/includes/about-spotlight.html' %}
    {% endif %}
```

response and Redirect
```
def index(request):
    return HttpResponseRedirect(reverse('web:about'))


def about(request):
    return HttpResponse('Hello from about')
````

31. Humanise
```
#add following to your INSTALLED_APPS in setting:

django.contrib.humanize

#In template, load the template tags:

{% load humanize %}

#sample
{% extends 'base.html' %}

{% load humanize %}

{% block content %}
  <ul>
    {% for notification in notifications %}
      <li>
        {{ notification }}
        <small>{{ notification.date|naturaltime }}</small>
      </li>
    {% empty %}
      <li>You have no unread notification.</li>
    {% endfor %}
  </ul>
{% endblock %}


Note : The for tag can take an optional {% empty %} clause whose text is displayed if the given array is empty or could not be found:

#available template filters:
apnumber    1                      becomes  one
intcomma	4500000                becomes  4,500,000
intword     1200000                becomes  1.2 million
naturalday	08 May 2016            becomes  yesterday
naturaltime	09 May 2016 20:54:31   becomes  29 seconds ago
ordinal 	3                      becomes      3rd

```
32. Adding (changeble)initial value into form (views.py)
```
form = CustomerForm(initial={
        "name" : "Default Name",
        "email" : "Default Email"
    })
```
```
# Default template tags
{{instance.date|date:"d/m/Y"}}

# Custom template tags
mkdir main/templatetags/
touch main_template_tags.py __init__.py

# on main_template_tags.py
```
```
from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
	return range(number)

@register.filter
def to_fixed_to(value):
	return "{:10.2f}".format(value)
```
```
# on required template
{% load main_template_tags %}

{{instance.date|to_fixed_to}}

```
