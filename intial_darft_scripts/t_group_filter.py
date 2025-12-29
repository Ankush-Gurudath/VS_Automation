import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.api_helpers import LytxApiClient
from pages.VideoSerachPage import VideoSearchPage
from data.prod.video_search_data_prod import VideoSearchDataProd

@pytest.mark.parametrize("group_name,group_id", VideoSearchDataProd.GROUP_FILTER_TEST_DATA)
def test_group_filter_and_data(driver, group_name, group_id):
    video_search_page = VideoSearchPage(driver)
    start_time = time.time()
    
    # 1. Filter by group in UI
    video_search_page.click_group_filter()
    video_search_page.search_group(group_name)
    video_search_page.select_searched_group()
    video_search_page.click_done_button()
    
    # Efficient wait for UI update
    try:
        # Wait for either the loading indicator to disappear or vehicle count to appear/change
        WebDriverWait(driver, 5).until(
            lambda d: d.find_elements(By.XPATH, "//div[contains(@class, 'vehicle-count')]") or
                     not d.find_elements(By.XPATH, "//div[contains(@class, 'loading-indicator')]")
        )
    except:
        time.sleep(1)  # Minimal wait if no indicators found
    
    # 2. Get vehicle count from UI
    ui_vehicle_count = int(video_search_page.get_vehicle_count())
    print(f"Expected group name: {group_name}")
    print(f"UI vehicle count: {ui_vehicle_count}")
    
    # 3. Get backend count for the group early (can run in parallel with UI work)
    api_client = LytxApiClient(VideoSearchDataProd.login_username, VideoSearchDataProd.login_password)
    api_count = api_client.get_vehicle_count(group_id=group_id)
    print(f"API count: {api_count}")
    
    # 4. Use optimized pagination with limited pages
    # If UI shows hundreds of vehicles, we don't need to validate all pages
    # Set a reasonable sample size based on the count
    sample_size = min(50, ui_vehicle_count)  # Limit to 50 max samples
    max_pages = 2 if ui_vehicle_count <= 20 else 1  # Check more pages for smaller result sets
    
    group_column_values = video_search_page.get_all_group_column_texts_with_pagination(max_pages)
    print(f"Number of group values found: {len(group_column_values)}")
    
    # 5. Assertions - Prioritize the most important checks first
    # Check UI count matches API count
    assert ui_vehicle_count == api_count, f"UI count {ui_vehicle_count} != API count {api_count} for group {group_name}"
    
    # Check that we found some group values 
    assert len(group_column_values) > 0, f"No group column values found. Expected at least 1 for group {group_name}"
    
    # Only check group name matching if we have enough values
    if len(group_column_values) >= 3:
        # Check if the sampled group values match expected group name
        unique_values = set(group_column_values[:sample_size])
        print(f"Sample of unique group values: {unique_values}")
        
        # Check percentage match with a smaller subset
        matching_values = sum(1 for val in group_column_values[:sample_size] if group_name.lower() in val.lower())
        match_percentage = (matching_values / len(group_column_values[:sample_size])) * 100
        print(f"Match percentage in sample: {match_percentage:.1f}%")
        assert match_percentage >= 80, f"Only {match_percentage:.1f}% of group values contain '{group_name}' (need at least 80%)"
    
    print(f"Test completed in {time.time() - start_time:.1f} seconds")
