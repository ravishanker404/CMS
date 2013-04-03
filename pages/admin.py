from django.contrib import admin
from pages.models import MultiPage, MultiPageContent, StaticPage 


class MultiPageAdmin(admin.ModelAdmin):
    list_display = ('page_name',)

class MultiPageContentAdmin(admin.ModelAdmin):
    list_display = ('title',)

class StaticpageAdmin(admin.ModelAdmin):
    list_display = ('page_name',)


#admin.site.register(MultiPage, MultiPageAdmin)
admin.site.register(StaticPage)
admin.site.register(MultiPage, MultiPageAdmin)
admin.site.register(MultiPageContent)