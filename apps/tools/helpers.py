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

REGION_TYPE = (
    ("Continent", 'Continent'),
    ("Country", 'Country'),
    ("District", 'District'),
)

CATALOG_TYPE = (
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
)

USER_STATUS = (
    ("Active", 'Active'),
    ('Passive', 'Passive'),
    ('Waiting', 'Waiting'),
    ('Edit', 'Edit'),
    ('Fail', 'Fail'),
)

STORY_TYPE = (
    ('Video', 'Video'),
    ('Audio', 'Audio'),
    ('Image', 'Image'),
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

USER_FILES_TYPE = (
    ('CLIENT')
)

def send_sms(phone, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc5MTUyMjksImlhdCI6MTcxNTMyMzIyOSwicm9sZSI6InVzZXIiLCJzaWduIjoiMjMzNWM0NDdjZjRiMmVjNjI1ODFkZTkyMTljODI3NjM0Y2VhYmVjOWU5Yzg3ZjRhMjVmNzU0ZjU0OTA2MzIwNCIsInN1YiI6IjQyNDcifQ.6zTPTsgxb6yRngLLqWFO7eBzaOxMrukVy5Uzn78N30E"}
    data = {
        'mobile_phone': phone,
        'message': message,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }
    response = requests.post(url=url, data=data, headers=headers)
    return response
