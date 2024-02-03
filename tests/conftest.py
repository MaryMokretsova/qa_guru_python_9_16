import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def browser_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(800, 480), (480, 360)])
def browser_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(scope='session', params=[(1920, 1080), (1280, 720), (1600, 900), (800, 480), (480, 360),  (390, 844)])
def check_browser(request):
    resolution = request.param
    width, height = resolution
    browser.config.window_width = width
    browser.config.window_height = height
    if width <= 1010:
        yield "mobile"

        browser.quit()
    else:
        yield 'desktop'

    browser.quit()
