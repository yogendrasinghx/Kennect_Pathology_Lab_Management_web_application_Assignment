from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.email_locator = (By.XPATH,"//input[@name='email']")
        self.password_locator = (By.XPATH,"//input[@name='password']")
        self.sign_in_button_locator = (By.XPATH,"//span[normalize-space()='Login']/parent::button")
        self.page_title_locator = (By.XPATH, "//div[@class='title']")
        self.error_message_locator = (By.XPATH,"//div[@class='MuiAlert-message']")

    def get_email(self):
        return self.driver.find_element(*self.email_locator)

    def get_password(self):
        return self.driver.find_element(*self.password_locator)

    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message_locator).text



