from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.shop import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.successtext=(By.XPATH,"//h1[normalize-space()='Logged In Successfully']")
        self.sign_button = (By.ID, "submit")
        self.logout_button = (By.XPATH,"//a[normalize-space()='Log out']")


    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.successtext))

    # def login(self, username, password):
    #     self.driver.find_element(*self.username_input).send_keys(username)
    #     self.driver.find_element(*self.password).send_keys(password)
    #     self.driver.find_element(*self.sign_button).click()
    #     shop_page = ShopPage(self.driver)
    #     return shop_page

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        self.wait()


    def find_text(self):
        return self.driver.find_element(*self.successtext).text

    def isDisplayed(self):
        return self.driver.find_element(*self.logout_button).is_displayed()