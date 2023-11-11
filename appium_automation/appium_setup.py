import time, os, shutil
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction

def setup_appium():
    caps:Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'emulator-5554',
        'appPackage':'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        "language": 'en',
        'locale': 'US'
    }

    url = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps))

    # Set an implicit wait
    driver.implicitly_wait(10)  # Wait for 10 seconds

    # Navigating to Amazon
    driver.get("https://www.amazon.in/s?k=Hindi+Books&page=2&crid=2PHNZ8RO3WZ88&qid=1699690596&sprefix=hindi+boo%2Caps%2C337&ref=is_ps_1")
    
    time.sleep(10)
    for i in range(8):  
        # Scroll down
        touch = TouchAction(driver)
        touch.press(x=500, y=1000).move_to(x=500, y=500).release().perform()

        # Take a screenshot
        driver.get_screenshot_as_file(f"screenshot{i}.png")

        # Wait a bit for the page to load
        time.sleep(2)

    source_dir = os.getcwd()  # This gets the current directory
    target_dir = os.path.join(source_dir, "screenshots")

    os.makedirs(target_dir, exist_ok=True)

    for i in range(8):  # Adjust the range to 9 to include screenshot8
        filename = f"screenshot{i}.png"
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)

        # Check if the file exists and then move the file
        if os.path.isfile(source_file):
            shutil.move(source_file, target_file)

    driver.quit()
