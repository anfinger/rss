from django.contrib import admin
from .models import Reise, Tag, Reisetage, ReisetageInline

class TagAdmin(admin.ModelAdmin):
    inlines = (ReisetageInline,)

class ReiseAdmin(admin.ModelAdmin):
    inlines = (ReisetageInline,)

admin.site.register(Reise, ReiseAdmin)
admin.site.register(Tag, TagAdmin)
