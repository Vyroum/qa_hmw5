from selene import browser, be, have

first_name_field_address = "'//input[@id='firstName']'"
last_name_field_address = "//input[@id='lastName']"


def test_name():
    browser.element(first_name_field_address).should(be.blank).type("Andrei")
    browser.element(first_name_field_address).should(have.exact_text("Andrei"))