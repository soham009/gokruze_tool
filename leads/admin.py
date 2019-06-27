from django.contrib import admin
from leads.models import Leads
from django.contrib.auth.models import Group

admin.site.register(Leads)
admin.site.unregister(Group)
# Register your models here.
