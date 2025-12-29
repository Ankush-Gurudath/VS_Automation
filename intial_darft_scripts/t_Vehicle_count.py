from utils.api_helpers import LytxApiClient
from pages.VideoSerachPage import VideoSearchPage
from data.prod.video_search_data_prod import VideoSearchDataProd


def test_vehicle_count_displayed_after_login(driver):
    video_search_page = VideoSearchPage(driver)
    print("vehicle count :", video_search_page.get_vehicle_count())
    print("Vehicle count displayed:", video_search_page.vehicle_count_displayed())
    assert video_search_page.vehicle_count_displayed(), "Vehicle count is not displayed after login."

def test_vehicle_count_matches_api(driver):
    """Verify that the vehicle count displayed in the UI matches the itemCount from the API."""
    api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
    api_count = api_client.get_vehicle_count()
    video_search_page = VideoSearchPage(driver)
    ui_count_text = video_search_page.get_vehicle_count()
    try:
        ui_count = int(ui_count_text)
    except ValueError:
        assert False, f"UI vehicle count is not a number: {ui_count_text}"
    assert ui_count == api_count, f"Mismatch: UI shows {ui_count}, API shows {api_count}"



