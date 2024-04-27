from rest_framework import serializers
from ..models import Order, TransportDocument, OrderItem, Payment, Transaction, OrderApplicant, OrderStatus, OrderView, \
    Chat, Message, OrderFiles
from ...adminstration.serializers import AccountSerializer
from ...main.v1.serializers import CatalogSerializer, CurrencySerializer, PaymentTypeSerializer, RegionSerializer, \
    CarTypeSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'name',
            'catalog_id',
            'order_type',
            'price',
            'prepaid',
            'currency_id',
            'payment_type_id',
            'from_region_id',
            'to_region_id',
            'from_address',
            'to_address',
            'transport_type_id',
            'upload_date',
            'weight',
            'brutto',
            'volume',
            'transport_document_id',
            'region_id',
            'status_id',
            'note',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ]


class OrderFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFiles
        fields = [
            'order',
            'file'
        ]


class TransportDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportDocument
        fields = [
            'id',
            'name',
            'order_on',
            'status',
            'created_at',
            'updated_at'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'order_id',
            'order_item_type',
            'price',
            'prepaid',
            'currency_id',
            'payment_type_id',
            'weight',
            'brutto',
            'status_id',
            'owner_id',
            'executor_id',
            'note',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'from_id',
            'to_id',
            'price',
            'order_item_id',
            'payment_type_id',
            'status',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by'
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'from_id',
            'to_id',
            'payment_id',
            'order_item_id',
            'price',
            'created_at',
            'created_by'
        ]


class OrderApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderApplicant
        fields = [
            'id',
            'order_id',
            'user_id',
            'note',
            'status',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = [
            'id',
            'name',
            'order_on',
            'change_allow_status',
            'status',
            'created_at',
            'updated_at'
        ]


class OrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderView
        fields = [
            'id',
            'order_id',
            'user_id',
            'is_liked',
            'created_at',
            'updated_at',
        ]


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id',
            'order_item_id',
            'one_id',
            'two_id',
            'created_at'
        ]


class ChatListSerializer(serializers.ModelSerializer):
    one_id = AccountSerializer(many=False)
    two_id = AccountSerializer(many=False)
    order_item_id = OrderItemSerializer(many=False)

    class Meta:
        model = Chat
        fields = [
            'id',
            'order_item_id',
            'one_id',
            'two_id',
            'created_at'
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'chat_id',
            'from_id',
            'to_id',
            'is_read',
            'read_time',
            'created_at',
            'message_text',
            "message_file",
            'type_message'
        ]


class MessageListSerializer(serializers.ModelSerializer):
    chat_id = ChatSerializer(many=False)
    from_id = AccountSerializer(many=False)
    to_id = AccountSerializer(many=False)

    class Meta:
        model = Message
        fields = [
            'id',
            'chat_id',
            'from_id',
            'to_id',
            'is_read',
            'read_time',
            'created_at',
            'message_text',
            "message_file",
            'type_message'
        ]


class OrderListSerializer(serializers.ModelSerializer):
    catalog_id = CatalogSerializer(many=False)
    currency_id = CurrencySerializer(many=False)
    payment_type_id = PaymentTypeSerializer(many=False)
    from_region_id = RegionSerializer(many=False)
    to_region_id = RegionSerializer(many=False)
    transport_type_id = CarTypeSerializer(many=False)
    transport_document_id = TransportDocumentSerializer(many=False)
    region_id = RegionSerializer(many=False)
    status_id = OrderStatusSerializer(many=False)
    created_by = AccountSerializer(many=False)
    order_files = OrderFilesSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'name',
            'catalog_id',
            'order_type',
            'price',
            'prepaid',
            'currency_id',
            'payment_type_id',
            'from_region_id',
            'to_region_id',
            'from_address',
            'to_address',
            'transport_type_id',
            'upload_date',
            'weight',
            'brutto',
            'volume',
            'transport_document_id',
            'region_id',
            'status_id',
            'note',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
            'order_files'
        ]


class OrderApplicantListSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer(many=False)
    user_id = AccountSerializer(many=False)
    created_by = AccountSerializer(many=False)

    class Meta:
        model = OrderApplicant
        fields = [
            'id',
            'order_id',
            'user_id',
            'note',
            'status',
            'created_at',
            'created_by'
        ]
