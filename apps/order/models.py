from django.db import models
from apps.main.models import Region, PaymentType, Currency, Catalog, CarType
from apps.my_auth.models import Account


class TransportDocument(models.Model):
    name = models.CharField(max_length=123)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name = models.CharField(max_length=123)
    order_on = models.PositiveIntegerField()
    change_allow_status = models.CharField(max_length=123)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_TYPE_CHOICES = (
        ('Order', 'Order'),
        ('Driver', 'Driver')
    )
    name = models.CharField(max_length=123)
    catalog_id = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True, blank=True)
    order_type = models.CharField(max_length=123, choices=ORDER_TYPE_CHOICES, default='Order')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    prepaid = models.DecimalField(max_digits=20, decimal_places=2)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    from_region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='from_region')
    to_region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='to_region')
    from_address = models.CharField(max_length=223)
    to_address = models.CharField(max_length=223)
    transport_type_id = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    brutto = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    transport_document_id = models.ForeignKey(TransportDocument, on_delete=models.CASCADE,
                                              related_name='transport_documents')
    region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='order_region')
    status_id = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, related_name="order_status", default='Active')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='order_owner')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='order_updated_by')
    latitude = models.DecimalField(max_digits=20, decimal_places=12, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=12, null=True)

    def __str__(self):
        return self.name


class OrderFiles(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_files')
    file = models.FileField(upload_to='order_files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.name


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    order_item_type = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    prepaid = models.DecimalField(max_digits=20, decimal_places=2)
    currency_id = models.PositiveIntegerField()
    payment_type_id = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    brutto = models.DecimalField(max_digits=20, decimal_places=2)
    status_id = models.PositiveIntegerField()
    owner_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner_id')
    executor_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='executor_id')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()


class Payment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Waiting', 'Waiting'),
        ('Approved', 'Approved'),
    )
    from_id = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='payment_from_id', null=True)
    to_id = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='payment_to_id', null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, related_name='payment_item_id')
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True,
                                        related_name='payment_payment_type_id')
    status = models.CharField(max_length=123, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()


class Transaction(models.Model):
    from_id = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='from_transaction_id', null=True)
    to_id = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='to_transaction_id', null=True)
    payment_id = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, related_name="payment_transaction_id")
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True,
                                      related_name="order_transaction_id")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='transaction_created_by')


class OrderApplicant(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('OwnerCancelled', 'OwnerCancelled'),
        ('InvitedCancelled', 'InvitedCancelled'),
        ('Accepted', 'Accepted'),
    )
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_applicant')
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_id')
    note = models.TextField()
    status = models.CharField(max_length=123, choices=STATUS_CHOICES, default="New")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='order_applicant_created_by')
    updated_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,
                                   related_name='order_applicant_updated_by')


class OrderView(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="order_view")
    user_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="order_view_user_id")
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, related_name="chat_item")
    one_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='chat_one_id')
    two_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='chat_two_id')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    TYPE_MESSAGE = (
        ('Text', 'Text'),
        ('Image', 'Image'),
        ('Video', 'Video'),
        ('Audio', 'Audio'),
    )
    type_message = models.CharField(max_length=123)
    chat_id = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, related_name='chat_id')
    from_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='from_id')
    to_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='to_id')
    is_read = models.BooleanField(default=False)
    read_time = models.DateTimeField()
    message_text = models.TextField(null=True, blank=True)
    message_file = models.FileField(upload_to='message_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
