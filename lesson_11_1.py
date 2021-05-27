from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as ec
import time

from browser import Browser
from UIElement import UIElement as Element
from dropdown import Dropdown
from actions import Actions

URL = "https://techskillacademy.net/practice/"

# May 25th, 2021
# student Evgeny Abdulin

# Exercise 1.1
def test_double_click():
    """testing double click on an element"""
    browser = Browser(URL, "Firefox")
    actions = Actions(browser)
    test_btn = Element(browser, By.ID, "card")

    # getting the background color of the button before the double click
    test_btn.wait_until_visible()
    background_color = test_btn.get_element().value_of_css_property("background-color")
    background_color_before = Color.from_string(background_color)

    # double-clicking the button
    actions.double_click(test_btn)

    # getting the background color of the button after the double click
    background_color = test_btn.get_element().value_of_css_property("background-color")
    background_color_after = Color.from_string(background_color)

    assert background_color_before != background_color_after

    time.sleep(3)
    browser.shutdown()

# Exercise 1.2
def test_enter_input():
    """testing sending Enter key to an element"""
    browser = Browser(URL, "Firefox")
    actions = Actions(browser)
    # locating the input field
    test_input = Element(browser, By.XPATH, "//aside[@id='key_practice']/input")
    test_input.wait_until_visible()
    # sending Enter
    test_input.click()
    # actions.move_to_element(test_input)
    actions.send_keys_to_element(test_input, Keys.ENTER)
    # locating hidden text "You pressed the key!"
    test_text = Element(browser, By.ID, "hidden_text")
    test_text.wait_until_visible()

    time.sleep(3)
    browser.shutdown()

# Exercise 1.3.1
def test_context_menu_change_color():
    browser = Browser(URL, "Firefox")
    actions = Actions(browser)
    # locating the area
    test_context_area = Element(browser, By.XPATH, "//div[@id='context_menu']")
    test_context_text = Element(browser, By.XPATH, "//div[@id='context_menu']/p")
    # getting the color before click
    background_color = test_context_area.get_element().value_of_css_property("background-color")
    background_color_before = Color.from_string(background_color)
    # right-click
    actions.move_to_element(test_context_text)
    actions.right_click(test_context_text)
    # locating Change Color option and clicking
    change_color_link = Element(browser, By.XPATH, "//li[@onclick='changeColor()']")
    change_color_link.wait_until_visible()
    change_color_link.click()

    # getting the color after click
    background_color = test_context_area.get_element().value_of_css_property("background-color")
    background_color_after = Color.from_string(background_color)

    assert background_color_before != background_color_after

    time.sleep(3)
    browser.shutdown()

# Exercise 1.3.2
def test_context_menu_change_font():
    browser = Browser(URL, "Firefox")
    actions = Actions(browser)
    # locating the area
    test_context_area = Element(browser, By.XPATH, "//div[@id='context_menu']/p")
    # test_context_area = Element(browser, By.ID, "context_menu")
    # getting the font weight before click
    font_weight_before = test_context_area.get_element().value_of_css_property("font-weight")
    # right-click
    # test_context_area.click()
    actions.right_click(test_context_area)
    # locating Change Font option and clicking
    change_color_link = Element(browser, By.XPATH, "//li[@onclick='changeFont()']")
    change_color_link.wait_until_visible()
    change_color_link.click()
    # getting the font weight after click
    font_weight_after = test_context_area.get_element().value_of_css_property("font-weight")

    assert font_weight_before != font_weight_after

    time.sleep(3)
    browser.shutdown()

# Exercise 1.3.3*
def test_context_menu_open_website():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()
    actions = Actions(browser)
    # locating the area
    test_context_area = Element(browser, By.XPATH, "//div[@id='context_menu']/p")
    # test_context_area = Element(browser, By.ID, "context_menu")
    # right-click
    actions.right_click(test_context_area)
    # locating Open TechSkillAcademy option and clicking
    test_link = Element(browser, By.XPATH, "//a[contains(text(),'Open TechSkillAcademy')]")
    test_link.wait_until_visible()
    test_link.click()

    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # browserTabs = browser.get_driver().WindowHandles
    # browser.get_driver().SwitchTo().Window(browserTabs[1])

    browser.get_wd_wait().until(ec.title_contains("CleverOnly"))

    time.sleep(5)
    browser.shutdown()

# Exercise 1.3.4
def test_context_menu_esc():
    browser = Browser(URL, "Firefox")
    actions = Actions(browser)
    # locating the area
    test_context_area = Element(browser, By.XPATH, "//div[@id='context_menu']/p")
    # right-click
    actions.right_click(test_context_area)
    # locating Change Color option to be sure that it is visible and therefore the entire menu is visible
    change_color_link = Element(browser, By.XPATH, "//li[@onclick='changeColor()']")
    change_color_link.wait_until_visible()
    # sending ESC key
    actions.send_keys(Keys.ESCAPE)


    time.sleep(3)
    browser.shutdown()


if __name__ == "__main__":
    # test_double_click()
    # test_enter_input()
    # test_context_menu_change_color()
    # test_context_menu_change_font()
    test_context_menu_open_website()
    # test_context_menu_esc()