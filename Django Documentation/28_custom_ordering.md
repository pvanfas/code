## Custom Ordering in Django Admin

When we register the models django automatically sorts apps by lexicographic order. But, we can do some hacks to order models and apps as we want.

1. Append below code in ```settings.py```
```
APP_ORDER = OrderedDict([
  ("app", ["Settings", "Vendor"]),
  ("web", ["Slider", "Category", "Subcategory","Product", "Order", "BulkOrder", "ServiceOrder", "Contact"]),
])
```
2. Now add a template tag which will create the order ```templatetags/tags.py```
```
from django import template
from django.conf import settings


register = template.Library()


def pop_and_get_app(apps, key, app_label):
	for index, app in enumerate(apps):
		if app[key] == app_label:
			obj = apps.pop(index)
			return obj
	return None


@register.filter
def sort_apps(apps):
	new_apps = []
	order = settings.APP_ORDER
	for app_label in order.keys():
		obj = pop_and_get_app(apps, "app_label", app_label)
		new_apps.append(obj) if obj else None
	apps = new_apps + apps
	for app in apps:
		models = app.get("models")
		app_label = app.get("app_label")
		new_models = []
		order_models = settings.APP_ORDER.get(app_label, [])
		for model in order_models:
			obj = pop_and_get_app(models, "object_name", model)
			new_models.append(obj) if obj else None
		models = new_models + models
		app["models"] = models
	return apps
```
3. override the django template ```templates/admin/app_list.html```

```
{% load i18n tags %}

{% if app_list %}
  {% for app in app_list|sort_apps %}
    <div class="app-{{ app.app_label }} module{% if app.app_url in request.path %} current-app{% endif %}">
      <table>
        <caption>
          <a href="{{ app.app_url }}" class="section" title="{% blocktranslate with name=app.name %}Models in the {{ name }} application{% endblocktranslate %}">{{ app.name }}</a>
        </caption>
        {% for model in app.models %}
          <tr class="model-{{ model.object_name|lower }}{% if model.admin_url in request.path %} current-model{% endif %}">
            {% if model.admin_url %}
              <th scope="row"><a href="{{ model.admin_url }}"{% if model.admin_url in request.path %} aria-current="page"{% endif %}>{{ model.name }}</a></th>
            {% else %}
              <th scope="row">{{ model.name }}</th>
            {% endif %}

            {% if model.add_url %}
              <td><a href="{{ model.add_url }}" class="addlink">{% translate 'Add' %}</a></td>
            {% else %}
              <td></td>
            {% endif %}

            {% if model.admin_url and show_changelinks %}
              {% if model.view_only %}
                <td><a href="{{ model.admin_url }}" class="viewlink">{% translate 'View' %}</a></td>
              {% else %}
                <td><a href="{{ model.admin_url }}" class="changelink">{% translate 'Change' %}</a></td>
              {% endif %}
            {% elif show_changelinks %}
              <td></td>
            {% endif %}
          </tr>
        {% endfor %}
      </table>
    </div>
  {% endfor %}
{% else %}
  <p>{% translate 'You don’t have permission to view or edit anything.' %}</p>
{% endif %}
```