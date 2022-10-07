from __future__ import unicode_literals

import json

from django.conf import settings
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
from django.forms.widgets import (
    CheckboxInput,
    CheckboxSelectMultiple,
    ChoiceWidget,
    ClearableFileInput,
    DateInput,
    DateTimeBaseInput,
    DateTimeInput,
    EmailInput,
    FileInput,
    HiddenInput,
    MultipleHiddenInput,
    MultiWidget,
    NullBooleanSelect,
    NumberInput,
    PasswordInput,
    RadioSelect,
    Select,
    SelectDateWidget,
    SelectMultiple,
    SplitDateTimeWidget,
    SplitHiddenDateTimeWidget,
    Textarea,
    TextInput,
    TimeInput,
    URLInput,
)
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
    resolve_url,
)
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
