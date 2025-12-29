import pytest
from utils.driver_factory import get_driver


from pages.login_page import LoginPage
from data.prod.video_search_data_prod import VideoSearchDataProd

@pytest.fixture(scope="session")
def driver():
    driver = get_driver("chrome")
    login_page = LoginPage(driver)
    driver.get(VideoSearchDataProd.New_UI_vehiclepage_url)
    login_page.login(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
    assert login_page.is_login_successful(), "Login was not successful."
    yield driver
    driver.quit()
