from django.contrib import admin
from .models import *

class GeneAttributeInline(admin.TabularInline):
    model = GeneAttributeLink
    extra = 3

class GeneAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity', 'start', 'stop', 'sense')
    inlines = [GeneAttributeInline]
    
class ECAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ec_name')
    
class SequencingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sequencing_factory', 'factory_location')
    
admin.site.register(Gene, GeneAdmin)
admin.site.register(EC, ECAdmin)
admin.site.register(Sequencing, SequencingAdmin)
    

