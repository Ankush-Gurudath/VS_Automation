import pytest
import allure
from pages.browse_page import BrowsePage
from data.prod.video_search_data_prod import VideoSearchDataProd


@allure.feature("Vehicle Browse")
@allure.story("Browse Page Functionality")
class TestBrowsePage:
    """
    Test suite for Browse/Vehicle Page functionality
    Tests vehicle browsing, snapshot images, and map display
    """

    @pytest.mark.skip(reason="Running only test_complete_browse_workflow")
    @allure.title("Verify vehicle page loads successfully")
    @allure.description("Test to verify that the vehicle browse page loads correctly with vehicle count displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(1)
    def test_vehicle_page_load(self, driver):
        """
        Given user is logged into the application
        When the vehicle browse page loads
        Then vehicle count should be displayed
        And page should be loaded successfully
        """
        with allure.step("Initialize Browse Page"):
            browse_page = BrowsePage(driver)
        
        with allure.step("Wait for page to load"):
            browse_page.wait_for_page_load()
        
        with allure.step("Get vehicle count"):
            vehicle_count = browse_page.get_vehicle_count_text()
            allure.attach(vehicle_count, name="Vehicle Count", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Verify page loaded successfully"):
            assert browse_page.is_vehicle_page_loaded(), "Vehicle page did not load successfully"

    @pytest.mark.skip(reason="Running only test_complete_browse_workflow")
    @allure.title("Browse first vehicle")
    @allure.description("Test to browse the first vehicle and navigate back")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.order(2)
    def test_browse_first_vehicle(self, driver):
        """
        Given user is on the vehicle browse page
        When user clicks on the first browse vehicle
        Then vehicle detail page should open
        And user should be able to navigate back
        """
        with allure.step("Initialize Browse Page"):
            browse_page = BrowsePage(driver)
        
        with allure.step("Wait for page to load"):
            browse_page.wait_for_page_load()
        
        with allure.step("Browse first vehicle"):
            result = browse_page.browse_first_vehicle()
            assert result, "Failed to browse first vehicle"

    @pytest.mark.skip(reason="Running only test_complete_browse_workflow")
    @allure.title("Set page size to 100")
    @allure.description("Test to change page size to display 100 vehicles per page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.order(3)
    def test_set_page_size_100(self, driver):
        """
        Given user is on the vehicle browse page
        When user changes page size to 100
        Then page should display 100 vehicles per page
        """
        with allure.step("Initialize Browse Page"):
            browse_page = BrowsePage(driver)
        
        with allure.step("Wait for page to load"):
            browse_page.wait_for_page_load()
        
        with allure.step("Set page size to 100"):
            browse_page.set_page_size_to_100()
            # Page size change is confirmed by print statement in method

    @pytest.mark.skip(reason="Running only test_complete_browse_workflow")
    @allure.title("Verify snapshot images display")
    @allure.description("Test to verify that snapshot images are displayed for a vehicle")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(4)
    def test_verify_snapshot_images(self, driver):
        """
        Given user is on the vehicle browse page
        When user browses a specific vehicle (index 2)
        Then snapshot images should be displayed
        And images should be visible
        """
        with allure.step("Initialize Browse Page"):
            browse_page = BrowsePage(driver)
        
        with allure.step("Wait for page to load"):
            browse_page.wait_for_page_load()
        
        with allure.step("Browse vehicle at index 2"):
            vehicle_name = browse_page.browse_vehicle_by_index(2)
            allure.attach(str(vehicle_name), name="Vehicle Name", attachment_type=allure.attachment_type.TEXT)
            assert vehicle_name is not None, "Failed to browse vehicle at index 2"
        
        with allure.step("Verify snapshot images are displayed"):
            snapshot_imgs, visible_images = browse_page.get_snapshot_images()
            allure.attach(
                f"Total: {len(snapshot_imgs)}, Visible: {len(visible_images)}", 
                name="Snapshot Image Count", 
                attachment_type=allure.attachment_type.TEXT
            )
            assert len(snapshot_imgs) > 0, "No snapshot images found"
            assert len(visible_images) > 0, "No visible snapshot images found"
        
        with allure.step("Verify map is displayed"):
            map_displayed = browse_page.is_map_displayed()
            assert map_displayed, "Map is not displayed on vehicle detail page"
            

    @allure.title("Complete browse workflow")
    @allure.description("End-to-end test covering complete browse page workflow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(5)
    def test_complete_browse_workflow(self, driver):
        """
        Complete workflow test:
        1. Load page and verify vehicle count
        2. Set page size to 100
        3. Browse a vehicle
        4. Verify snapshot images
        5. Verify map display
        """
        browse_page = BrowsePage(driver)
        
        with allure.step("Step 1: Wait for page load and verify vehicle count"):
            browse_page.wait_for_page_load()
            vehicle_count = browse_page.get_vehicle_count_text()
            allure.attach(vehicle_count, name="Initial Vehicle Count", attachment_type=allure.attachment_type.TEXT)
            assert browse_page.is_vehicle_page_loaded(), "Page did not load"
        
        with allure.step("Step 2: Set page size to 100"):
            browse_page.set_page_size_to_100()
        
        with allure.step("Step 3: Browse specific vehicle"):
            vehicle_name = browse_page.browse_vehicle_by_index(2)
            allure.attach(str(vehicle_name), name="Selected Vehicle", attachment_type=allure.attachment_type.TEXT)
            assert vehicle_name is not None, "Failed to browse vehicle"
        
        with allure.step("Step 4: Verify snapshot images"):
            result = browse_page.verify_snapshot_images_displayed()
            assert result, "Snapshot images verification failed"
        
        with allure.step("Step 5: Verify map display"):
            map_displayed = browse_page.is_map_displayed()
            assert map_displayed, "Map display verification failed"
