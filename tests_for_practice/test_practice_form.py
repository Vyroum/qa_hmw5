import os

from selene import browser, be, have
from selene.support.by import xpath

## Input fields
first_name_field_address = xpath('//input[@id="firstName"]')
last_name_field_address = xpath('//input[@id="lastName"]')
email_field_address = xpath('//input[@id="userEmail"]')
gender_radiobuttons = xpath('//input[@name="gender"]')
gender_male_radiobutton = xpath('//label[@for="gender-radio-1"]')
gender_female_radiobutton = xpath('//label[@for="gender-radio-2"]')
gender_other_radiobutton = xpath('//label[@for="gender-radio-3"]')
mobile_number_address = xpath('//input[@id="userNumber"]')
datepicker_address = xpath('//input[@id="dateOfBirthInput"]')
datepicker_month_select = xpath('//select[@class="react-datepicker__month-select"]')
datepicker_year_select = xpath('//select[@class="react-datepicker__year-select"]')
datepicker_13_day = xpath('//div[contains(@class, "react-datepicker__day react-datepicker__day--013")]')
subjects_input_line = xpath('//input[@id="subjectsInput"]')
subject_container = xpath('//input[@id="subjectsContainer"]')
hobbies_checkboxes = xpath('//div[contains(@class, "custom-checkbox")]')
hobbies_sport = xpath('//label[@for="hobbies-checkbox-1"]')
hobbies_reading = xpath('//label[@for="hobbies-checkbox-2"]')
hobbies_music = xpath('//label[@for="hobbies-checkbox-3"]')
picture_button = xpath('//input[@id="uploadPicture"]')
address_field = xpath('//textarea[@id="currentAddress"]')
state_dropdown = xpath('//div[@id="state"]')
city_dropdown = xpath('//div[@id="city"]')
submit_button = xpath('//button[@id="submit"]')
submit_form = ".modal-body"

##Dropdown selects
subjects_first_choice = '[id="react-select-2-option-0"]'
subjects_third_choice = '[id="react-select-2-option-2"]'
state_first_choice = '[id="react-select-3-option-0"]'
city_third_choice = '[id="react-select-4-option-2"]'


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element(first_name_field_address).should(be.blank).type("Andrei")
    browser.element(first_name_field_address).should(have.value("Andrei"))
    browser.element(last_name_field_address).should(be.blank).type("Monichev")
    browser.element(last_name_field_address).should(have.value("Monichev"))

    browser.element(email_field_address).should(be.blank).type("testmail@test.ru")
    browser.element(email_field_address).should(have.value("testmail@test.ru"))


    browser.all(gender_radiobuttons).should(have.size(3))
    browser.element(gender_male_radiobutton).should(be.present).click()
    browser.element(gender_female_radiobutton).should(be.present)
    browser.element(gender_other_radiobutton).should(be.present)

    browser.element(mobile_number_address).should(be.blank).type("1231231234")
    browser.element(mobile_number_address).should(have.value("1231231234"))


    browser.element(datepicker_address).should(be.clickable)
    browser.element(datepicker_address).click()
    browser.element(datepicker_month_select).click().type('s').press_enter()
    browser.element(datepicker_year_select).click().type('1995').press_enter()
    browser.element(datepicker_13_day).click()
    browser.element(datepicker_address).should(have.value_containing("13 Sep 1995"))

    browser.element(subjects_input_line).should(be.blank)
    browser.element(subjects_input_line).type('m')
    browser.element(subjects_first_choice).click()
    browser.element(subjects_input_line).type('a')
    browser.element(subjects_third_choice).click()
    browser.element(subjects_input_line).type('c')
    browser.element(subjects_third_choice).click()
    browser.all(subject_container).should(be._not_.blank)


    browser.all(hobbies_checkboxes).should(have.size(3))
    browser.element(hobbies_sport).should(be.present).click()
    browser.element(hobbies_music).should(be.present).click()
    browser.element(hobbies_reading).should(be.present).click()


    browser.element(picture_button).should(be.clickable)
    browser.element(picture_button).send_keys(os.path.abspath("../tests_for_practice/image.jpg"))


    browser.element(address_field).should(be.blank)
    browser.element(address_field).type("City Name, Street Name")
    browser.element(address_field).should(have.value("City Name, Street Name"))

    browser.element(state_dropdown).click()
    browser.element(state_first_choice).click()
    browser.element(state_dropdown).should(have.text("NCR"))
    browser.element(city_dropdown).click()
    browser.element(city_third_choice).click()
    browser.element(city_dropdown).should(have.text("Noida"))


    browser.element(submit_button).click()
    browser.element(submit_form).should(have.text("Andrei Monichev"))
    browser.element(submit_form).should(have.text("testmail@test.ru"))
    browser.element(submit_form).should(have.text("Male"))
    browser.element(submit_form).should(have.text("1231231234"))
    browser.element(submit_form).should(have.text("13 September,1995"))
    browser.element(submit_form).should(have.text("Maths, Arts, Computer Science"))
    browser.element(submit_form).should(have.text("Sports, Music, Reading"))
    browser.element(submit_form).should(have.text("image.jpg"))
    browser.element(submit_form).should(have.text("City Name, Street Name"))
    browser.element(submit_form).should(have.text("NCR Noida"))
