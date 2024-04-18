from django.contrib import admin

from apps.main.models import Region, Catalog, UserFiles, Subscription, Notification, Story, PaymentType, Currency, \
    CarWeightType, \
    CarType, CarBrand, CarMark, Color, TransportInformation


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'region_type', 'parent_id')


admin.site.register(Region, RegionAdmin)
admin.site.register(Catalog)
admin.site.register(UserFiles)
admin.site.register(Subscription)
admin.site.register(Notification)
admin.site.register(PaymentType)
admin.site.register(Currency)
admin.site.register(Story)
admin.site.register(CarWeightType)
admin.site.register(CarType)
admin.site.register(CarBrand)
admin.site.register(CarMark)
admin.site.register(Color)
admin.site.register(TransportInformation)
