import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # ==========================
    # Utility Methods
    # ==========================

    def _attach_log(self, message):
        allure.attach(
            message,
            name="Execution Log",
            attachment_type=AttachmentType.TEXT
        )

    def _attach_screenshot(self, name="Screenshot", element=None):
        """
        Attach screenshot to Allure.
        If element is provided → scroll + highlight before screenshot.
        This method will tolerate stale elements — if the element goes stale we'll
        fall back to attaching a full-page screenshot without interacting with it.
        """
        try:
            if element:
                try:
                    self._scroll_into_view(element)
                    self._highlight_element(element)
                except StaleElementReferenceException:
                    # Element went stale (click likely caused DOM update) —
                    # continue and attach a regular screenshot instead of failing.
                    element = None

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=name,
                attachment_type=AttachmentType.PNG
            )

            if element:
                try:
                    self._remove_highlight(element)
                except StaleElementReferenceException:
                    # If element became stale while removing highlight, ignore.
                    pass

        except Exception as e:
            # Never let screenshotting break the test flow; log the issue to Allure.
            try:
                self._attach_log(f"Screenshot attachment failed: {e}")
            except Exception:
                # If even logging fails, swallow silently — we must not raise here.
                pass

    def _highlight_element(self, element):
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';"
            "arguments[0].style.backgroundColor='yellow';",
            element
        )

    def _remove_highlight(self, element):
        self.driver.execute_script(
            "arguments[0].style.border='';"
            "arguments[0].style.backgroundColor='';",
            element
        )

    def _scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def _step_wrapper(self, step_name, action, element=None):
        with allure.step(step_name):
            try:
                result = action()
                self._attach_log(f"SUCCESS: {step_name}")
                # Protect screenshot so it doesn't mask a successful action
                try:
                    self._attach_screenshot(step_name, element)
                except Exception as e:
                    # Log silently to Allure and continue
                    try:
                        self._attach_log(f"Screenshot failed after success: {e}")
                    except Exception:
                        pass
                return result
            except Exception as e:
                self._attach_log(f"FAILED: {step_name}\nError: {str(e)}")
                # Try to attach failure screenshot but don't let it override original exception
                try:
                    self._attach_screenshot(f"{step_name} - Failed", element)
                except Exception:
                    pass
                raise

    # ==========================
    # Element Methods
    # ==========================

    def find_locator(self, locator, element_name="Element"):
        def action():
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )

        return self._step_wrapper(
            f"Find {element_name}",
            action
        )

    def find_locators(self, locator, element_name="Elements"):
        def action():
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )

        return self._step_wrapper(
            f"Find {element_name}",
            action
        )

    def click(self, locator, element_name="Element"):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        def action():
            element.click()

        return self._step_wrapper(
            f"Click on {element_name}",
            action,
            element
        )

    def send_text(self, locator, text, element_name="Element"):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        def action():
            element.clear()
            element.send_keys(text)

        return self._step_wrapper(
            f"Enter text into {element_name}",
            action,
            element
        )

    def get_text(self, locator, element_name="Element"):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        def action():
            return element.text

        return self._step_wrapper(
            f"Get text from {element_name}",
            action,
            element
        )

    def is_visible(self, locator, element_name="Element"):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            self._attach_log(f"{element_name} is visible")
            self._attach_screenshot(
                f"{element_name} Visible",
                element
            )
            return True

        except TimeoutException:
            self._attach_log(f"{element_name} not visible")
            return False

    def wait_and_handle_alert(self):
        def action():
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text

        return self._step_wrapper(
            "Handle Alert Popup",
            action
        )