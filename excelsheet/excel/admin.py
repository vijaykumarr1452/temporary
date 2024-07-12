from django.contrib import admin

# Register your models here.

from . models import Person

from import_export.admin import ImportExportModelAdmin

admin.site.register(Person,ImportExportModelAdmin)