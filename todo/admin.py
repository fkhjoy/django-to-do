from django.contrib import admin
from .models import Todo

class TodOAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt',)

admin.site.register(Todo, TodOAdmin)
