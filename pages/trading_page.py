from typing import Callable

import allure
from playwright.sync_api import Page, expect

from core.urls import BASE_URL
from pages.common_element import CommonPage


class TradingPage(CommonPage):
    def __init__(self, page: Page, assert_snapshot: Callable) -> None:
        super().__init__(page, assert_snapshot)

        self.page = page
        self.TRADING_URL = f"{BASE_URL}/trading"

        self.app_shell_main = self.page.locator(".app_shell_main")
        self.header = self.page.locator(".app__header")
        self.menu = self.page.locator(".app_menu_collapsed")
        self.header_status = self.page.locator(".app__header_stats")
        self.app_shell_main_center = self.page.locator(".app_shell_main_center")
        self.app_footer = self.page.locator(".app__footer")
        self.watch_list_tile = self.page.locator(".ums-watches-watchListTile")

    @allure.step("Go to trading page")
    def goto(self) -> None:
        self.page.goto(self.TRADING_URL)

    @allure.step("Check that trading page is opened and all elements are visible")
    def check_trading_page_is_opened(self) -> None:
        self.wait_for_load_page_disappear()

        expect(self.app_shell_main).to_be_visible()
        expect(self.header).to_be_visible()
        expect(self.menu).to_be_visible()
        expect(self.app_footer).to_be_visible()
        expect(self.header_status).to_be_visible()
        expect(self.watch_list_tile).to_be_visible()
        expect(self.app_shell_main_center).to_be_visible()
