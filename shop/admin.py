from django.contrib import admin

from shop.models import RegisterModel, LoginModel


@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'password', 'created_at')
    search_fields = ('first_name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
