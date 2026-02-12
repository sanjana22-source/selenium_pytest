from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import shutil
import os
import requests


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
        else:
            raise Exception("Browser not supported")

        # Default implicit wait (kept conservative)
        driver.implicitly_wait(10)
        return driver