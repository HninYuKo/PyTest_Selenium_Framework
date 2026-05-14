"""
End-to-end test validating the complete purchase flow using the automation framework.
"""
import json
import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage


# test_data_path = '../data/test_e2eTestFramework.json'

test_data_path = '/Users/mims/PycharmProjects/pythonTesting/data/test_e2eTestFramework04.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# @pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.get_title())
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.get_title())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
