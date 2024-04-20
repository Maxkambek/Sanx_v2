from django.contrib import admin

from apps.main.models import Region, Catalog, UserFiles, Subscription, Notification, Story, PaymentType, Currency, \
    CarWeightType, \
    CarType, CarBrand, CarMark, Color, TransportInformation


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'region_type', 'parent_id')


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id')


@admin.register(UserFiles)
class UserFilesAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ["name", 'order_on']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(CarWeightType)
class CarWeightTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'note', 'weight_max', 'status']


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_weight_type_id', 'status']


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_type_id', 'status']


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_brand_id', 'status']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'status']
