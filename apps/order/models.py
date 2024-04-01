from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=123)
    catalog_id = models.PositiveIntegerField()
    order_type = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    prepaid = models.DecimalField(max_digits=20, decimal_places=2)
    currency_id = models.PositiveIntegerField()
    payment_type_id = models.PositiveIntegerField()
    from_region_id = models.PositiveIntegerField()
    to_region_id = models.PositiveIntegerField()
    from_address = models.CharField(max_length=223)
    to_address = models.CharField(max_length=223)
    transport_type_id = models.PositiveIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    brutto = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)
    transport_document_id = models.PositiveIntegerField()
    region_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.PositiveIntegerField()


class TransportDocument(models.Model):
    name = models.CharField(max_length=123)
    order_on = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order_id = models.PositiveIntegerField()
    order_item_type = models.CharField(max_length=123)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    prepaid = models.DecimalField(max_digits=20, decimal_places=2)
    currency_id = models.PositiveIntegerField()
    payment_type_id = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    brutto = models.DecimalField(max_digits=20, decimal_places=2)
    status_id = models.PositiveIntegerField()
    owner_id = models.PositiveIntegerField()
    executor_id = models.PositiveIntegerField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()


class Payment(models.Model):
    from_id = models.PositiveIntegerField()
    to_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    order_item_id = models.PositiveIntegerField()
    payment_type_id = models.PositiveIntegerField()
    status = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()


class Transaction(models.Model):
    from_id = models.PositiveIntegerField()
    to_id = models.PositiveIntegerField()
    payment_id = models.PositiveIntegerField()
    order_item_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()


class OrderApplicant(models.Model):
    order_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    note = models.TextField()
    status = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()


class OrderStatus(models.Model):
    name = models.CharField(max_length=123)
    order_on = models.PositiveIntegerField()
    change_allow_status = models.CharField(max_length=123)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderView(models.Model):
    order_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    order_item_id = models.PositiveIntegerField()
    one_id = models.PositiveIntegerField()
    two_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat_id = models.PositiveIntegerField()
    from_id = models.PositiveIntegerField()
    to_id = models.PositiveIntegerField()
    is_read = models.BooleanField(default=False)
    read_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)