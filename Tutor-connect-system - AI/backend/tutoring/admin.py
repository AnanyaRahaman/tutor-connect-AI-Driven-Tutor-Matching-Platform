from django.contrib import admin
from .models import TuitionRequest


class TuitionRequestAdmin(admin.ModelAdmin):

    list_display = ("subject", "location", "date", "time", "method")


admin.site.register(TuitionRequest, TuitionRequestAdmin)