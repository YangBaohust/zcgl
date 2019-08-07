from django.contrib import admin

from .models import Server, ServerType


class ServerAdmin(admin.ModelAdmin):
    pass


class ServerTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Server, ServerAdmin)
admin.site.register(ServerType, ServerTypeAdmin)
