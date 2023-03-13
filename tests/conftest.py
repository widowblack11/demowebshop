import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.DemoQaWithEnv import DemoQaWithEnv


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope="session")
def get_option(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(get_option):
    return DemoQaWithEnv(get_option)


@pytest.fixture(scope='session')
def reqres(get_option):
    return DemoQaWithEnv(get_option).reqres


@pytest.fixture(scope='session')
def cookie(demoshop):
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Check code"):
        assert response.status_code == 302

    return authorization_cookie


@pytest.fixture(scope='function')
def auth_browser(demoshop, cookie):
    browser.config.base_url = demoshop.demoqa.url
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    yield browser
    browser.quit()





