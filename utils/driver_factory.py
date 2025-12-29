from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser {browser} is not supported")

    driver.implicitly_wait(10)
    return driver
