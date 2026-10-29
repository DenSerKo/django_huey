from django.contrib import admin

from apps.core.models import DemoJob


@admin.register(DemoJob)
class DemoJobAdmin(admin.ModelAdmin):
    pass