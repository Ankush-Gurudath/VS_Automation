# Test Ordering in Video Search Test Suite

## Test Execution Order

This project uses pytest's ordering mechanisms to control the sequence of test execution. Here's how it works:

### Current Order Setup

1. Tests are ordered using the `@pytest.mark.order()` decorator
2. Lower numbers run first (e.g., order(1) runs before order(2))
3. Tests within the same order number run in the order they appear in the file

### Files with Ordering

- `test_vehicle_search.py`:
  - `test_vehicle_name_search` runs first (order 1)
  - `test_serial_number_search` runs second (order 2)

### Required Plugin

To make the ordering work, you need to install the pytest-ordering plugin:

```
pip install pytest-ordering
```

## Test State Management

Each test is designed to be independent by:

1. Resetting filters at the start of each test
2. Resetting filters at the end of each test

This double reset approach ensures that:
- Tests don't interfere with each other
- If a test fails, subsequent tests start with a clean state
- The order of execution doesn't affect test results

## Running Tests in Order

To run tests in their defined order:

```
pytest -v tests/test_vehicle_search.py
```

To run specific tests:

```
pytest -v tests/test_vehicle_search.py::test_vehicle_name_search
pytest -v tests/test_vehicle_search.py::test_serial_number_search
```

## Common Issues

If tests are not running in the expected order:

1. Verify pytest-ordering is installed
2. Check that the order numbers are correctly applied
3. Look for conflicts with other pytest plugins

If tests are interfering with each other:

1. Make sure the reset button is working correctly
2. Add explicit waits after resets
3. Consider implementing a more robust reset mechanism if needed
