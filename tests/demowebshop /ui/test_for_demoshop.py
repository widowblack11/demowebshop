import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()


def test_login_with_api(auth_browser):
    auth_browser.open("")

    with step("Verify successful authorization"):
        auth_browser.element(".account").should(have.text(os.getenv("LOGIN")))


def test_search_negative_result(auth_browser):
    auth_browser.open("")
    with step("Negitive search"):
        browser.element('.search-box [value="Search store"]').click()
        browser.element('.search-box [value="Search store"]').type('negative test').press_enter()
        browser.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(auth_browser):
    auth_browser.open("")
    with step("Check logout"):
        browser.element('.ico-logout').click()
        browser.element('.ico-login').should(have.text('Log in'))


def test_watch_profile(auth_browser):
    auth_browser.open("")

    with step("Check info in profile"):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('#FirstName').should(have.value('Oksana'))
        browser.element('#LastName').should(have.value('Oksana'))
        browser.element('#Email').should(have.value(os.getenv('LOGIN')))
        browser.element('[checked="checked"]#gender-female')


def test_watch_profile(auth_browser):
    auth_browser.open("")

    with step("Check text buttion in change passwird"):
        browser.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser.element('.active').click()
        browser.element('[for="OldPassword"]')
        browser.element('[for="NewPassword"]')
        browser.element('[for="ConfirmNewPassword"]')







