import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.api_helpers import LytxApiClient
from pages.VideoSerachPage import VideoSearchPage
from data.prod.video_search_data_prod import VideoSearchDataProd

# Define test order - lower numbers run first
pytestmark = pytest.mark.order("vehicle_search")

@pytest.mark.order(1)  # This will run first
@pytest.mark.parametrize("group_name,group_id", VideoSearchDataProd.GROUP_FILTER_TEST_DATA)
@pytest.mark.parametrize("vehicle_name,expected_match", VideoSearchDataProd.VEHICLE_NAME_SEARCH_DATA)
def test_vehicle_name_search(driver, group_name, group_id, vehicle_name, expected_match):
    """
    Test searching for vehicles by vehicle name within a specific group
    
    Steps:
    1. Ensure clean state by resetting any filters
    2. Filter by group first
    3. Click on the search filter dropdown
    4. Select "Vehicle Name" option
    5. Enter vehicle name in search box
    6. Get UI vehicle count
    7. Verify with API vehicle count
    8. Verify that results contain the expected vehicle name
    """
    video_search_page = VideoSearchPage(driver)
    start_time = time.time()
    
    # Ensure clean state by resetting filters first
    try:
        video_search_page.click_reset_button()
        time.sleep(1)  # Brief pause after reset
    except Exception as e:
        print(f"Reset at start (can be ignored if first test): {e}")
        
    # 1. First apply group filter
    print(f"Filtering by group: {group_name}")
    video_search_page.click_group_filter()
    video_search_page.search_group(group_name)
    video_search_page.select_searched_group()
    video_search_page.click_done_button()
    
    # Wait for UI to update after group filtering
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.find_elements(By.XPATH, "//div[contains(@class, 'vehicle-count')]") or
                     not d.find_elements(By.XPATH, "//div[contains(@class, 'loading-indicator')]")
        )
    except:
        time.sleep(1)  # Minimal wait if no indicators found
    
    # 2. Click on search filter dropdown and select vehicle name option
    video_search_page.click_select_search_filter()
    video_search_page.select_vehicle_name_dropdown()
    
    # 3. Enter vehicle name in search box
    video_search_page.search_criteria_textbox(vehicle_name)
    
    # Wait for UI to update after searching
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.find_elements(By.XPATH, "//div[contains(@class, 'vehicle-count')]") or
                     not d.find_elements(By.XPATH, "//div[contains(@class, 'loading-indicator')]")
        )
    except:
        time.sleep(1)  # Minimal wait if no indicators found
    
    # 4. Get vehicle count from UI
    ui_vehicle_count = int(video_search_page.get_vehicle_count())
    print(f"Group: {group_name}, Search term: {vehicle_name}")
    print(f"UI vehicle count: {ui_vehicle_count}")
    
    # 5. Get backend count for the vehicle name search within the filtered group
    api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
    api_count = api_client.get_vehicle_count_by_vehicle_name(vehicle_name, group_id=group_id)
    print(f"API count: {api_count}")

    # 6. Get the vehicle names from the search results (first page only)
    # We need to check the actual vehicle names to verify the search worked correctly
    try:
        # Try to get vehicle column cells (usually the 2nd column)
        vehicle_cells = driver.find_elements(By.XPATH, "//div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[2]")
        vehicle_names = [cell.text.strip() for cell in vehicle_cells if cell.text.strip()]
        print(f"Vehicle names found: {vehicle_names}")
        
        # Check if the expected match is in the results
        expected_found = any(expected_match.lower() in name.lower() for name in vehicle_names)
    except Exception as e:
        print(f"Error getting vehicle names: {str(e)}")
        expected_found = False
    
    # 7. Assertions
    # Check UI count matches API count
    assert ui_vehicle_count == api_count, f"UI count {ui_vehicle_count} != API count {api_count} for vehicle name search: {vehicle_name} in group {group_name}"
    
    # Verify we found vehicles
    assert ui_vehicle_count > 0, f"No vehicles found for search term: {vehicle_name} in group {group_name}"
    
    # Check that we found the expected vehicle (if UI shows any vehicles)
    if ui_vehicle_count > 0 and len(vehicle_names) > 0:
        assert expected_found, f"Expected vehicle '{expected_match}' not found in results for search: {vehicle_name} in group {group_name}"
    
    # Clean up - reset search
    video_search_page.click_reset_button()
    print(f"Test completed in {time.time() - start_time:.1f} seconds")
    

@pytest.mark.order(2)  # This will run second
@pytest.mark.parametrize("group_name,group_id", VideoSearchDataProd.GROUP_FILTER_TEST_DATA)
@pytest.mark.parametrize("serial_number,expected_match", VideoSearchDataProd.SERIAL_NUMBER_SEARCH_DATA)
def test_serial_number_search(driver, group_name, group_id, serial_number, expected_match):
    """
    Test searching for vehicles by serial number within a specific group
    
    Steps:
    1. Ensure clean state by resetting any filters
    2. Filter by group first
    3. Click on the search filter dropdown
    4. Select "Serial Number" option
    5. Enter serial number in search box
    6. Get UI vehicle count
    7. Verify with API vehicle count
    8. Verify that results contain the expected serial number
    """
    video_search_page = VideoSearchPage(driver)
    start_time = time.time()
    
    # Ensure clean state by resetting filters first
    try:
        video_search_page.click_reset_button()
        time.sleep(1)  # Brief pause after reset
    except Exception as e:
        print(f"Reset at start (can be ignored if first test): {e}")
    
    # 1. First apply group filter
    print(f"Filtering by group: {group_name}")
    video_search_page.click_group_filter()
    video_search_page.search_group(group_name)
    video_search_page.select_searched_group()
    video_search_page.click_done_button()
    
    # Wait for UI to update after group filtering
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.find_elements(By.XPATH, "//div[contains(@class, 'vehicle-count')]") or
                     not d.find_elements(By.XPATH, "//div[contains(@class, 'loading-indicator')]")
        )
    except:
        time.sleep(1)  # Minimal wait if no indicators found
    
    # 2. Click on search filter dropdown and select serial number option
    video_search_page.click_select_search_filter()
    video_search_page.select_serial_name_dropdown()
    
    # 3. Enter serial number in search box
    video_search_page.search_criteria_textbox(serial_number)
    
    # Wait for UI to update after searching
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.find_elements(By.XPATH, "//div[contains(@class, 'vehicle-count')]") or
                     not d.find_elements(By.XPATH, "//div[contains(@class, 'loading-indicator')]")
        )
    except:
        time.sleep(1)  # Minimal wait if no indicators found
    
    # 4. Get vehicle count from UI
    ui_vehicle_count = int(video_search_page.get_vehicle_count())
    print(f"Group: {group_name}, Search term: {serial_number}")
    print(f"UI vehicle count: {ui_vehicle_count}")
    
    # 5. Get backend count for the serial number search within the filtered group
    api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
    api_count = api_client.get_vehicle_count_by_serial_number(serial_number, group_id=group_id)
    print(f"API count: {api_count}")

    # 6. Get the device/serial numbers from the search results (first page only)
    # We need to check the actual serial numbers to verify the search worked correctly
    try:
        # Try to get device column cells (usually the 3rd column)
        device_cells = driver.find_elements(By.XPATH, "//div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[3]")
        serial_numbers = [cell.text.strip() for cell in device_cells if cell.text.strip()]
        print(f"Serial numbers found: {serial_numbers}")
        
        # Check if the expected match is in the results
        expected_found = any(expected_match.lower() in serial.lower() for serial in serial_numbers)
    except Exception as e:
        print(f"Error getting serial numbers: {str(e)}")
        expected_found = False
    
    # 7. Assertions
    # Check UI count matches API count
    assert ui_vehicle_count == api_count, f"UI count {ui_vehicle_count} != API count {api_count} for serial number search: {serial_number} in group {group_name}"
    
    # Verify we found vehicles
    assert ui_vehicle_count > 0, f"No vehicles found for search term: {serial_number} in group {group_name}"
    
    # Check that we found the expected serial number (if UI shows any vehicles)
    if ui_vehicle_count > 0 and len(serial_numbers) > 0:
        assert expected_found, f"Expected serial number '{expected_match}' not found in results for search: {serial_number} in group {group_name}"
    
    # Clean up - reset search
    video_search_page.click_reset_button()
    print(f"Test completed in {time.time() - start_time:.1f} seconds")
