import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_set():
    browser.config.driver_name = "firefox"
    browser.config.base_url= "https://demoqa.com"
    browser.driver.maximize_window()

    yield
    browser.quit()
