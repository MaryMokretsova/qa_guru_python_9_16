import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(1920, 1080), (1280, 720)], indirect=True)
def test_desktop_indirect(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(800, 480), (480, 360)], indirect=True)
def test_mobile_indirect(mobile_browser):
    browser.open('/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))