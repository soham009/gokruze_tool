from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from leads.models import Leads, CustomUser
from django.contrib.auth.models import Group

class LeadsAdmin(ImportExportModelAdmin):
    class Meta:
        model = Leads

admin.site.register(Leads, LeadsAdmin)
admin.site.register(CustomUser)