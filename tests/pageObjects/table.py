from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkout_confirmation import CheckoutConfirmation
from utils.browserutils import BrowserUtils


class TablePage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.languageElements = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
        self.rdoLang = (By.NAME,"lang")

        # self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        # self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getLanguageElements(self):
        langList = []
        languageElements = self.driver.find_elements(*self.languageElements)
        for language in  languageElements:
            if language.text == "":
                continue
            langList.append(language.text)
            # print(f" each element text {language.text}")
        # print(f"{langList}\n")
        return langList

    def findAllLanguages(self, lang_param: str):
        print("lang_param : ", lang_param )
        # Find all radio buttons in the group
        options = self.driver.find_elements(*self.rdoLang)

        for option in options:
            if option.get_attribute("value") == lang_param:
                option.click()
                break

    # def waitShopLink(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located(self.shop_link))
    #
    # def add_product_to_cart(self, product_name):
    #     self.waitShopLink()
    #     self.driver.find_element(*self.shop_link).click()
    #     products = self.driver.find_elements(*self.product_cards)
    #     for product in products:
    #         productName = product.find_element(By.XPATH, "div/h4/a").text
    #         if productName == product_name:
    #             product.find_element(By.XPATH, "div/button").click()
    #
    # def goToCart(self):
    #     self.driver.find_element(*self.checkout_button).click()
    #     checkout_confirmation = CheckoutConfirmation(self.driver)
    #     return checkout_confirmation




