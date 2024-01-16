from pages.swag_labs import SwagLab
from conftest import browser


def test_icon(browser):
    tester = SwagLab(browser)
    tester.visit()
    assert tester.exist_icon()


def test_name(browser):
    tester = SwagLab(browser)
    tester.visit()
    assert tester.exist_name


def test_password(browser):
    tester = SwagLab(browser)
    tester.visit()
    assert tester.exist_password()
