from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model

class CustomUserTestCase(TestCase):

    #@override_settings(AUTH_USER_MODEL='users.User')
    def test_custom_user(self):
        user_model = get_user_model()
        # user states
        # registered without email validation
        # registered and active (email validated)
        # registered and not active (canceled)
        # user type
        # admin, staff, auditor, publisher, author, etc.
        pass

