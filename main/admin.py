from django.contrib import admin

from .models import Bimbo


class TimbroAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nickname']

    class Meta:
        model = Bimbo


admin.site.register(Bimbo, TimbroAdmin)
