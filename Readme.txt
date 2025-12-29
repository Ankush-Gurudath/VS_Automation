To run only specific test files or a single test file with pytest (and Allure), use the file path in your command. For example:

Run a single test file:

pytest tests/test_login.py --alluredir=allure-results

Run multiple specific files:

pytest tests/test_login.py tests/test_other.py --alluredir=allure-results

Run all tests in a specific folder:

pytest tests/subfolder/ --alluredir=allure-results

You can also specify a single test function within a file:

pytest tests/test_login.py::test_vehicle_count_matches_api --alluredir=allure-results

pytest --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report

run all tests

.\run_tests_with_allure.bat


pytest -v tests/test_LQ_15231.py::TestFilterClearing::test_delete_group_filter

pytest -v tests/test_LQ_15231.py

# Note: If you see USB related errors like:
# [ERROR:components\device_event_log\device_event_log_impl.cc:198] USB: usb_service_win.cc:105 SetupDiGetDeviceProperty(...) failed: Element not found. (0x490)
# These are from the Chrome browser's USB detection and can be safely ignored. They don't affect test execution.