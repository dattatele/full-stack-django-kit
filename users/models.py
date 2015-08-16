from django.contrib.auth.models import AbstractUser
from django.core import signing
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


class User(AbstractUser):

    def send_confirmation_email(self, request=None):
        from django.template.loader import get_template
        signer = signing.Signer()
        signed_value = signer.sign(self.email)
        template = get_template('emails/confirm-email.html')

        self.email_user('Email Confirmation', '',
                        from_email='donotreply@example.com',
                        html_message=template.render({
                            'request': request,
                            'code': reverse('confirm-email', args=(signed_value,))
                        }))




