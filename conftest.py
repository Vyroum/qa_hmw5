import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_set():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.driver.maximize_window()
    yield
    browser.quit()