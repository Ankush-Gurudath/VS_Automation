class LocatorsVideoSearchPage:
    video_search_page_title_id = 'videoSearchText'
    vehicle_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[1]/div'
    library_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]/div'
    saved_videos_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]/' \
                             'div[2]/div[2]/div[1]/div'
    video_tags_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]' \
                           '/div[2]/div[2]/div[2]'

    # table columns in vehicle page
    actions_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/' \
                                'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                'cdk-header-cell[1]/span/span'
    vehicles_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/' \
                                 'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                 '/cdk-header-cell[2]/span/span'
    device_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div' \
                               '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[3]/span/span'
    last_communicated_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component' \
                                          '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                          'cdk-header-cell[4]/span/span'
    group_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/lx-table/' \
                              'div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[5]/span/span'
    
    
    views_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/lx-table' \
                              '/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[6]/span/span'
    vehicle_count_text_xpath = '//span[contains(text(),"Vehicle")]/parent::div/preceding-sibling::div/div'

    # Filters and select search criteria in vehicle page
    group_filter_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/div/' \
                         'vehicles-list-filter/filter-bar/div/div[2]/div[2]/group-filter/div'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                 '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                  'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div' \
                                  '/ngb-typeahead-window/button[1]'
    done_button_group_filter_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                     '/group-selector/div/div[3]/button[2]'
    reset_button_xpath = '//div[@class="reset-button-text"]'
    select_search_filter_xpath = '/html/body/app-root/shell/div/div/div/ng-component/' \
                                 'div/div/vehicles-list-filter/filter-bar/div/div[2]/div[2]/' \
                                 'dropdown/div/span/span'
    select_vehicle_name_dropdown_xpath = '/html/body/app-root/shell/div/div/div/ng-component' \
                                         '/div/div/vehicles-list-filter/filter-bar/div/div[2]/div[2]' \
                                         '/dropdown/div/div/ul/li[1]'
    select_serial_number_dropdown_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/' \
                                          'div/vehicles-list-filter/filter-bar/div/div[2]/div[2]' \
                                          '/dropdown/div/div/ul/li[2]'
    search_criteria_textbox_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/div' \
                                    '/vehicles-list-filter/filter-bar/div/div[2]/div[2]/div/' \
                                    'lytx-search/div/form/input'

    # table columns in saved videos page
    video_name_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                   'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                   'cdk-header-cell[2]/span/span'
    status_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                               '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[3]/span/span'
    tag_type_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                                 '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                 'cdk-header-cell[4]/span/span'
    vehicle_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                             'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                             'cdk-header-cell[5]/span/span'
    group_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[6]/span/span'
    length_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                               '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[7]/span/span'
    views_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[8]/span/span'
    video_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                                   '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                   'cdk-header-cell[9]/span/span'
    request_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                     'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                     'cdk-header-cell[10]/span/span'
    video_count_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                             'div/event-library-filter/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'
                             
    # Pagination elements
    pagination_next_button_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/device-pagination/div/div[2]/div/div/span[3]'
    pagination_next_button_rel_xpath = "//device-pagination//span[contains(@class, 'page-forward')]"
    pagination_prev_button_xpath = "//device-pagination//span[contains(@class, 'page-back')]"
    pagination_current_page_xpath = "//device-pagination//div[contains(@class, 'page-indicator')]"
    pagination_total_pages_xpath = "//device-pagination//div[contains(@class, 'page-indicator')]"

    video_name_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/lx-table/div[2]/div[2]' \
                       '/cdk-table/cdk-row/cdk-cell[2]/span[2]/video-preview-link/span'
    # Filters and select search criteria in saved videos page
    group_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                                      '/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                      'group-filter/div'
    search_group_textbox_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/' \
                                              'group-selector-modal/group-selector/div' \
                                              '/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/' \
                                               'group-selector-modal/group-selector/div/div[1]/div[2]/div/' \
                                               'lytx-typeahead/div/ngb-typeahead-window/button'
    done_button_group_filter_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                                  'group-selector/div/div[3]/button[2]'
    date_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                     'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                     'lx-date-range-filter/div/div[1]'
    date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter/' \
                                   'filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                   '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[1]'
    date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                 '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[2]'
    date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filte' \
                                  'r/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                  '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[3]'
    date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                 '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[1]'
    date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                               '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                               '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[2]'
    date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter/' \
                                'filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[3]'
    apply_button_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                      'event-library-filter/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                      '/div/div[2]/lx-date-range-selector/div/div[2]/div[2]/div/div[2]/button[2]'
    select_search_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                              '/filter-bar/div/div[2]/div[2]/dropdown/div/span/span'
    video_name_dropdown_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                             'div/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                             'dropdown/div/div/ul/li[1]'
    vehicle_name_dropdown_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                               'event-library-filter/filter-bar/div/div[2]/div[2]/dropdown/div/div/ul/li[2]'
    search_criteria_textbox_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                                                 '/div/event-library-filter/filter-bar/div/div[2]/div[2]/div/' \
                                                 'lytx-search/div/form/input'
    reset_button_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                      'event-library-filter/filter-bar/div/div[2]/div[2]/button'

    # table columns in video tags page
    actions_column_text_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[1]/span/span'
    vehicle_column_video_tags_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[2]/span/span'
    tag_name_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/lx-table/div[2]' \
                                 '/div[2]/cdk-table/cdk-header-row/cdk-header-cell[3]/span/span'
    category_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/lx-table' \
                                 '/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[4]/span/span'
    available_views_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                        '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                        'cdk-header-cell[5]/span/span'
    group_column_video_tag_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                        'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                        '/cdk-header-cell[6]/span/span'
    record_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                    'lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                    '/cdk-header-cell[7]/span/span'
    video_tags_count_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                  '/event-library-filter/filter-bar/div/div[2]/div[1]/div[1]' \
                                  '/div/div[1]/div'

    # Filters and select search criteria on Video tags page
    group_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                    'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                    'group-filter/div/span'
    search_group_textbox_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                            'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                             '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                             'ngb-typeahead-window/button'
    done_button_group_filter_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                                'group-selector/div/div[3]/button[2]'
    reset_button_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                                    '/filter-bar/div/div[2]/div[2]/button'
    date_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                                   '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[1]'
    last_30_days_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter/filter-bar/' \
                                    'div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector/' \
                                    'div/div[2]/div[1]/div[3]'
    apply_date_button_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                         'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                         'lx-date-range-filter/div/div[2]/lx-date-range-selector/' \
                                         'div/div[2]/div[2]/div/div[2]/button[2]'
    category_filter_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                            '/filter-bar/div/div[2]/div[2]/dropdown[1]/div/span/span'
    driver_tagged_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                          '/filter-bar/div/div[2]/div[2]/dropdown[1]/div/div/ul/li[1]'
    select_search_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library' \
                                            '/div/event-library-filter/filter-bar/div/div[2]/div[2]' \
                                            '/dropdown[2]/div/span/span'
    select_tag_name_dropdown_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                                '/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                                'dropdown[2]/div/div/ul/li[1]'
    select_vehicle_name_dropdown_video_tags_xpath = '/html/body/app-root/shell/div/div/div' \
                                                    '/tag-library/div/event-library-filter/filter-bar/' \
                                                    'div/div[2]/div[2]/dropdown[2]/div/div/ul/li[2]'
    search_criteria_textbox_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                               'event-library-filter/filter-bar/div/div[2]/div[2]/div/' \
                                               'lytx-search/div/form/input'

    # Video Player page:
    video_player_title_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/div[1]'
    video_date_xpath = '(//*[@class="video-date"])[1]'
    play_button_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/' \
                        'simultaneous-video-player/div/synchronized-video-player/div[2]/' \
                        'video-player-control-bar/div[1]/div[2]/div/i'
    video_play_time_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/' \
                            'simultaneous-video-player/div/synchronized-video-player/div[2]/' \
                            'video-player-control-bar/div[1]/div[1]/div[1]'

    browse_button_id = 'browseContainer'
    live_button_id = 'liveStream'
    wake_button_id = 'wakeButton'
    video_browser_title_text_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div' \
                                     '/div[1]/div[1]'
    browser_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[1]/div[2]' \
                        '/lytx-tab-views/div/div[1]/button[1]'
    live_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[1]/div[2]' \
                     '/lytx-tab-views/div/div[1]/button[2]'

    outside_view_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/' \
                             'div/div[2]/player-tabs/div/div[2]/div[1]'
    map_live_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                         '/livestream/div/div[1]/div[2]'
    gps_speed_text_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                           '/livestream/div/div[2]/span'

    save_to_library_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                            '/simultaneous-view-browser/div[1]/div[2]/browser-control-bar/div' \
                            '/div[1]/div[3]/div[4]/i'
    video_name_input_box_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[3]' \
                                 '/simultaneous-view-browser/div[1]/div[2]/browser-control-bar/' \
                                 'div/trim-transfer-dialog/div/div/div[1]/div[1]/input'
    save_button_id = 'saveButton'
    go_to_video_button_xpath = '/html/body/ngb-modal-window/div/div/action-modal/lytx-modal-shell' \
                               '/div/div[2]/div[3]/button[2]'
    length_value_id = 'clipLength'
    profile_xpath = '//span[@id="profileButton"]'
    sign_out_button_xpath = '//*[text()="Sign Out"]'
    vehicles_tab_xpath = '//*[text()="Vehicles"]'
    
    # Filter clear button XPaths
    group_filter_clear_xpath = "/html/body/app-root/shell/div/div/div/ng-component/div/div/vehicles-list-filter/filter-bar/div/div[2]/div[2]/group-filter/div/i[2]"
    search_filter_clear_xpath = "//div[contains(@class, 'search')]//span[contains(@class, 'clear-search-icon')]"
    search_box_xpath = "//div[contains(@class, 'search')]//input"
    group_filter_items_xpath = "//div[contains(@class, 'filter-container')]//div[contains(@class, 'filter-item')]"
