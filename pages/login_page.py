import re
from typing import Callable

import allure
from playwright.sync_api import Locator, Page, expect

from core.urls import BASE_URL
from pages.common_element import CommonPage


class LoginPage(CommonPage):
    def __init__(self, page: Page, assert_snapshot: Callable) -> None:
        super().__init__(page, assert_snapshot)

        self.page: Page = page
        self.LOGIN_URL: str = f"{BASE_URL}/login"

        self.email_input: Locator = self.page.locator('input[type="email"]')
        self.password_input: Locator = self.page.locator('input[type="password"]')
        self.submit_button: Locator = self.page.locator(
            "div.login-action.mt-8 > ion-button"
        )
        self.forgot_password_link: Locator = self.page.locator(
            'ion-label[translate="login.ForgotPassword"]'
        )
        self.continue_guest_link: Locator = self.page.locator(
            'ion-label[translate="login.ContinueAsGuest"]'
        )

        self.language_button: Locator = self.page.locator("#language-selector")

    @allure.step("Go to login page")
    def goto(self) -> None:
        self.page.goto(self.LOGIN_URL)

    @allure.step("Perform login with email: {email}")
    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    @allure.step("Click 'Continue as Guest'")
    def click_on_continue_guest(self) -> None:
        self.continue_guest_link.click()

    @allure.step("Click 'Forgot Password' link")
    def click_forgot_password(self) -> None:
        self.forgot_password_link.click()

    @allure.step("Change language to '{lang}'")
    def change_lang(self, lang: str) -> None:
        self.language_button.click()
        print(lang)
        self.page.click(f"text='{lang}'")

    @allure.step("Check submit button text: '{text}'")
    def check_submit_button_text(self, text: str) -> None:
        expect(self.submit_button).to_be_visible()
        expect(self.submit_button).to_have_text(text)

    @allure.step("Check selected language: '{lang}'")
    def check_selected_language(self, lang: str) -> None:
        expect(self.language_button).to_have_text(lang, use_inner_text=True)

    @allure.step("Click 'Forgot Password' link and open in a new tab")
    def click_on_forgot_password(self) -> None:
        return self.click_on_link_with_new_tab(self.forgot_password_link)
