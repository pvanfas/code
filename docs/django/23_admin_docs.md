
Django’s [`admindocs`](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/admindocs/#module-django.contrib.admindocs "django.contrib.admindocs: Django's admin documentation generator.") app pulls documentation from the docstrings of models, views, template tags, and template filters for any app in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-INSTALLED_APPS) and makes that documentation available from the [`Django  admin`](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#module-django.contrib.admin "django.contrib.admin: Django's admin site.").

To activate the  [`admindocs`](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/admindocs/#module-django.contrib.admindocs "django.contrib.admindocs: Django's admin documentation generator."), you will need to do the following:

-   Add  `django.contrib.admindocs`  to your  [`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-INSTALLED_APPS).
-   Add `path('admin/doc/',include('django.contrib.admindocs.urls')),`  to your  `urlpatterns`. Make sure it’s included  _before_  the  `'admin/'`  entry, so that requests to  `/admin/doc/`  don’t get handled by the latter entry.
-   Install the docutils Python module ([https://docutils.sourceforge.io/](https://docutils.sourceforge.io/)). `python -m pip install docutils`
-   **Optional:**  Using the admindocs bookmarklets requires  `django.contrib.admindocs.middleware.XViewMiddleware`  to be installed.

Once those steps are complete, you can start browsing the documentation by going to your admin interface and clicking the “Documentation” link in the upper right of the page.