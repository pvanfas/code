#add/change admin logo

open venv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/base_site.html

```
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">
        <img src="{% static 'umsra_logo.png' %}" height="40px" />
    </a>
</h1>
```