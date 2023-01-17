import time

from seleniumbase import BaseCase


class Register_LogIn(BaseCase):
    def setUp(self):
        super().setUp()
        print("Everything Zimbabwean, Your one stop shop, Running Before Each Test")

        # open url & maximize page
        url = "https://everythingzimbabwean.com/my-account/?login=register"
        self.open(url)
        self.maximize_window()

    def tearDown(self):
        print("Everything Zimbabwean, Running after each test")
        super().tearDown()

    def test_home_page(self):
        # assert page title
        self.assert_title("My account - Everything Zimbabwean")
        # get url & assert
        url = self.get_current_url()
        self.assert_equal(url, "https://everythingzimbabwean.com/my-account/?login=register")

    def test_register_page(self):
        self.scroll_to_element("//div[@id='continue-registration']")
        self.click("//div[@id='continue-registration']")
        time.sleep(2)
        self.send_keys("//input[@name='first_name']", "Nickson")
        self.send_keys("//input[@name='last_name']", "Gwanzura")
        self.send_keys("//input[@name='email']", "nicksongwe@gmail.com")
        self.send_keys("//input[@name='phone']", "263700000000")
        self.send_keys("//input[@type='password']", "123456789Qaz@")
        time.sleep(2)
        self.click("//input[@id='accept-tnc-user']")
        time.sleep(2)
        self.click("//button[@type='submit']")
        # grab log out button
        self.assert_text("LOG OUT", "//span[text()='LOG OUT']")
