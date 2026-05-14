
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
from pageObjects.table import TablePage


# test_data_path = '../data/test_e2eTestFramework.json'

test_data_path = '/Users/mims/PycharmProjects/pythonTesting/data/test_user_stories.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.regression
def test_LanguageFilter_Java(browserInstance):
    driver = browserInstance
    tablePage = TablePage(browserInstance)
    driver.get("https://practicetestautomation.com/practice-test-table/")
    # driver.implicitly_wait(5)
    tablePage.findAllLanguages("Java")
    expectedLangFlag = True
    langList = tablePage.getLanguageElements()
    # print(langList)
    for langTxt in langList:
        if langTxt != "Java":
            expectedLangFlag = False
            break

    assert expectedLangFlag is True, f" Filter by Java Expected language Flag: True, Actual: {expectedLangFlag}"

@pytest.mark.regression
def test_LanguageFilter_Python(browserInstance):
    driver = browserInstance
    tablePage = TablePage(browserInstance)
    driver.get("https://practicetestautomation.com/practice-test-table/")
    # driver.implicitly_wait(5)
    tablePage.findAllLanguages("Python")
    expectedLangFlag = True
    langList = tablePage.getLanguageElements()
    # print(langList)
    for langTxt in langList:
        if langTxt != "Python":
            expectedLangFlag = False
            break

    assert expectedLangFlag is True, f" Filter by Python Expected language Flag: True, Actual: {expectedLangFlag}"

@pytest.mark.regression
def test_LanguageFilter_Any(browserInstance):
    driver = browserInstance
    tablePage = TablePage(browserInstance)
    driver.get("https://practicetestautomation.com/practice-test-table/")
    # driver.implicitly_wait(5)
    tablePage.findAllLanguages("Any")
    expectedLangFlag = True
    langList = tablePage.getLanguageElements()
    # print(langList)
    for langTxt in langList:
        if langTxt == "":
            expectedLangFlag = False
            break

    assert expectedLangFlag is True, f" Filter by Any Expected language Flag: True, Actual: {expectedLangFlag}"

