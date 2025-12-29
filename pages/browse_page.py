from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage


class BrowsePage(BasePage):
    """Page Object for Browse/Vehicle Page"""
    
    # Locators
    VIDEO_SEARCH_TEXT = (By.ID, "videoSearchText")
    VEHICLE_COUNT = (By.XPATH, '//div[@data-test-id="filter-headerBar-countValue"]')
    PAGE_SIZE_DROPDOWN = (By.XPATH, '//*[@id="pageSizeDropdown"]/div/span/span')
    PAGE_SIZE_100_OPTION = (By.XPATH, '//*[@id="pageSizeDropdown"]/div/div/ul/li[3]/span')
    BROWSE_VEHICLES = (By.XPATH, '//*[@id="browseText"]')
    VEHICLE_NAME = (By.XPATH, '//div[contains(@class, "browse-vehicle__header-bar__vehicle")]')
    SNAPSHOT_IMAGES = (By.XPATH, "//simultaneous-view-browser[@id='simultaneousViewBrowser']//img[contains(@class, 'simultaneous-view-browser__views__snapshot__image')]")
    MAP_NAME = (By.XPATH, '//*[@id="simultaneousViewBrowser"]/div[1]/div[1]/simultaneous-view[3]/div/div[1]/div/div[1]/div')
    MAP_ELEMENT = (By.XPATH, '//*[@id="simultaneousViewBrowser"]/div[1]/div[1]/simultaneous-view[3]/div/div[2]/div')
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 30)

    def wait_for_page_load(self):
        """Wait for browse/vehicle page to fully load"""
        sleep(15)
        self.driver.implicitly_wait(10)
        element = self.find(self.VIDEO_SEARCH_TEXT)
        print(f"Video search text element - Displayed: {element.is_displayed()}, Enabled: {element.is_enabled()}")
        self.click(self.VIDEO_SEARCH_TEXT)
        sleep(10)

    def get_vehicle_count_text(self):
        """Get the vehicle count text displayed on the page"""
        sleep(10)
        vehicle_count_element = self.find(self.VEHICLE_COUNT)
        count_text = vehicle_count_element.text
        print(f"Number of Vehicles displayed are: {count_text}")
        return count_text

    def is_vehicle_page_loaded(self):
        """Check if vehicle page is loaded successfully"""
        vehicle_count_element = self.find(self.VEHICLE_COUNT)
        is_loaded = vehicle_count_element.is_displayed()
        if is_loaded:
            print("Vehicle page loaded successfully")
        else:
            print("Vehicle page did not load")
        return is_loaded

    def set_page_size_to_100(self):
        """Set the page size to 100 vehicles per page"""
        dropdown_toggle = self.find(self.PAGE_SIZE_DROPDOWN)
        dropdown_toggle.click()
        sleep(5)
        
        option_100 = self.find(self.PAGE_SIZE_100_OPTION)
        option_100.click()
        sleep(10)
        print("Clicked on 100 page size option")

    def browse_first_vehicle(self):
        """Click on the first browse vehicle and navigate back"""
        browse_vehicles = self.find_elements(self.BROWSE_VEHICLES)
        print(f"Total browse vehicles displayed: {len(browse_vehicles)}")
        
        if browse_vehicles:
            vehicle = browse_vehicles[0]
            self.scroll_into_view(vehicle)
            self.wait.until(EC.element_to_be_clickable(self.BROWSE_VEHICLES))
            vehicle.click()
            print("Clicked on the first browse vehicle.")
            sleep(10)
            self.back()
            sleep(5)
            print("Navigated back to the Vehicles page.")
            return True
        else:
            print("No browse vehicles found.")
            return False

    def browse_vehicle_by_index(self, index):
        """Browse a specific vehicle by index and return vehicle name"""
        browse_vehicles = self.find_elements(self.BROWSE_VEHICLES)
        
        if len(browse_vehicles) > index:
            vehicle = browse_vehicles[index]
            self.scroll_into_view(vehicle)
            self.wait.until(EC.element_to_be_clickable(self.BROWSE_VEHICLES))
            vehicle.click()
            sleep(10)
            
            vehicle_name_element = self.find(self.VEHICLE_NAME)
            vehicle_name = vehicle_name_element.text
            print(f"Clicked on the vehicle: {vehicle_name}")
            return vehicle_name
        else:
            print(f"No vehicle found at index {index}")
            return None

    def get_snapshot_images(self):
        """Get all snapshot images and their details"""
        wait = WebDriverWait(self.driver, 30)
        
        snapshot_imgs = wait.until(
            EC.presence_of_all_elements_located(self.SNAPSHOT_IMAGES)
        )
        
        print(f"✅ Found {len(snapshot_imgs)} snapshot images.")
        
        visible_images = []
        for idx, img in enumerate(snapshot_imgs, start=1):
            is_visible = img.is_displayed()
            src = img.get_attribute("src")
            print(f"📸 Image {idx}: Visible = {is_visible}, src starts with = {src[:30] if src else 'N/A'}...")
            
            if is_visible:
                print(f"✅ Image {idx} is currently displayed.")
                visible_images.append(img)
            else:
                print(f"⚠️ Image {idx} is hidden or not visible.")
        
        return snapshot_imgs, visible_images

    def verify_snapshot_images_displayed(self):
        """Verify that snapshot images are displayed"""
        try:
            snapshot_imgs, visible_images = self.get_snapshot_images()
            return len(visible_images) > 0
        except Exception as e:
            print(f"❌ Error occurred while verifying snapshot images: {str(e)}")
            return False

    def is_map_displayed(self):
        """Check if map element is displayed"""
        try:
            map_name_element = self.find(self.MAP_NAME)
            map_element = self.find(self.MAP_ELEMENT)
            
            is_displayed = map_name_element.is_displayed() and map_element.is_displayed()
            
            if is_displayed:
                print("✅ Map is displayed successfully.")
            else:
                print("❌ Map is not displayed.")
                
            return is_displayed
        except Exception as e:
            print(f"❌ Error occurred while verifying map: {str(e)}")
            return False

    def scroll_into_view(self, element):
        """Scroll element into view"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
