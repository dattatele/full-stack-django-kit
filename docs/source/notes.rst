Notes
+++++

Force SSL traffic

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

Available Headers from Nginx via ``request.META``
request.META
'REMOTE_ADDR': '10.0.2.2',
'X-Forwarded-For': '10.0.2.2',
'X-Real-IP': '10.0.2.2'

