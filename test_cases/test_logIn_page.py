
import time

from seleniumbase import BaseCase

class LogIn_Page(BaseCase):
    def setUp(self):
        super().setUp()
        print("Everything Zimbabwean, Test has been triggered")

        # open url & maximize
        url = "https://everythingzimbabwean.com/"
        self.open(url)
        self.maximize_window()

    def tearDown(self):
        print("Running after each test")
        super().tearDown()

    def test_invalid_username(self):
        # logIn details
        self.click("")
        time.sleep(2)
        self.send_keys("//input[@name='username']", "")
        self.send_keys("//input[@id='password']", "123456789Qaz@")
        time.sleep(2)
        self.click("//button[@name='login']")

    def test_invalid_password(self):
        # logIn details
        self.click("")
        time.sleep(2)
        self.send_keys("//input[@name='username']", "nicksongwe@gmail.com")
        self.send_keys("//input[@id='password']", "")
        time.sleep(2)
        self.click("//button[@name='login']")

    def test_invalid_logins(self):
        # logIn details
        self.click("")
        time.sleep(2)
        self.send_keys("//input[@name='username']", " ")
        self.send_keys("//input[@id='password']", " ")
        time.sleep(2)
        self.click("//button[@name='login']")

    def test_valid_logins(self):
        # logIn details
        self.click("")
        time.sleep(2)
        self.send_keys("//input[@name='username']", "nicksongwe@gmail.com")
        self.send_keys("//input[@id='password']", "123456789Qaz@")
        time.sleep(2)
        self.click("//button[@name='login']")





