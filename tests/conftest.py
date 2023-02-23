import os

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from utils.base_session import BaseSession

browser.config.base_url = "https://demowebshop.tricentis.com"

load_dotenv()


@pytest.fixture(scope='session')
def demoshop():
    demoshop_session = BaseSession(os.getenv("API_URL"))
    return demoshop_session


@pytest.fixture(scope='session')
def auth_browser(demoshop):
    response = demoshop.post("/login", json={"Email": os.getenv("LOGIN"), "Password": os.getenv("PASSWORD")}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Check code"):
        response.status_code = 302

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser


@pytest.fixture(scope='session')
def reqres_in():
    return BaseSession(os.getenv("BASE_URL"))



