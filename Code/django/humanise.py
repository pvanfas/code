Django comes with a set of template filters to add a “human touch” to your data. 
It is used to translate numbers and dates into a human readable format.

#add foolowing to your INSTALLED_APPS in setting:
django.contrib.humanize

#Now in the template, load the template tags:
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

