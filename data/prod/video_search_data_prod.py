class VideoSearchDataProd:


    # vehicle count getting URL
    vehicle_count_url = "https://api.aws.drivecam.net/api/videosearch-api/devices"
    
    # New UI vehicle page URL
    New_UI_vehiclepage_url = "https://app.lytx.com/#/lvs/vehicles"

    VEHICLE_TEST_DATA = [
        ("Vehicle Name","QM40849291"),  # Lab Test group with expected vehicle count
        # Add more (group_id, expected_count) pairs as needed
    ]

    # Login Details
    login_username = "qa_ind_full_access"
    login_password = "Login123!"
    
    # Group filter test data (group_name, group_id)
    GROUP_FILTER_TEST_DATA = [
        ("Lab Test", "5100ffff-60b6-d6cd-18b2-a8a3e03f0000"),
        # ("***FBI Security Test", "5c5f08fe-17f4-e411-8857-02215e5eed57"),
        # Add more (group_name, group_id) pairs as needed
    ]
    
    # Vehicle name search test data (vehicle_name, expected_match)
    VEHICLE_NAME_SEARCH_DATA = [
        ("QM408", "QM40849291"),  # Partial name that should match
        ("QM40849291", "QM40849291"),  # Exact match
    ]
    
    # Serial number search test data (serial_number, expected_match)
    SERIAL_NUMBER_SEARCH_DATA = [
        ("QM408", "QM40849291"),  # Partial serial that should match
        ("QM40849291", "QM40849291"),  # Exact match
    ]