from playwright.sync_api import Locator, Page, expect
from pytest_playwright_visual.plugin import assert_snapshot


class BasePage:
    def __init__(self, page: Page, assert_snapshot):
        self.page = page
        self.assert_snapshot = assert_snapshot

    def click_on_link_with_new_tab(self, element: Locator):
        with self.page.context.expect_page() as new_tab_info:
            element.click()

        new_tab = new_tab_info.value
        new_tab.wait_for_load_state()

    def check_new_tab_content(
        self,
        title,
        url,
    ):
        context = self.page.context
        pages_after = context.pages
        new_tab = pages_after[-1]

        expect(new_tab).to_have_url(url)
        expect(new_tab).to_have_title(title)
