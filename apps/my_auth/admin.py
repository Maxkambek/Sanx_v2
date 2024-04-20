from django.contrib import admin

from apps.my_auth.models import Account, VerifyCode


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'first_name', 'is_active')


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'code']
