import firebase_admin
from django.http import HttpResponse
from firebase_admin import messaging


def send_notification(device_tokens, title, body):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(title=title, body=body),
        tokens=device_tokens
    )

    response = messaging.send_multicast(message)

    success_count = response.success_count
    failure_count = response.failure_count


def send_notifications(request):
    device_tokens = ['device_token_1', 'device_token_2']
    send_notification(device_tokens, 'Notification Title', 'Notification Body')
    return HttpResponse('Notifications sent')
