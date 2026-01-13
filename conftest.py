"""
Pytest-based Selenium automation framework using Page Object Model (POM).

The framework supports:
- Cross-browser execution via command-line options
- Fixture-based WebDriver lifecycle management
- Page Object Model for UI interactions
- Data-driven testing using external JSON files
- Automatic screenshots and HTML reports on test failures
"""
import os
import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    browser_name = request.config.getoption( "browser_name" )

    if browser_name == "chrome":
        chrome_options = Options()

        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            }
        )
        chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    driver.quit()  #post your test function execution


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item,call):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            os.makedirs(reports_dir, exist_ok=True)
            safe_nodeid = re.sub(r"[^\w\-.]", "_", report.nodeid)
            file_name = os.path.join(reports_dir, safe_nodeid.replace("::", "_") + ".png")
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
