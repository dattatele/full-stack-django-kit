==============
Configurations
==============


Production
----------
Force SSL traffic
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

request.META
'REMOTE_ADDR': '10.0.2.2',
'X-Forwarded-For': '10.0.2.2',
'X-Real-IP': '10.0.2.2'