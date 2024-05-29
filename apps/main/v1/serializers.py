from rest_framework import serializers
from ..models import Region, Catalog, UserFiles, Subscription, Notification, Story, PaymentType, Currency, \
    CarWeightType, CarType, CarBrand, CarMark, Color, TransportInformation, UserRating


class UserRatingCreateSerializer(serializers.ModelSerializer):
    rate = serializers.BooleanField()

    class Meta:
        model = UserRating
        fields = [
            'user_id',
            'rate'
        ]


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = [
            'user_id',
            'positive',
            'negative'
        ]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id',
            'name',
            'flag',
            'parent_id',
            'region_type',
            'order_on',
            'status',
            'created_at',
            'updated_at'
        ]


class RegionFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id',
            'name',
            'flag',
        ]


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            'id',
            'name',
            'parent_id',
            'order_on',
            'status',
            'created_at',
            'updated_at',
            'type_catalog'
        ]


class CatalogFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            'id',
            'name',
        ]


class UserFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFiles
        fields = [
            'id',
            'user_id',
            'file_type',
            'file_url',
            'order_on',
            'created_at'
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'id',
            'watcher_id',
            'user_id',
            'created_at'
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'user_id',
            'message_type',
            'message',
            'is_read',
            'read_time',
            'source_table',
            'source_id',
            'created_at',
            'created_by'
        ]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'id',
            'user_id',
            'created_at',
            'story_type',
            'file_url'
        ]


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            'id',
            'name',
            'order_on',
            'status',
            'created_at',
            'updated_at'
        ]


class PaymentTypeFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            'id',
            'name',
        ]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'id',
            'name',
            'code',
            'created_at',
            'updated_at',
            'order_on',
            'status'
        ]


class CurrencyFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'id',
            'name',
        ]


class CarWeightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWeightType
        fields = [
            'id',
            'name',
            'order_on',
            'note',
            'weight_max',
            'status',
            'created_at',
            'updated_at'
        ]


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = [
            'id',
            'car_weight_type_id',
            'name',
            'order_on',
            'photo_url',
            'note',
            'status',
            'created_at',
            'updated_at'
        ]


class CarTypeFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = [
            'id',
            'name',
        ]


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = [
            'id',
            'name',
            'logo_url',
            'car_type_id',
            'status',
            'created_at',
            'updated_at'
        ]


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = [
            'id',
            'car_brand_id',
            'name',
            'status',
            'order_on',
            'created_at',
            'updated_at'
        ]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'name',
            'code',
            'order_on',
            'status',
            'created_at',
            'updated_at'
        ]


class TransportInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportInformation
        fields = [
            'id',
            'passport_type',
            'passport',
            'passport_expiration',
            'driver_license',
            'passport_back',
            'passport_with_face',
            'payment_type_id',
            'car_weight_type_id',
            'car_mark_id',
            'car_type_id',
            'color_id',
            'created_at',
            'updated_at'
        ]
