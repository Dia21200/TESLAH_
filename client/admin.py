from django.contrib import admin
from django.contrib.auth.models import User
from .models import client
from django.contrib.auth.admin import UserAdmin

#admin.site.register(pub)

class clientInline(admin.StackedInline):
    model=client
    can_delete = False
    verbose_name_plural = 'clients'

"""class CustomizedUserAdmin(UserAdmin):
    inlines = (clientInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
"""


@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    list_display = ('nom','user','adresse','date_naissance','gender','Date_inscription')




