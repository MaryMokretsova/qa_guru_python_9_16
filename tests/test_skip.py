import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop_skip(is_desktop_browser):
    if not is_desktop_browser:
        pytest.skip(reason='Тест для экрана компьютера')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobil
def test_mobile_skip(is_desktop_browser):
    if is_desktop_browser:
        pytest.skip(reason='Тест для экрана телефона')
    browser.open('/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))