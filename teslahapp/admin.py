
from django.contrib import admin
from .models import prestation,publication,commentaire,image_publication


#-----------------------------------------------------------------------------------------------
class prestationInline(admin.StackedInline):
    model=prestation
    can_delete = False
    verbose_name_plural = 'prestations'

@admin.register(prestation)
class prestationAdmin(admin.ModelAdmin):
    list_display = ('client','num_telephone', 'Adress', 'Service','Description','Date')
    list_filter = ('num_telephone', 'Adress', 'Service', 'Description')
    search_fields = ['num_telephone']

class publicationInline(admin.StackedInline):
    model=publication
    can_delete = False
    verbose_name_plural = 'publications'

class image_publicationInline(admin.StackedInline):
    model=image_publication


@admin.register(publication)
class publicationAdmin(admin.ModelAdmin):
    list_display = ('prestataire','Description', 'photos','Lieu','Date_pub')
    inlines=[image_publicationInline]
    class Meta:
        model = publication

@admin.register(image_publication)
class image_publicationAdmin(admin.ModelAdmin):
    pass

class commentaireInline(admin.StackedInline):
    model=publication
    can_delete = False
    verbose_name_plural = 'commentaires'

@admin.register(commentaire)
class commentaireAdmin(admin.ModelAdmin):
    list_display = ('client','Comment', 'date_comments','publi')
#------------------------------------------------------------------------------------------------