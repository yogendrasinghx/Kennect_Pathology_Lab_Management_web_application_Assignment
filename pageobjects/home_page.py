from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.page_title_locator = (By.XPATH,"//div[@class='title']")
        self.todo_list_locator = (By.CSS_SELECTOR,"div[class*='MuiCardContent-root']")
        self.test_cost_calculator_name_locator = (By.XPATH,"//div[normalize-space()='Test Cost Calculator']/div")
        self.add_test_for_patient_locator = (By.ID,"patient-test")

    def get_todo_list(self):
        return self.driver.find_elements(*self.todo_list_locator)

    def get_test_cost_calculator_name(self):
        return self.driver.find_element(*self.test_cost_calculator_name_locator).text

    def get_add_test_for_patient_input(self):
        return self.driver.find_element(*self.add_test_for_patient_locator)

    def get_page_title(self):
        return self.driver.find_element(*self.page_title_locator).text

