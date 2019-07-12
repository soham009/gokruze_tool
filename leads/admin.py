from django.contrib import admin
from leads.models import Leads, CustomUser
from django.contrib.auth.models import Group

admin.site.register(Leads)
admin.site.register(CustomUser)
# Register your models here.
