import allure
import pytest
from _pytest.fixtures import FixtureRequest


@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(
    request: FixtureRequest, feature, scenario, step, step_func, step_func_args
):
    outcome = yield
    exc = outcome.excinfo
    if exc is not None:
        page = request.getfixturevalue("page")  # Фикстура playwright
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name=f"Failure screenshot - {step.name}",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_bdd_after_scenario(request: FixtureRequest, feature, scenario):
    yield
    page = request.getfixturevalue("page")
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=f"Final screenshot - {scenario.name}",
        attachment_type=allure.attachment_type.PNG,
    )
