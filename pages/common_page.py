import allure
from playwright.sync_api import Page, expect
from pytest_playwright_visual.plugin import assert_snapshot

from pages import BasePage


class CommonPage(BasePage):
    def __init__(self, page: Page, assert_snapshot):
        super().__init__(page, assert_snapshot)

        self.page = page
        self.assert_snapshot = assert_snapshot

        self.notification = self.page.locator("rg-notification")
        self.notification_summary = self.page.locator(".notification__summary")
        self.notification_text = self.page.locator(".notification__text")
        self.load_page = self.page.locator("div.tm-landing-container")

        self.chat_button = self.page.locator("div#c-external-chat-icon")
        self.chat = self.page.locator('iframe[id="c-chat-widget-iframe"]')

    @allure.step("Wait for loading screen to disappear")
    def wait_for_load_page_disappear(self) -> None:
        self.load_page.wait_for(state="hidden")

    @allure.step("Open chat")
    def open_chat(self) -> None:
        self.chat_button.click()

    @allure.step("Verify that chat is opened")
    def check_chat_is_opened(self) -> None:
        expect(self.chat).to_be_visible()

    @allure.step("Verify notification with summary '{summary}' and text '{text}'")
    def check_notification(self, summary: str, text: str) -> None:
        expect(self.notification).to_be_visible()
        expect(self.notification_summary).to_have_text(summary)
        expect(self.notification_text).to_have_text(text)
        self.assert_snapshot(self.notification.screenshot())
