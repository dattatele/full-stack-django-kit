from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.core.urlresolvers import reverse

class UserRegistrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(UserRegistrationTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UserRegistrationTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('users-register')))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('brady@vitrano.me')
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys('secret')
        password_input = self.selenium.find_element_by_name("password2")
        password_input.send_keys('secret')
        #self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()