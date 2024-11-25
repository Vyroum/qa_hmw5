import time
from datetime import datetime

from selene import browser, be, have
from selene.support.by import xpath


first_name_field_address = '//input[@id="firstName"]'
last_name_field_address = '//input[@id="lastName"]'
email_field_address = '//input[@id="userEmail"]'
gender_radiobuttons = '//input[@name="gender"]'
gender_male_radiobutton = '//input[@id="gender-radio-1"]'
gender_female_radiobutton = '//input[@id="gender-radio-2"]'
gender_other_radiobutton = '//input[@id="gender-radio-3"]'
mobile_number_address = '//input[@id="userNumber"]'
datepicker_address = '//input[@id="dateOfBirthInput"]'
datepicker_tenth_day = '//div[contains(@class, "react-datepicker__day react-datepicker__day--010")]'
subjects_input_line = '//input[@id="subjectsInput"]'
subject_container = '//input[@id="subjectsContainer"]'
subjects_multiselect_choice = '//input[@id="react-select-2-option-0"]'
hobbies_checkboxes = '//div[contains(@class, "custom-checkbox")]'
hobbies_sport = '//input[@id="hobbies-checkbox-1"]'
hobbies_reading = '//input[@id="hobbies-checkbox-2"]'
hobbies_music = '//input[@id="hobbies-checkbox-3"]'
picture_button = '//input[@id="uploadPicture"]'


def test_name():
    browser.element(xpath(first_name_field_address)).should(be.blank).type("Andrei")
    browser.element(xpath(first_name_field_address)).should(have.value("Andrei"))
    browser.element(xpath(last_name_field_address)).should(be.blank).type("Monichev")
    browser.element(xpath(last_name_field_address)).should(have.value("Monichev"))

def test_email():
    browser.element(xpath(email_field_address)).should(be.blank).type("testmail@test.ru")
    browser.element(xpath(email_field_address)).should(have.value("testmail@test.ru"))

def test_gender():
    browser.all(xpath(gender_radiobuttons)).should(have.size(3))
    browser.element(gender_male_radiobutton).should(be.present)
    browser.element(gender_female_radiobutton).should(be.present)
    browser.element(gender_other_radiobutton).should(be.present)
    browser.element(gender_male_radiobutton).click()

def test_mobile_number():
    browser.element(xpath(mobile_number_address)).should(be.blank).type("1231231234")
    browser.element(xpath(mobile_number_address)).should(have.value("1231231234"))

def test_datepicker():
    browser.element(xpath(datepicker_address)).should(be.clickable)
    browser.element(xpath(datepicker_address)).click()
    browser.element(xpath(datepicker_tenth_day)).click()
    browser.element(xpath(datepicker_address)).should(have.value_containing("10"))

def test_subjects():
    browser.element(xpath(subjects_input_line)).should(be.blank)
    browser.element(xpath(subjects_input_line)).type('M')
    browser.element(xpath(subjects_multiselect_choice)).click()
    browser.element(xpath(subjects_input_line)).type('Co')
    browser.element(xpath(subjects_multiselect_choice)).click()

def test_hobbies():
    browser.all(xpath(hobbies_checkboxes)).should(have.size(3))
    browser.element(xpath(hobbies_sport)).should(be.present)
    browser.element(xpath(hobbies_music)).should(be.present)
    browser.element(xpath(hobbies_reading)).should(be.present)
    browser.element(xpath(hobbies_music)).click()

def test_picture():
    browser.element(xpath(picture_button)).set_value(image)
