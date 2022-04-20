from __future__ import unicode_literals
from django.contrib import admin
from .models import Blog
from django.contrib.auth.models import User, Group

# To remove user,groups from admin panel
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    actions = [mark_active, mark_inactive]
    list_display = ("title", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")
    list_filter = ("title", "author")
    ordering = "timestamp"
    exclude = None
    readonly_fields = ("auto_id",)
    autocomplete_fields = ("author",)
    search_fields = (
        "title",
        "author__name",
    )

    
# For import_export action
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Registration)
class RegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ("full_name", "phone_number")


# Custom Admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages
from django.utils.translation import ngettext


def mark_active(self, request, queryset):
    updated = queryset.update(is_active=True)
    self.message_user(
        request,
        ngettext(
            "%d object was successfully marked as active.",
            "%d objects were successfully marked as active.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


def mark_inactive(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(
        request,
        ngettext(
            "%d object was successfully marked as inactive.",
            "%d objects were successfully marked as inactive.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


class CustomAdmin(ImportExportModelAdmin):
    exclude = ["creator", "is_active"]
    list_display = ("__str__", "created", "updated", "is_deleted")
    list_filter = ("is_active",)
    actions = [mark_active, mark_deleted]
    readonly_fields = ("is_active",)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

        
