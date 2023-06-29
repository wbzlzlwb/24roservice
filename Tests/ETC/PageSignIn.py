# Pages.PageEmailSignin.py
from Tests.Pages.Base import BasePage
from selenium.webdriver.common.by import By
# from Tests.Config.Accounts import Accounts
#rr

class EmailSignIn(BasePage):

    input_email_id = (By.NAME, "01000000008")
    input_email_pw = (By.NAME, "1111")
    btn_login = (By.XPATH, '//button[text()="인증하기"]')

    sign_in_url = "https://24ro.co.kr/"

    def __init__(self, driver):
        super(EmailSignIn, self).__init__(driver)

    def get_login_page(self):
        self.get(self.sign_in_url)

    def send_keys_email_id(self):
        self.send_keys(self.input_email_id, Accounts["email_id"])

    def send_keys_email_pw(self):
        self.send_keys(self.input_email_pw, Accounts["email_pw"])