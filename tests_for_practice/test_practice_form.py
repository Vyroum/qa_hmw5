import os

from selene import browser, be, have, by

def test_practice_form():
    browser.open('/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('[id="firstName"]').should(be.blank).type("Andrei")
    browser.element('[id="lastName"]').should(be.blank).type("Monichev")

    browser.element('[id="userEmail"]').should(be.blank).type("testmail@test.ru")

    browser.element(by.text("Male")).click()

    browser.element('[id="userNumber"]').should(be.blank).type("1231231234")

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element("#dateOfBirthInput").click()
    browser.element("[class='react-datepicker__month-select']").click().element(by.text("September")).click()
    browser.element("[class='react-datepicker__year-select']").click().element(by.text("1995")).click()
    browser.element("[class='react-datepicker__month']").element(by.text("13")).click()

    browser.element("#subjectsInput").type('Maths').press_enter().type("Arts").press_enter().type("Computer Science").press_enter()


    browser.element(by.text("Sports")).click()
    browser.element(by.text("Music")).click()
    browser.element(by.text("Reading")).click()

    #browser.element(by.text("[id='uploadPicture']")).send_keys(os.path.abspath("../tests_for_practice/image.jpg"))

    browser.element('[id="currentAddress"]').type("City Name, Street Name")

    browser.element('[id="state"]').click()
    browser.element(by.text("NCR")).click()
    browser.element('[id="city"]').click()
    browser.element(by.text("Noida")).click()

    browser.element('[id="submit"]').click()
    browser.element(".modal-body").should(have.text("Andrei Monichev"))
    browser.element(".modal-body").should(have.text("testmail@test.ru"))
    browser.element(".modal-body").should(have.text("Male"))
    browser.element(".modal-body").should(have.text("1231231234"))
    browser.element(".modal-body").should(have.text("13 September,1995"))
    browser.element(".modal-body").should(have.text("Maths, Arts, Computer Science"))
    browser.element(".modal-body").should(have.text("Sports, Music, Reading"))
    #browser.element(".modal-body").should(have.text("image.jpg"))
    browser.element(".modal-body").should(have.text("City Name, Street Name"))
    browser.element(".modal-body").should(have.text("NCR Noida"))
