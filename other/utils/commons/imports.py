from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, resolve_url
from django.template import loader
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.formats import get_format
from django.utils.functional import cached_property
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _
import json

from django.forms.widgets import (
    TextInput, NumberInput, EmailInput, URLInput, PasswordInput, HiddenInput, MultipleHiddenInput,
    FileInput, ClearableFileInput, Textarea, DateTimeBaseInput, DateInput, DateTimeInput, TimeInput,
    CheckboxInput, ChoiceWidget, Select, NullBooleanSelect, SelectMultiple, RadioSelect,
    CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget
)
