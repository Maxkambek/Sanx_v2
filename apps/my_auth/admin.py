from django.contrib import admin

from apps.my_auth.models import Account, VerifyCode

admin.site.register(Account)
admin.site.register(VerifyCode)
