import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_set():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.driver.maximize_window()
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    yield
    browser.quit()
