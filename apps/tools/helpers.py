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


def send_sms(phone, code):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEwMTg0MzUsImlhdCI6MTcwODQyNjQzNSwicm9sZSI6InVzZXIiLCJzaWduIjoiMjMzNWM0NDdjZjRiMmVjNjI1ODFkZTkyMTljODI3NjM0Y2VhYmVjOWU5Yzg3ZjRhMjVmNzU0ZjU0OTA2MzIwNCIsInN1YiI6IjQyNDcifQ.gqD09z2NF8iBWsM6wTiI87PLzHUZba8xbN90sKO8Ow4"}
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }

    response = requests.post(url=url, data=data, headers=headers)
    return response
