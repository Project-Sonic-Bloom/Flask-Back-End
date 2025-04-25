from selenium import webdriver
from selenium.webdriver.common.by import By


def hello():
    return "hello";

def screenshot():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8100/tabs/home')

    target_element = browser.find_element(By.CLASS_NAME, "map-container")

    target_element.screenshot("Map.png")

    browser.quit()

    return "Screenshot"