"""
End-to-end test validating the complete purchase flow using the automation framework.
"""
import json
import os
import sys
import time
# from datetime import time

import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage


# test_data_path = '../data/test_e2eTestFramework.json'

test_data_path = '/Users/mims/PycharmProjects/pythonTesting/data/test_user_stories.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# @pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("test_list_item", test_list)
def test_userSuccess(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(browserInstance)
    # driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # print(loginPage.get_title())
    loginPage.login("student", "Password123")
    # loginPage.login(test_list_item["userName"], test_list_item["userPassword"])
    success_url = "practicetestautomation.com/logged-in-successfully/"
    expectedText = "Logged In Successfully"
    actualText = loginPage.find_text()
    # time.sleep(3)
    # print(driver.current_url)
    # print(f"{actualText} - actual text")
    expectedLogoutBtn = True
    actualLogoutBtn = loginPage.isDisplayed()
    # print(f"{actualLogoutBtn} - actualLogoutBtn Status")
    # tbody tr  td:nth-child(5)
    assert success_url in driver.current_url, f"{success_url} is not a login success URL"
    assert expectedText in actualText, f" Expected log in success text: {expectedText}, Actual: {actualText}"
    assert expectedLogoutBtn == actualLogoutBtn, f"Expected logout btn status '{expectedLogoutBtn}', but got '{actualLogoutBtn}'"


    # shop_page.add_product_to_cart(test_list_item["productName"])
    # print(shop_page.get_title())
    # checkout_confirmation = shop_page.goToCart()
    # checkout_confirmation.checkout()
    # checkout_confirmation.enter_delivery_address("ind")
    # checkout_confirmation.validate_order()
