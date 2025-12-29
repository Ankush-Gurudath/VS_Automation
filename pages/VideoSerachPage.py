from time import sleep
import time

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators_video_search_page import LocatorsVideoSearchPage as VS
from pages.base_page import BasePage


class VideoSearchPage(BasePage):

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_video_search_title(self):
        return self.get_text((By.ID, VS.video_search_page_title_id))

    def click_vehicle_tab(self):
        self.click((By.XPATH, VS.vehicle_tab_xpath))

    def click_library_tab(self):
        self.click((By.XPATH, VS.library_tab_xpath))

    def click_saved_videos_tab(self):
        self.click((By.XPATH, VS.saved_videos_tab_xpath))

    def click_video_tags_tab(self):
        self.click((By.XPATH, VS.video_tags_tab_xpath))

    # table columns in vehicle page
    def get_vehicle_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.vehicle_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.vehicle_count_text_xpath))

    def get_actions_column_text(self):
        return self.get_text((By.XPATH, VS.actions_column_text_xpath))

    def get_vehicles_column_text(self):
        return self.get_text((By.XPATH, VS.vehicles_column_text_xpath))

    def get_device_column_text(self):
        return self.get_text((By.XPATH, VS.device_column_text_xpath))

    def get_last_communicated_column_text(self):
        return self.get_text((By.XPATH, VS.last_communicated_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, VS.group_column_text_xpath))

    def get_views_column_text(self):
        return self.get_text((By.XPATH, VS.views_column_text_xpath))

    # Filters and select search criteria in Vehicle page
    def click_group_filter(self):
        self.click((By.XPATH, VS.group_filter_xpath))

    def search_group(self, group_name):
        """
        Enters a group name in the search field of the group filter.
        :param group_name: Name of the group to search for
        """
        self.type((By.XPATH, VS.search_group_textbox_xpath), group_name)
        # Wait a bit for search results to appear
        sleep(2)

    def select_searched_group(self):
        self.click((By.XPATH, VS.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, VS.done_button_group_filter_xpath))

    def get_all_group_column_texts(self):
        """
        Returns a list of all group column values from the vehicle table.
        Optimized version that tries to find the group column faster.
        """
        try:
            # Faster, more targeted approach - use a direct XPath for the group column cells
            # This XPath targets specifically the 5th column (group column) cells in the table
            direct_xpath = "//div/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[5]"
            
            # Try the direct approach first with a short timeout
            try:
                WebDriverWait(self.driver, 2).until(
                    lambda d: len(d.find_elements(By.XPATH, direct_xpath)) > 0
                )
                group_cells = self.driver.find_elements(By.XPATH, direct_xpath)
                print(f"Found {len(group_cells)} elements with direct XPath")
                
                # Get text from cells
                values = []
                for cell in group_cells:
                    try:
                        text = cell.text.strip()
                        if text and text.lower() != "group":  # Filter out header text
                            values.append(text)
                    except StaleElementReferenceException:
                        continue
                
                print(f"Extracted {len(values)} text values")
                return values
                
            except Exception:
                print("Direct XPath failed, trying JavaScript approach...")
                
            # JavaScript approach as fallback - often faster and more reliable with complex DOM
            try:
                # Use JavaScript to extract all text values from the group column
                js_result = self.driver.execute_script("""
                    const rows = document.querySelectorAll('cdk-row');
                    const values = [];
                    
                    // Try to find the group column index
                    const headers = document.querySelectorAll('cdk-header-cell');
                    let groupIndex = 4; // Default to 5th column (0-indexed)
                    
                    // Look for header with "GROUP" text to confirm index
                    for (let i = 0; i < headers.length; i++) {
                        if (headers[i].textContent.toUpperCase().includes('GROUP')) {
                            groupIndex = i;
                            break;
                        }
                    }
                    
                    // Extract text from each row's group column cell
                    for (const row of rows) {
                        const cells = row.querySelectorAll('cdk-cell');
                        if (cells.length > groupIndex) {
                            const text = cells[groupIndex].textContent.trim();
                            if (text && text.toLowerCase() !== 'group') {
                                values.push(text);
                            }
                        }
                    }
                    return values;
                """)
                
                if js_result and len(js_result) > 0:
                    print(f"JavaScript approach found {len(js_result)} values")
                    return js_result
            except Exception as e:
                print(f"JavaScript approach failed: {str(e)}")
            
            # If both optimized approaches fail, fall back to the original method
            print("Falling back to original method...")
            
            # Try multiple possible XPath patterns to find the rows and cells
            possible_xpaths = [
                "//cdk-table/cdk-row/cdk-cell[5]",
                "//lx-table//cdk-table/cdk-row/cdk-cell[5]"
            ]
            
            # Try each pattern
            group_cells = []
            for xpath in possible_xpaths:
                try:
                    WebDriverWait(self.driver, 1).until(
                        lambda d: len(d.find_elements(By.XPATH, xpath)) > 0
                    )
                    group_cells = self.driver.find_elements(By.XPATH, xpath)
                    if len(group_cells) > 0:
                        break
                except:
                    continue
            
            # Get text from cells
            values = []
            for cell in group_cells:
                try:
                    text = cell.text.strip()
                    if text and text.lower() != "group":
                        values.append(text)
                except:
                    pass
            
            return values
            
        except Exception as e:
            print(f"Error in get_all_group_column_texts: {str(e)}")
            return []

    def click_select_search_filter(self):
        self.click((By.XPATH, VS.select_search_filter_xpath))

    def select_vehicle_name_dropdown(self):
        self.click((By.XPATH, VS.select_vehicle_name_dropdown_xpath))

    def select_serial_name_dropdown(self):
        self.click((By.XPATH, VS.select_serial_number_dropdown_xpath))
        
    def select_serial_number_dropdown(self):
        self.click((By.XPATH, VS.select_serial_number_dropdown_xpath))

    def search_criteria_textbox(self, searched_name, press_enter=False):
        """
        Enters text into the search criteria textbox
        Args:
            searched_name: The text to enter
            press_enter: Whether to press Enter after entering the text
        """
        self.type((By.XPATH, VS.search_criteria_textbox_xpath), searched_name)
        
        if press_enter:
            search_box = self.find((By.XPATH, VS.search_criteria_textbox_xpath))
            search_box.send_keys(Keys.ENTER)

    def click_reset_button(self):
        self.click((By.XPATH, VS.reset_button_xpath))

    # table columns in saved videos page
    def get_video_name_column_text(self):
        return self.get_text((By.XPATH, VS.video_name_column_text_xpath))

    def get_status_column_text(self):
        return self.get_text((By.XPATH, VS.status_column_text_xpath))

    def get_tag_type_column_text(self):
        return self.get_text((By.XPATH, VS.tag_type_column_text_xpath))

    def get_vehicle_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.vehicle_column_saved_videos_text_xpath))

    def get_group_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.group_column_saved_videos_text_xpath))

    def get_length_column_text(self):
        return self.get_text((By.XPATH, VS.length_column_text_xpath))

    def get_views_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.views_column_saved_videos_text_xpath))

    def get_video_date_column_text(self):
        return self.get_text((By.XPATH, VS.video_date_column_text_xpath))

    def get_request_date_column_text(self):
        return self.get_text((By.XPATH, VS.request_date_column_text_xpath))

    def get_video_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.video_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.video_count_text_xpath))

    # Filters and select search criteria in video tags page
    def click_group_filter_saved_videos(self):
        self.click((By.XPATH, VS.group_filter_saved_videos_xpath))

    def search_group_saved_videos(self, group_name):
        self.type((By.XPATH, VS.search_group_textbox_saved_videos_xpath), group_name)

    def select_searched_group_saved_videos(self):
        self.click((By.XPATH, VS.select_searched_group_saved_videos_xpath))

    def done_button_saved_videos(self):
        self.click((By.XPATH, VS.done_button_group_filter_saved_videos_xpath))

    def click_date_filter_saved_videos(self):
        self.click((By.XPATH, VS.date_filter_saved_videos_xpath))

    def set_video_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, VS.date_range_start_month_xpath))
        self.type((By.XPATH, VS.date_range_start_month_xpath), start_month)
        self.click((By.XPATH, VS.date_range_start_day_xpath))
        self.type((By.XPATH, VS.date_range_start_day_xpath), start_day)
        self.click((By.XPATH, VS.date_range_start_year_xpath))
        self.type((By.XPATH, VS.date_range_start_year_xpath), start_year)
        self.click((By.XPATH, VS.date_range_end_month_xpath))
        self.type((By.XPATH, VS.date_range_end_month_xpath), end_month)
        self.click((By.XPATH, VS.date_range_end_day_xpath))
        self.type((By.XPATH, VS.date_range_end_day_xpath), end_day)
        self.click((By.XPATH, VS.date_range_end_year_xpath))
        self.type((By.XPATH, VS.date_range_end_year_xpath), end_year)

    def click_apply_saved_videos(self):
        self.click((By.XPATH, VS.apply_button_saved_videos_xpath))

    def click_select_search_filter_saved_videos(self):
        self.click((By.XPATH, VS.select_search_filter_saved_videos_xpath))

    def select_video_name_dropdown_saved_videos(self):
        self.click((By.XPATH, VS.video_name_dropdown_saved_videos_xpath))

    def select_vehicle_name_dropdown_saved_videos(self):
        self.click((By.XPATH, VS.vehicle_name_dropdown_saved_videos_xpath))

    def search_criteria_textbox_saved_videos(self, searched_name):
        self.type((By.XPATH, VS.search_criteria_textbox_saved_videos_xpath), searched_name)

    def click_reset_button_saved_videos(self):
        self.click((By.XPATH, VS.reset_button_saved_videos_xpath))

    # table columns in video tags page
    def get_actions_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.actions_column_text_video_tags_xpath))

    def get_vehicle_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.vehicle_column_video_tags_text_xpath))

    def get_tag_name_column_text(self):
        return self.get_text((By.XPATH, VS.tag_name_column_text_xpath))

    def get_category_column_text(self):
        return self.get_text((By.XPATH, VS.category_column_text_xpath))

    def get_available_views_column_text(self):
        return self.get_text((By.XPATH, VS.available_views_column_text_xpath))

    def get_group_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.group_column_video_tag_text_xpath))

    def get_record_date_column_text(self):
        return self.get_text((By.XPATH, VS.record_date_column_text_xpath))

    def get_video_tags_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.video_tags_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.video_tags_count_text_xpath))

    # Filters and select search criteria in video tags page
    def click_group_filter_video_tags(self):
        self.click((By.XPATH, VS.group_filter_video_tags_xpath))

    def search_group_video_tags(self, group_name):
        self.type((By.XPATH, VS.search_group_textbox_video_tags_xpath), group_name)

    def select_searched_group_video_tags(self):
        self.click((By.XPATH, VS.select_searched_group_video_tags_xpath))

    def click_done_button_video_tags(self):
        self.click((By.XPATH, VS.done_button_group_filter_video_tags_xpath))

    def click_date_filter_video_tags(self):
        self.click((By.XPATH, VS.date_filter_video_tags_xpath))

    def select_last_30_days_video_tags(self):
        self.click((By.XPATH, VS.last_30_days_video_tags_xpath))

    def click_apply_button_video_tags(self):
        self.click((By.XPATH, VS.apply_date_button_video_tags_xpath))

    def click_category_filter(self):
        self.click((By.XPATH, VS.category_filter_xpath))

    def select_driver_tagged(self):
        self.click((By.XPATH, VS.driver_tagged_xpath))

    def click_reset_button_video_tags(self):
        self.click((By.XPATH, VS.reset_button_video_tags_xpath))

    def click_select_search_filter_video_tags(self):
        self.click((By.XPATH, VS.select_search_filter_video_tags_xpath))

    def select_tag_name_dropdown_video_tags(self):
        self.click((By.XPATH, VS.select_tag_name_dropdown_video_tags_xpath))

    def select_vehicle_name_dropdown_video_tags(self):
        self.click((By.XPATH, VS.select_vehicle_name_dropdown_video_tags_xpath))

    def search_criteria_textbox_video_tags(self, searched_name):
        self.type((By.XPATH, VS.search_criteria_textbox_video_tags_xpath), searched_name)

    def wake_button_is_displayed(self):
        return self.element_is_displayed((By.ID, VS.wake_button_id))

    def click_wake_button(self):
        self.click((By.ID, VS.wake_button_id))

    def click_browse_button(self):
        self.wait_for_element_displayed((By.ID, VS.browse_button_id))
        self.click((By.ID, VS.browse_button_id))

    def click_live_button(self):
        self.wait_for_element_displayed((By.ID, VS.live_button_id))
        self.click((By.ID, VS.live_button_id))

    def browser_tab_is_active(self):
        return 'active' in self.get_attribute((By.XPATH, VS.browser_tab_xpath), "class")

    def live_tab_is_active(self):
        return 'active' in self.get_attribute((By.XPATH, VS.live_tab_xpath), "class")

    def get_video_browser_title(self, video_browser):
        return self.wait_for_expected_text((By.XPATH, VS.video_browser_title_text_xpath), video_browser)

    def outside_view_live_tab_is_active(self):
        return 'selected' in self.get_attribute((By.XPATH, VS.outside_view_tab_xpath), "class")

    def map_displayed_live_tab(self):
        return self.element_is_displayed((By.XPATH, VS.map_live_tab_xpath))

    def get_gps_speed_text(self, gps_speed):
        return self.wait_for_expected_text((By.XPATH, VS.gps_speed_text_xpath), gps_speed)

    def click_video_name(self):
        self.click((By.XPATH, VS.video_name_xpath))

    def get_video_player_title(self, expected_text):
        return self.wait_for_expected_text((By.XPATH, VS.video_player_title_xpath), expected_text)

    def video_play_time(self):
        return self.get_text((By.XPATH, VS.video_play_time_xpath))

    def video_play_time_changed(self, play_time):
        return self.wait_for_expected_text_change((By.XPATH, VS.video_play_time_xpath), play_time)

    def click_browser_tab(self):
        self.click((By.XPATH, VS.browser_tab_xpath))

    def click_save_to_library(self):
        self.click((By.XPATH, VS.save_to_library_xpath))

    def type_video_name(self, video_name):
        self.type((By.XPATH, VS.video_name_input_box_xpath), video_name)

    def click_save_button(self):
        self.click((By.ID, VS.save_button_id))

    def click_go_to_video_button(self):
        self.wait_for_element_displayed((By.XPATH, VS.go_to_video_button_xpath))
        self.click((By.XPATH, VS.go_to_video_button_xpath))

    def video_length_duration_is_displayed(self):
        self.wait_for_element_displayed((By.ID, VS.length_value_id))
        return self.element_is_displayed((By.ID, VS.length_value_id))

    def click_profile_icon(self):
        self.click((By.XPATH, VS.profile_xpath))

    def click_sign_out_button(self):
        self.click((By.XPATH, VS.sign_out_button_xpath))
        sleep(3)

    def vehicle_count_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.vehicle_count_text_xpath))

    def get_vehicle_count_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, VS.video_tags_count_text_xpath))
        return result

    def video_tag_count_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, VS.vehicle_count_text_xpath))
        return result

    def get_row_count_for_video_tag(self):
        result = self.element_is_displayed((By.TAG_NAME, "cdk-row"))
        return result

    def click_vehicles_tab(self):
        self.click((By.XPATH, VS.vehicles_tab_xpath))

    def get_video_date(self):
        self.wait_for_element_displayed((By.XPATH, VS.video_date_xpath))
        return self.get_text((By.XPATH, VS.video_date_xpath))
    
    def click_next_page(self):
        """
        Clicks the next page button in pagination.
        First tries to use the absolute XPath (user provided), then falls back to a relative XPath.
        Returns True if successfully navigated to next page, False if there is no next page.
        """
        from selenium.webdriver.support import expected_conditions as EC
        
        try:
            # Use a shorter timeout for checking pagination to avoid long waits
            WebDriverWait(self.driver, 2).until(
                lambda d: d.find_elements(By.XPATH, VS.pagination_next_button_xpath) or 
                         d.find_elements(By.XPATH, VS.pagination_next_button_rel_xpath)
            )
            
            # Try the absolute XPath first (directly what the user provided)
            try:
                next_button = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, VS.pagination_next_button_xpath))
                )
                # Check if clickable before trying
                if next_button.is_displayed() and next_button.is_enabled():
                    next_button.click()
                    # Small wait for page update
                    sleep(0.5)
                    return True
            except Exception as e:
                print(f"Trying alternate next button: {str(e)}")
            
            # Fall back to the relative XPath
            try:
                next_button = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, VS.pagination_next_button_rel_xpath))
                )
                if next_button.is_displayed() and next_button.is_enabled():
                    next_button.click()
                    # Small wait for page update
                    sleep(0.5)
                    return True
            except Exception:
                # Direct click as last resort (using JavaScript)
                try:
                    self.driver.execute_script(
                        "document.evaluate('/html/body/app-root/shell/div/div/div/ng-component/div/device-pagination/div/div[2]/div/div/span[3]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();"
                    )
                    sleep(0.5)  # Small delay
                    return True
                except Exception as e:
                    print(f"Error using direct JS click: {str(e)}")
                    
            return False
        except Exception as e:
            print(f"No pagination found: {str(e)}")
            return False
    
    def get_current_page_number(self):
        """
        Gets the current page number from the pagination control.
        Returns the current page number or 1 if pagination not found.
        """
        try:
            # Try to find the page indicator
            if self.element_is_displayed((By.XPATH, VS.pagination_current_page_xpath)):
                page_text = self.get_text((By.XPATH, VS.pagination_current_page_xpath))
                # The text might be like "Page 1 of 5"
                if "Page" in page_text and "of" in page_text:
                    return int(page_text.split("of")[0].replace("Page", "").strip())
                # Or it might just show numbers like "1 / 5"
                elif "/" in page_text:
                    return int(page_text.split("/")[0].strip())
            return 1
        except Exception as e:
            print(f"Error getting current page number: {str(e)}")
            return 1
    
    def get_all_group_column_texts_with_pagination(self, max_pages=3):
        """
        Returns a list of all group column values from the vehicle table,
        navigating through up to max_pages of pagination.
        
        Args:
            max_pages (int): Maximum number of pages to check (default: 3)
                             Set to None to check all pages
        """
        all_values = []
        
        # Get values from the first page
        values_on_page = self.get_all_group_column_texts()
        all_values.extend(values_on_page)
        print(f"Found {len(values_on_page)} values on page 1")
        
        # Keep clicking next and getting values until there are no more pages or we reach max_pages
        page = 1
        while page < (max_pages or float('inf')):
            # Try to click next button with a shorter timeout to avoid long waits
            if not self.click_next_page():
                break  # No more pages
                
            page += 1
            values_on_page = self.get_all_group_column_texts()
            all_values.extend(values_on_page)
            print(f"Found {len(values_on_page)} values on page {page}")
            
            # Performance optimization: If we've collected enough data to validate the test
            # (e.g., 50+ records or 3 pages), we can stop to save time
            if len(all_values) >= 50:
                print(f"Collected {len(all_values)} records, stopping pagination to improve performance")
                break
                
        print(f"Total values found across {page} pages: {len(all_values)}")
        return all_values
        
    def clear_group_filter(self):
        """
        Clears the group filter by clicking the X button
        Returns: True if the filter was cleared successfully, False otherwise
        """
        try:
            self.click((By.XPATH, VS.group_filter_clear_xpath))
            return True
        except Exception as e:
            print(f"Error clearing group filter: {str(e)}")
            return False
            
    def clear_search_filter(self):
        """
        Clears the search filter (vehicle name or serial number) by clicking the X button
        Returns: True if the filter was cleared successfully, False otherwise
        """
        try:
            # First check if there's any text in the search box
            search_box_value = self.get_search_box_value()
            if not search_box_value:
                print("Search box is already empty, no need to clear")
                return True
                
            # Multiple approaches to find and click the clear button
            clear_button_xpaths = [
                VS.search_filter_clear_xpath,  # Primary XPath from locators
                "//div[contains(@class, 'search')]//i[contains(@class, 'clear')]",  # Alternative 1
                "//div[contains(@class, 'search')]//span[contains(@class, 'clear')]",  # Alternative 2
                "//lytx-search//i[contains(@class, 'clear')]",  # Alternative 3
                "//form//i[contains(@class, 'clear')]"  # Alternative 4
            ]
            
            clear_button_found = False
            
            for xpath in clear_button_xpaths:
                try:
                    # Wait for the clear button to be clickable
                    WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    
                    # Try to click the clear button
                    clear_button = self.driver.find_element(By.XPATH, xpath)
                    
                    # Scroll to element if needed
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", clear_button)
                    
                    # Try regular click first
                    try:
                        clear_button.click()
                    except:
                        # If regular click fails, try JavaScript click
                        self.driver.execute_script("arguments[0].click();", clear_button)
                    
                    print(f"Successfully clicked clear button using XPath: {xpath}")
                    clear_button_found = True
                    break
                    
                except Exception as e:
                    print(f"Clear button XPath failed: {xpath} - {str(e)}")
                    continue
            
            if not clear_button_found:
                # Final fallback: clear the search box manually
                print("Clear button not found, clearing search box manually")
                search_box = self.driver.find_element(By.XPATH, VS.search_box_xpath)
                search_box.clear()
                search_box.send_keys(Keys.ENTER)
                
            # Wait for the clear operation to complete
            time.sleep(1)
            
            # Verify the search box is now empty
            final_value = self.get_search_box_value()
            if final_value == "":
                print("Search filter cleared successfully")
                return True
            else:
                print(f"Search filter may not be fully cleared. Remaining value: '{final_value}'")
                return False
                
        except Exception as e:
            print(f"Error clearing search filter: {str(e)}")
            # Try one more fallback approach
            try:
                print("Attempting fallback clear method...")
                search_box = self.driver.find_element(By.XPATH, VS.search_box_xpath)
                search_box.clear()
                search_box.send_keys(Keys.ENTER)
                time.sleep(1)
                return True
            except Exception as fallback_error:
                print(f"Fallback clear method also failed: {str(fallback_error)}")
                return False
            
    def get_search_box_value(self):
        """
        Gets the current value in the search box
        Returns: The text value in the search box
        """
        try:
            return self.get_attribute((By.XPATH, VS.search_box_xpath), "value")
        except Exception as e:
            print(f"Error getting search box value: {str(e)}")
            return ""
            
    def is_group_filter_visible(self):
        """
        Check if any group filter items are visible in the UI
        Returns: True if filter items are visible, False otherwise
        """
        elements = self.find_elements((By.XPATH, VS.group_filter_items_xpath))
        return len(elements) > 0
            
    def delete_characters_from_search(self, new_text):
        """
        Clears the search box and enters new text
        Args:
            new_text: The new text to enter in the search box
        """
        try:
            search_box = self.find((By.XPATH, VS.search_box_xpath))
            search_box.clear()
            search_box.send_keys(new_text)
            search_box.send_keys(Keys.ENTER)
            return True
        except Exception as e:
            print(f"Error modifying search text: {str(e)}")
            return False
    
    def get_group_filter_elements(self):
        """
        Get all group filter elements currently displayed in the filter container
        Returns: List of WebElements for group filter items, empty list if none found
        """
        filter_item_xpath = "//div[contains(@class, 'filter-container')]//div[contains(@class, 'filter-item')]"
        return self.find_elements((By.XPATH, filter_item_xpath))
