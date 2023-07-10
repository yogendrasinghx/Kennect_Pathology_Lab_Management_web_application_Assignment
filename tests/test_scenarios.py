import time

from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage
from testdata.test_data import data
from utilities.base_class import BaseClass


class TestScenarios(BaseClass):

    def test_unsuccessful_login(self):

        email = data['email']
        password = data['invalid_password']

        login_page = LoginPage(self.driver)
        email_field = login_page.get_email()
        email_field.send_keys(email)
        password_field = login_page.get_password()
        password_field.send_keys(password)
        sign_in_button = login_page.get_sign_in_button()
        sign_in_button.click()
        self.wait_for_element_visibility(login_page.error_message_locator, 10)
        assert login_page.get_error_message() == "The password is invalid or the user does not have a password."

    def test_successful_login(self):

        email = data['email']
        password = data['password']

        login_page = LoginPage(self.driver)
        email_field = login_page.get_email()
        email_field.clear()
        email_field.send_keys(email)
        password_field = login_page.get_password()
        password_field.clear()
        password_field.send_keys(password)
        sign_in_button = login_page.get_sign_in_button()
        sign_in_button.click()
        self.wait_for_element_visibility(login_page.page_title_locator,10)
        assert self.get_current_url() == "https://gor-pathology.web.app/dashboard"

    def test_todo_list_visibility(self):
        home_page = HomePage(self.driver)
        todo_list_elements = home_page.get_todo_list()
        assert len(todo_list_elements) > 0

    def test_cost_calculator_visibility(self):
        home_page = HomePage(self.driver)
        test_cost_calculator_name = home_page.get_test_cost_calculator_name()
        assert test_cost_calculator_name == "Test Cost Calculator"






