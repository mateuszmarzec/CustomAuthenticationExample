from django.contrib import admin

from App.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
