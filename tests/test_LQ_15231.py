import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.api_helpers import LytxApiClient
from pages.VideoSerachPage import VideoSearchPage
from data.prod.video_search_data_prod import VideoSearchDataProd

# Define test order
pytestmark = pytest.mark.order("filter_clear")

class TestFilterClearing:
    """
    Test suite for clearing filters in the Video Search page
    Ticket: LQ-15231
    """
    
    @pytest.mark.order(1)
    @pytest.mark.parametrize("group_name,group_id", VideoSearchDataProd.GROUP_FILTER_TEST_DATA)
    def test_delete_group_filter(self, driver, group_name, group_id):
        """
        @P2
        Scenario: Delete the group filter
        Given "Video Reviewer Plus" user is in VIDEO SEARCH
        And the group is in group filter
        And the vehicles in the group are filtered out
        When the user clicks "X" button in group filter
        Then the group filter is cleared
        And the vehicle list is reset
        And the vehicle count number is updated
        """
        video_search_page = VideoSearchPage(driver)
        api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
        
        # Record initial total vehicle count (unfiltered)
        initial_vehicle_count = int(video_search_page.get_vehicle_count())
        print(f"Initial vehicle count: {initial_vehicle_count}")
        
        # 1. Filter by test group
        test_group_name = group_name
        test_group_id = group_id
        
        video_search_page.click_group_filter()
        video_search_page.search_group(test_group_name)
        video_search_page.select_searched_group()
        video_search_page.click_done_button()
        
        # Wait for filtering to complete
        time.sleep(2)
        
        # 2. Verify filtering worked - get filtered count
        filtered_count = int(video_search_page.get_vehicle_count())
        print(f"Filtered count with group '{test_group_name}': {filtered_count}")
        
        # Verify with API
        api_filtered_count = api_client.get_vehicle_count(group_id=test_group_id)
        assert filtered_count == api_filtered_count, f"UI filtered count {filtered_count} doesn't match API count {api_filtered_count}"
        
        # 3. Click X button to clear the group filter
        video_search_page.clear_group_filter()
        
        # Wait for vehicle list to reset
        time.sleep(2)
        
        # 4. Verify filter is cleared and count is reset
        updated_count = int(video_search_page.get_vehicle_count())
        print(f"Count after clearing filter: {updated_count}")
        
        # Verify the count has been reset to initial count
        assert updated_count == initial_vehicle_count, f"Vehicle count after clearing filter ({updated_count}) doesn't match initial count ({initial_vehicle_count})"
        
        # Verify the filter visually appears cleared
        assert not video_search_page.is_group_filter_visible(), "Group filter still appears in UI after clearing"
    
    @pytest.mark.order(2)
    @pytest.mark.parametrize("vehicle_name,expected_match", VideoSearchDataProd.VEHICLE_NAME_SEARCH_DATA)
    def test_delete_vehicle_name_filter(self, driver, vehicle_name, expected_match):
        """
        @P2
        Scenario: Delete the Search by vehicle name filter
        Given "Video Reviewer Plus" user is in VIDEO SEARCH
        And the vehicle name is in search by vehicle name filter
        And all the vehicles that name contains the vehicle name are filtered out
        When the user clicks "X" button in the filter
        Then the search by vehicle name filter is cleared
        And the vehicle list is reset
        And the vehicle count number is updated
        """
        video_search_page = VideoSearchPage(driver)
        api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
        
        # Record initial vehicle count
        initial_vehicle_count = int(video_search_page.get_vehicle_count())
        print(f"Initial vehicle count: {initial_vehicle_count}")
        
        # 1. Set up vehicle name search
        search_term = vehicle_name
        video_search_page.click_select_search_filter()
        video_search_page.select_vehicle_name_dropdown()
        video_search_page.search_criteria_textbox(search_term, press_enter=True)
        
        # Wait for filtering to complete
        time.sleep(2)
        
        # 2. Verify filtering worked
        filtered_count = int(video_search_page.get_vehicle_count())
        print(f"Filtered count with vehicle name '{search_term}': {filtered_count}")
        
        # Verify with API
        api_filtered_count = api_client.get_vehicle_count_by_vehicle_name(search_term)
        assert filtered_count == api_filtered_count, f"UI filtered count {filtered_count} doesn't match API count {api_filtered_count}"
        
        # 3. Click X button to clear the vehicle name filter
        video_search_page.clear_search_filter()
        
        # Wait for vehicle list to reset
        time.sleep(2)
        
        # 4. Verify filter is cleared and count is reset
        updated_count = int(video_search_page.get_vehicle_count())
        print(f"Count after clearing filter: {updated_count}")
        
        # Verify the count has been reset to initial count
        assert updated_count == initial_vehicle_count, f"Vehicle count after clearing filter ({updated_count}) doesn't match initial count ({initial_vehicle_count})"
        
        # Verify the search box is empty
        assert video_search_page.get_search_box_value() == "", "Search box is not empty after clearing filter"
    
    @pytest.mark.order(3)
    @pytest.mark.parametrize("serial_number,expected_match", VideoSearchDataProd.SERIAL_NUMBER_SEARCH_DATA)
    def test_delete_serial_number_filter(self, driver, serial_number, expected_match):
        """
        @P2
        Scenario: Delete the Search by Serial Number filter
        Given "Video Reviewer Plus" user is in VIDEO SEARCH
        And the serial number is in search by Serial Number filter
        And all the vehicles attached ER with the serial number characters are filtered out
        When the user clicks "X" button in the filter
        Then the Serial Number filter is cleared
        And the vehicle list is reset
        And the vehicle count number is updated
        """
        video_search_page = VideoSearchPage(driver)
        api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
        
        # Record initial vehicle count
        initial_vehicle_count = int(video_search_page.get_vehicle_count())
        print(f"Initial vehicle count: {initial_vehicle_count}")
        
        # 1. Set up serial number search
        
        search_term = serial_number
        video_search_page.click_select_search_filter()
        video_search_page.select_serial_number_dropdown()
        video_search_page.search_criteria_textbox(search_term, press_enter=True)
        
        # Wait for filtering to complete
        time.sleep(2)
        
        # 2. Verify filtering worked
        filtered_count = int(video_search_page.get_vehicle_count())
        print(f"Filtered count with serial number '{search_term}': {filtered_count}")
        
        # Verify with API
        api_filtered_count = api_client.get_vehicle_count_by_serial_number(search_term)
        assert filtered_count == api_filtered_count, f"UI filtered count {filtered_count} doesn't match API count {api_filtered_count}"
        
        # 3. Click X button to clear the serial number filter
        video_search_page.clear_search_filter()
        
        # Wait for vehicle list to reset
        time.sleep(2)
        
        # 4. Verify filter is cleared and count is reset
        updated_count = int(video_search_page.get_vehicle_count())
        print(f"Count after clearing filter: {updated_count}")
        
        # Verify the count has been reset to initial count
        assert updated_count == initial_vehicle_count, f"Vehicle count after clearing filter ({updated_count}) doesn't match initial count ({initial_vehicle_count})"
        
        # Verify the search box is empty
        assert video_search_page.get_search_box_value() == "", "Search box is not empty after clearing filter"
    
    @pytest.mark.order(4)
    @pytest.mark.parametrize("serial_number,expected_match", VideoSearchDataProd.SERIAL_NUMBER_SEARCH_DATA)
    def test_vehicle_list_update_on_partial_delete(self, driver, serial_number, expected_match):
        """
        @P2
        Scenario: the vehicle list is updated accordingly when delete the charactors
        Given "Video Reviewer Plus" user is in VIDEO SEARCH
        And the full serial number is in search by Serial Number filter
        And all the vehicles attached ER with the full serial number charactors are filtered out
        When the user deletes some charactors from the filter
        Then the vehicle list is updated accordingly
        And the vehicle count number is updated accordingly
        """
        video_search_page = VideoSearchPage(driver)
        api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
        
        # Record initial vehicle count
        initial_vehicle_count = int(video_search_page.get_vehicle_count())
        print(f"Initial vehicle count: {initial_vehicle_count}")
        
        # 1. Set up serial number search with longer string
        initial_search_term = expected_match  # Use the full/exact match
        video_search_page.click_select_search_filter()
        video_search_page.select_serial_number_dropdown()
        video_search_page.search_criteria_textbox(initial_search_term, press_enter=True)
        
        # Wait for filtering to complete
        time.sleep(2)
        
        # 2. Verify filtering worked
        initial_filtered_count = int(video_search_page.get_vehicle_count())
        print(f"Filtered count with serial number '{initial_search_term}': {initial_filtered_count}")
        
        # Verify with API
        api_initial_filtered_count = api_client.get_vehicle_count_by_serial_number(initial_search_term)
        assert initial_filtered_count == api_initial_filtered_count, \
            f"UI initial filtered count {initial_filtered_count} doesn't match API count {api_initial_filtered_count}"
        
        # 3. Delete some characters from the search term
        partial_search_term = serial_number  # Use the partial search term from the test data
        video_search_page.delete_characters_from_search(partial_search_term)
        
        # Wait for list to update
        time.sleep(2)
        
        # 4. Get updated vehicle count
        updated_filtered_count = int(video_search_page.get_vehicle_count())
        print(f"Updated count with partial serial number '{partial_search_term}': {updated_filtered_count}")
        
        # 5. Verify with API that the count updated correctly
        api_updated_filtered_count = api_client.get_vehicle_count_by_serial_number(partial_search_term)
        assert updated_filtered_count == api_updated_filtered_count, \
            f"UI updated filtered count {updated_filtered_count} doesn't match API count {api_updated_filtered_count}"
        
        # 6. Verify the count changed (should be greater since we're using a broader search)
        assert updated_filtered_count >= initial_filtered_count, \
            f"Updated count {updated_filtered_count} should be >= initial filtered count {initial_filtered_count}"
        
        # 7. Clean up - clear filter
        video_search_page.clear_search_filter()
        
        # Wait for vehicle list to reset
        time.sleep(2)
        
        # 8. Verify filter is cleared and count is reset
        final_count = int(video_search_page.get_vehicle_count())
        assert final_count == initial_vehicle_count, f"Final count {final_count} doesn't match initial count {initial_vehicle_count}"
