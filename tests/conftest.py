import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.DemoQaWithEnv import DemoQaWithEnv
from utils.base_session import BaseSession

browser.config.base_url = "https://demowebshop.tricentis.com"

load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def demoshop(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def reqres(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env).reqres


@pytest.fixture(scope='function')
def auth_browser(demoshop):
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Check code"):
        response.status_code = 302

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser





