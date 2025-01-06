from api.models import Task
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    list_filter = [
        "owner__username",
        "task_type",
        "is_complete",
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # default to current user
        if db_field.name == "owner":
            kwargs["initial"] = request.user.id
            return db_field.formfield(**kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)
