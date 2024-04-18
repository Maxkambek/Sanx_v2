from django.db import models

from apps.tools.helpers import REGION_TYPE, CATALOG_TYPE, STORY_TYPE


class Region(models.Model):
    name = models.CharField(max_length=123)
    flag = models.FileField(upload_to='regions/')
    parent_id = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    region_type = models.CharField(max_length=123, choices=REGION_TYPE)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(max_length=123)
    parent_id = models.PositiveIntegerField(null=True, blank=True)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    type_catalog = models.CharField(max_length=123, choices=CATALOG_TYPE, default='First')
    updated_at = models.DateTimeField(auto_now=True)


class UserFiles(models.Model):
    user_id = models.PositiveIntegerField()
    file_type = models.CharField(max_length=123)
    file_url = models.FileField(upload_to='user/files')
    order_on = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    watcher_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user_id = models.PositiveIntegerField()
    message_type = models.CharField(max_length=123)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    read_time = models.DateTimeField(auto_now_add=True)
    source_table = models.CharField(max_length=123)
    source_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()


class Story(models.Model):
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    story_type = models.CharField(max_length=123, choices=STORY_TYPE, default='Video')
    file_url = models.FileField(upload_to='user/story')


class PaymentType(models.Model):
    name = models.CharField(max_length=123)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Currency(models.Model):
    name = models.CharField(max_length=123)
    code = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)


class CarWeightType(models.Model):
    name = models.CharField(max_length=222)
    order_on = models.PositiveIntegerField()
    note = models.TextField()
    weight_max = models.FloatField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CarType(models.Model):
    car_weight_type_id = models.PositiveIntegerField()
    name = models.CharField(max_length=222)
    order_on = models.PositiveIntegerField()
    photo_url = models.FileField(upload_to='car_type/')
    note = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CarBrand(models.Model):
    name = models.CharField(max_length=222)
    logo_url = models.FileField(upload_to='car_brand/')
    car_type_id = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CarMark(models.Model):
    car_brand_id = models.PositiveIntegerField()
    name = models.CharField(max_length=222)
    status = models.BooleanField(default=False)
    order_on = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Color(models.Model):
    name = models.CharField(max_length=222)
    code = models.CharField(max_length=222)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TransportInformation(models.Model):
    user_id = models.PositiveIntegerField()

    passport_type = models.CharField(max_length=222)
    passport = models.FileField(upload_to='passport/')
    passport_expiration = models.DateField()

    driver_license = models.FileField(upload_to='driver_license/')

    payment_type_id = models.PositiveIntegerField()
    car_weight_type_id = models.PositiveIntegerField()
    car_mark_id = models.PositiveIntegerField()
    car_type_id = models.PositiveIntegerField()
    color_id = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
