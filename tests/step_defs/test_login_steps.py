import pytest
from playwright.sync_api import Browser, Page
from pytest_bdd import given, parsers, scenarios, then, when

from core.user import BASE_PASSWORD
from pages.login_page import LoginPage
from pages.trading_page import TradingPage

scenarios("../features/login.feature")


@pytest.fixture
def login_page(page: Page, assert_snapshot) -> LoginPage:
    return LoginPage(page, assert_snapshot)


@pytest.fixture
def login_fr_page(browser: Browser, assert_snapshot) -> LoginPage:
    france_context = browser.new_context(
        locale="fr-FR", geolocation={"latitude": 48.8566, "longitude": 2.3522}
    )
    page = france_context.new_page()
    return LoginPage(page, assert_snapshot)


@pytest.fixture
def trading_page(page: Page, assert_snapshot) -> TradingPage:
    return TradingPage(page, assert_snapshot)


@given("Open page")
def open_page(login_page: LoginPage) -> None:
    login_page.goto()


@given("Open page from FR")
def open_page_fr(login_fr_page: LoginPage) -> None:
    login_fr_page.goto()


@when(parsers.parse('Login email = "{email}"'))
def login_user(login_page: LoginPage, email: str) -> None:
    login_page.login(email, BASE_PASSWORD)


@then(parsers.parse("See terminal"))
def check_success_login(trading_page: TradingPage) -> None:
    trading_page.check_trading_page_is_opened()


@when(parsers.parse("Open chat"))
def open_chat(login_page: LoginPage) -> None:
    login_page.open_chat()


@when(parsers.parse('Change language "{lang}"'))
def change_language(login_page: LoginPage, lang: str) -> None:
    login_page.change_lang(lang)


@when(parsers.parse("Forgot password"))
def forgot_password(login_page: LoginPage) -> None:
    login_page.click_on_forgot_password()


@then(parsers.parse("See chat"))
def check_chat_opened(login_page: LoginPage) -> None:
    login_page.check_chat_is_opened()


@then(parsers.parse('Page translated on "{lang}" ' 'and text visible "{expect}"'))
def check_page_translated(login_page: LoginPage, lang: str, expect: str) -> None:
    login_page.check_selected_language(lang)
    login_page.check_submit_button_text(expect)


@then(parsers.parse('Page opened on "{lang}" ' 'and text visible "{expect}"'))
def check_fr_page_translated(login_fr_page: LoginPage, lang: str, expect: str) -> None:
    login_fr_page.check_selected_language(lang)
    login_fr_page.check_submit_button_text(expect)


@then(parsers.parse("See failed notification"))
def check_failed_notification(login_page: LoginPage) -> None:
    login_page.check_notification(
        "Неверные данные для доступа", "Неверный логин или пароль"
    )


@then(parsers.parse('See new page "{title}", "{url}"'))
def check_new_tab(login_page: LoginPage, title: str, url: str) -> None:
    login_page.check_new_tab_content(title, url)
