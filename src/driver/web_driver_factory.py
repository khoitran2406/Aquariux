from browser_type import BrowserType
from selenium import webdriver

def init_web_driver(browser_type):
    driver = None
    if browser_type == BrowserType.EDGE:
        driver = __init_edge_driver()
    elif browser_type == BrowserType.CHROME:
        driver = __init_chrome_driver()
    elif browser_type == BrowserType.FIREFOX:
        driver = __init_firefox_driver()

    return driver

def __init_chrome_driver():
    return webdriver.Chrome()

def __init_edge_driver():
    return webdriver.Edge()

def __init_firefox_driver():
    return webdriver.Firefox()