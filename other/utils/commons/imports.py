from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, resolve_url
from django.utils.formats import get_format
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
import json

from django.forms.widgets import (
    TextInput, NumberInput, EmailInput, URLInput, PasswordInput, HiddenInput, MultipleHiddenInput,
    FileInput, ClearableFileInput, Textarea, DateTimeBaseInput, DateInput, DateTimeInput, TimeInput,
    CheckboxInput, ChoiceWidget, Select, NullBooleanSelect, SelectMultiple, RadioSelect,
    CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget
)
