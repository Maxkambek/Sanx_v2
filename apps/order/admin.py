from django.contrib import admin

from apps.order.models import Order, TransportDocument, OrderItem, Payment, Transaction, OrderView, OrderStatus, OrderApplicant, \
    Chat, Message

admin.site.register(Order)
admin.site.register(TransportDocument)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Transaction)
admin.site.register(OrderView)
admin.site.register(OrderStatus)
admin.site.register(OrderApplicant)
admin.site.register(Chat)
admin.site.register(Message)
