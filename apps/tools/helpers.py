from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import requests

USER_TYPE = (
    ("Driver", 'Driver'),
    ("Client", 'Client'),
    ("Company", 'Company'),

    ("Administrator", 'Administrator'),
    ('SuperAdmin', 'SuperAdmin')
)

USER_STATUS = (
    ("Active", 'Active'),
    ('Passive', 'Passive'),
    ('Waiting', 'Waiting'),
    ('Edit', 'Edit'),
    ('Fail', 'Fail'),
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def send_sms(phone, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ5OTE2ODMsImlhdCI6MTcxMjM5OTY4Mywicm9sZSI6InVzZXIiLCJzaWduIjoiNTQzOWFkYzQyMzVjYjNjZDIwMzNlZmIwOTFiYzg2NzI4NDIyNzA5NDcxNGM0NmRmOTc3MTNiOTM4ZjVkYmNjYiIsInN1YiI6IjEwNTMifQ.CT_JbuU5UXaxhpuPQVgyCTbL_sFWuFdgNHQYTIV4pX4"}
    data = {
        'mobile_phone': phone,
        'message': message,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }
    response = requests.post(url=url, data=data, headers=headers)
    return response
