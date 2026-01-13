"""
Test to validate sorting behavior of a table column using Selenium and Pytest.
"""
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browser_sorted_veggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collect all veggie names -> BrowserSortedveggieList ( A,B, C)
    veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggie_web_elements:
        browser_sorted_veggies.append(ele.text)
    original_browser_sorted_list = browser_sorted_veggies.copy()
    # Sort this original_browser_sorted_list => newSortedList -> (A,B,C)
    browser_sorted_veggies.sort()
    assert browser_sorted_veggies == original_browser_sorted_list
