from __future__ import unicode_literals
from django.contrib import admin
from .models import Blog
from django.contrib.auth.models import User, Group

# For custom admin actions
from django.contrib import messages
from django.utils.translation import ngettext


def mark_active(self, request, queryset):
    updated = queryset.update(is_active=True)
    self.message_user(request, ngettext(
        '%d object was successfully marked as active.',
        '%d objects were successfully marked as active.',
        updated,
    ) % updated, messages.SUCCESS)

def mark_inactive(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(request, ngettext(
        '%d object was successfully marked as inactive.',
        '%d objects were successfully marked as inactive.',
        updated,
    ) % updated, messages.SUCCESS)

    
# To remove user,groups from admin panel
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    actions = [mark_active,mark_inactive]
    list_display = ('title','is_active')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','author')
    list_filter = ('title','author')
    ordering = ('timestamp')
    exclude = None
    readonly_fields = ('auto_id',)
    autocomplete_fields = ('author',)
    search_fields = ('title', 'author__name',)

  
admin.site.site_header = "PROJECT Administration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Admin Portal"