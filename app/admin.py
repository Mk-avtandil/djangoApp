from django.contrib import admin

from .models import Marvel


class MarvelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ability', 'gender')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Marvel, MarvelAdmin)
