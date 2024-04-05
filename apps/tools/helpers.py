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


#
# def send_auth_code(phone, code):
#     verification_code = str(randint(10000, 100000))
#     result = send_sms(phone, f'Tadiqlash kodingiz: {code}')
#     VerifyCode.objects.create(phone=phone, code=verification_code)
#     return result


def send_sms(phone, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEwMTg0MzUsImlhdCI6MTcwODQyNjQzNSwicm9sZSI6InVzZXIiLCJzaWduIjoiMjMzNWM0NDdjZjRiMmVjNjI1ODFkZTkyMTljODI3NjM0Y2VhYmVjOWU5Yzg3ZjRhMjVmNzU0ZjU0OTA2MzIwNCIsInN1YiI6IjQyNDcifQ.gqD09z2NF8iBWsM6wTiI87PLzHUZba8xbN90sKO8Ow4"}
    data = {
        'mobile_phone': phone,
        'message': message,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }
    response = requests.post(url=url, data=data, headers=headers)
    return response


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
