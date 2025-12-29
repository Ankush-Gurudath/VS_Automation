from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage
from locators.locators_login_page import LocatorsLogin as LG
from locators.locators_video_search_page import LocatorsVideoSearchPage as LV


class LoginPage(BasePage):
    # USERNAME = LG.USERNAME
    # PASSWORD = LG.PASSWORD
    LOGIN_BTN = LG.LOGIN_BTN

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        """Validate login by checking for dashboard element after login, with wait and debug info."""

        try:
            dashboard_element = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.ID, LV.video_search_page_title_id))
            )
            return dashboard_element.is_displayed()
        except Exception as e:
            print("Login success element not found. Exception:", e)
            print("Page source after login:\n", self.driver.page_source[:2000])  # Print first 2000 chars
            return False
        
    def enter_username(self, username):
        try:
            self.find((By.ID, LG.username))
        except NoSuchElementException:
            self.click_refresh_button()
            sleep(10)
        except TimeoutException:
            self.click_refresh_button()
            sleep(10)
        finally:
            self.type((By.ID, LG.username), username)

    def enter_password(self, password):
        try:
            self.find((By.ID, LG.password))
        except NoSuchElementException:
            self.click_refresh_button()
            sleep(10)
        except TimeoutException:
            self.click_refresh_button()
            sleep(10)
        finally:
            self.type((By.ID, LG.password), password)

    def click_login(self):
        self.click((By.ID, LG.LOGIN_BTN))
