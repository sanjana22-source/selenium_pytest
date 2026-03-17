import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import tempfile
import shutil


class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()

            # 🔥 Force a fresh temp user profile
            temp_profile = tempfile.mkdtemp()
            options.add_argument(f"--user-data-dir={temp_profile}")

            # Disable password manager
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False
            }
            options.add_experimental_option("prefs", prefs)

            # Extra hardening
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-save-password-bubble")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--start-maximized")

            # Try to download driver via webdriver-manager; if network fails, fall back to local driver on PATH
            try:
                driver_path = ChromeDriverManager().install()
                driver = webdriver.Chrome(
                    service=Service(driver_path),
                    options=options
                )
            except Exception as e:
                # If webdriver-manager fails (e.g., no internet), attempt to use chromedriver from PATH
                local_chromedriver = shutil.which("chromedriver")
                if local_chromedriver and os.path.exists(local_chromedriver):
                    driver = webdriver.Chrome(
                        service=Service(local_chromedriver),
                        options=options
                    )
                else:
                    # Re-raise with helpful message
                    raise RuntimeError(
                        "Failed to obtain ChromeDriver via webdriver-manager and no local 'chromedriver' was found on PATH. "
                        "Ensure you have internet access or install chromedriver and add it to PATH. Original error: " + str(e)
                    )
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            options.add_argument("--start-maximized")

            try:
                driver_path = GeckoDriverManager().install()
                driver = webdriver.Firefox(
                    service=FirefoxService(driver_path),
                    options=options
                )
            except Exception as e:
                local_driver = shutil.which("geckodriver")
                if local_driver:
                    driver = webdriver.Firefox(
                        service=FirefoxService(local_driver),
                        options=options
                    )
                else:
                    raise RuntimeError(
                        f"GeckoDriver not found. {str(e)}"
                    )

            # -------------------- EDGE --------------------
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            try:
                driver_path = EdgeChromiumDriverManager().install()
                driver = webdriver.Edge(
                    service=EdgeService(driver_path),
                    options=options
                )
            except Exception as e:
                local_driver = shutil.which("msedgedriver")
                if local_driver:
                    driver = webdriver.Edge(
                        service=EdgeService(local_driver),
                        options=options
                    )
                else:
                    raise RuntimeError(
                        f"EdgeDriver not found. {str(e)}"
                    )
        else:
            raise Exception("Browser not supported")

        # Default implicit wait (kept conservative)
        driver.implicitly_wait(10)
        return driver