from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import time

from browser import Browser
from UIElement3 import UIElement as Element
from dropdown2 import Dropdown
from navigation_bar import NavigationBar
from actions_fixed import Actions

URL = "https://techskillacademy.net/brainbucket/index.php"

# May 28th, 2021
# student Evgeny Abdulin

def test_basic():
    """sequential testing clicking on elements"""
    browser = Browser(URL, "Firefox")
    # actions = Actions(browser)
    delay_between_pages = 1.5
    navigation_bar = NavigationBar(browser)
    # sequential clicking on all new elements
    navigation_bar.show_printers()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Printers"

    time.sleep(delay_between_pages)
    navigation_bar.show_scanners()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Scanners"

    time.sleep(delay_between_pages)
    navigation_bar.show_webcams()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Web Cameras"

    time.sleep(delay_between_pages)
    navigation_bar.show_all_phones_and_pdas()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Phones & PDAs"

    time.sleep(delay_between_pages)
    navigation_bar.show_pdas()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "PDAs"

    time.sleep(delay_between_pages)
    navigation_bar.show_phones()
    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Phones"

    time.sleep(delay_between_pages)

    time.sleep(3)
    browser.shutdown()

def test_all_pc():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all PCs
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_pcs()

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "PC"

    # calculating number of products in PC category
    number_of_products = len(driver.find_elements_by_class_name("product-thumb"))

    if number_of_products == 0:
        print("There are no products to list in this category.")

    time.sleep(3)
    browser.shutdown()

def test_all_macs():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all Macs
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_mac_desktops()
    # receiving the option of the dropdown as a string
    option_text = navigation_bar._option_text
    # slicing the string to extract the number of Macs
    number_from_option = int(option_text[option_text.find("(")+1:option_text.find(")")])

    # calculating number of products in PC category
    number_of_products = len(driver.find_elements_by_class_name("product-thumb"))

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "Mac"

    assert number_of_products == number_from_option

    time.sleep(3)
    browser.shutdown()

def test_all_desktops():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all desktops
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_all_desktops()

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "Desktops"

    time.sleep(3)
    browser.shutdown()

# Exercise #2
# Make the test fail by providing an incorrect xpath, verify that the error message is shown in the console and screenshot is saved
def test_all_desktops_fail():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all desktops
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_all_desktops()

    section_title = Element(browser, By.XPATH, "//f[@id='content14']").get_text()

    assert section_title == "Desktops"

    time.sleep(3)
    browser.shutdown()

# Exercise #3
# Create a program that will:
# ask a user to enter the date in the specified format(ex: "YYYY-MM-DD")
# catch an exception if the user provides the date in the wrong format and prints a custom message
# return what's a day of the week this date corresponds to (ex: Sunday)

def input_date(date_str=""):
    if date_str == "":
        date_str = input("Please enter date in the specified format(YYYY-MM-DD):")
    try:
        date_time_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Incorrect format of the date")
    else:
        print("The day of the week for the date you entered is: ", datetime.strftime(date_time_obj, "%A"))

# Test your program with multiple date and formats
def test_input_date():
    test_date_str = ("YYYY-MM-DD", "date", "989", "12-04-1961", "04-12-1961", "987-05-09", "1961-4-12", "1961-04-12")
    for t_date in test_date_str:
        input_date(t_date)


if __name__ == "__main__":
    # test_basic()
    # test_all_pc()
    # test_all_macs()
    # test_all_desktops()

    # test_all_desktops_fail()
    # input_date()
    test_input_date()