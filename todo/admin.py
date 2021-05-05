from django.contrib import admin
from .models import ToDo

class ToDOAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt',)

admin.site.register(ToDo, ToDOAdmin)
