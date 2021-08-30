
## View decorators
Django provides several decorators that can be applied to views to support various HTTP features.

#### @login_required
```
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```
#### @require_http_methods
```
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
```
### Numeric for loop in Django templates
```
@register.filter(name='times') 
def times(number):
    return range(number)
```
```
{% load my_filters %}
{% for i in 15|times %}
    <li>Item</li>
{% endfor %}
```
#### @group_required

Sometimes we need to protect some views, to allow a certain group of users to access it. Instead of checking within it if the user belongs to that group/s, we can use the following decorator
```
from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated:
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)


# The way to use this decorator is:
@group_required(‘admins’, ‘seller’)
def my_view(request, pk)
    ...
```
#### @anonymous_required

This decorator is based on the decorator login_required of Django, but looks for the opposite case, that the user is anonymous, otherwise the user is redirected to the website defined in our settings.py and can be useful when we want to protect logged user views, such as the login or registration view
```
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = settings.LOGIN_REDIRECT_URL

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous(),
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


# The way to use this decorator is:
@anonymous_required
def my_view(request, pk)
    ...
```
#### @superuser_only

This is the same case as when we want to allow certain groups access to a view, but in this case only super users can visit it.
```
from django.core.exceptions import PermissionDenied


def superuser_only(function):
  """Limit view to superusers only."""

   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied           
       return function(request, *args, **kwargs)
   return _inner


# The way to use this decorator is:
@superuser_only
def my_view(request):
    ...
```
#### @ajax_required

This decorator check if the request is an AJAX request, useful decorator when we are working with Javascript frameworks as jQuery and a good way to try to secure our application
```
from django.http import HttpResponseBadRequest


def ajax_required(f):
   """
   AJAX request required decorator
   use it in your views:

   @ajax_required
   def my_view(request):
       ....

   """   

   def wrap(request, *args, **kwargs):
       if not request.is_ajax():
           return HttpResponseBadRequest()
       return f(request, *args, **kwargs)

   wrap.__doc__=f.__doc__
   wrap.__name__=f.__name__
   return wrap


# The way to use this decorator is:
@ajax_required
def my_view(request):
    ...
```
#### @timeit

This decorator is very helpful if you need to improve the response time of one of then our views or if you just want to know how long it takes to run.
```
def timeit(method):

   def timed(*args, **kw):
       ts = time.time()
       result = method(*args, **kw)
       te = time.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result

   return timed


# The way to use this decorator is:
@timeit
def my_view(request):
    ...

```
