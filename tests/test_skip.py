import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop_skip(check_browser):
    if check_browser == 'mobile':
        pytest.skip('Not a desktop resolution')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.mobil
def test_mobile_skip(check_browser):
    if check_browser == 'desktop':
        pytest.skip('Not a mobile resolution')
    browser.open('https://github.com/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
