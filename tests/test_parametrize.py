import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize("browser_desktop", [(1600, 900), (1440, 900)], indirect=True)
def test_desktop_indirect(browser_desktop):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("browser_mobile", [(932, 430), (740, 360)], indirect=True)
def test_mobile_indirect(browser_mobile):
    browser.open('https://github.com/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
