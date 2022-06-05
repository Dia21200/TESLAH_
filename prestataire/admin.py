from django.contrib import admin
from django.contrib.auth.models import User
from .models import prestataire
from django.contrib.auth.admin import UserAdmin


class prestataireInline(admin.StackedInline):
    model=prestataire
    can_delete = False
    verbose_name_plural = 'prestataires'

"""class CustomizedUserAdmin(UserAdmin):
    inlines = (prestataireInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
"""

@admin.register(prestataire)
class prestataireAdmin(admin.ModelAdmin):
    list_display = ('nom','user','Specialite','adresse', 'gender', 'date_naissance','annee_experience','NNI','cv','Date_inscription')
