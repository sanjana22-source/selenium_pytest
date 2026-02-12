import os
from datetime import datetime
import allure
import yaml
from allure_commons.types import AttachmentType
import pytest

from services.user_service import UserService
from utilities.config_reader import get_config
from utilities.driver_factory import DriverFactory


# ----------------------
# UI Driver Fixture
# ----------------------

@pytest.fixture(scope="function")
def driver():
    config = get_config()
    driver = DriverFactory.get_driver(config["browser"])
    driver.get(config["base_url"])
    yield driver
    driver.quit()


# ----------------------
# API Config + Fixture
# ----------------------

def get_api_config():
    with open("config/api_config.yaml") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="session")
def user_service():
    config = get_api_config()

    return UserService(
        base_url=config["base_url"],
        default_headers=config.get("default_headers")
    )

# ----------------------
# Screenshot Hook
# ----------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            last_element = getattr(driver, "last_element", None)

            if last_element:
                driver.execute_script(
                    "arguments[0].style.border='3px solid red';"
                    "arguments[0].style.backgroundColor='yellow';",
                    last_element
                )

            project_root = os.path.dirname(__file__)
            screenshot_dir = os.path.join(project_root, "screenshots")

            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{item.name} - FAILED",
                attachment_type=AttachmentType.PNG
            )