# Default template tags
{{instance.date|date:"d/m/Y"}}

# Custom template tags
    mkdir main/templatetags/
    touch main_template_tags.py __init__.py

    # on main_template_tags.py
    @register.filter
    def to_fixed_to(value):
        return "{:10.2f}".format(value)

# on required template
{% load main_template_tags %}

{{instance.date|to_fixed_to}}
