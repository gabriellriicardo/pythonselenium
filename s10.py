from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get("https://www.instagram.com")
time.sleep(5)
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input").send_keys("stephany_viitoriia")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys("ig@22803" + Keys.RETURN)
time.sleep(10)
driver.get("https://www.segue10.com/signin")
time.sleep(5)
driver.find_element_by_css_selector("#email").send_keys("user")
driver.find_element_by_css_selector("#password").send_keys("s122803" + Keys.RETURN)
time.sleep(5)
print("oi kkkk")
driver.find_element_by_css_selector("#modal-profile-warning > div > div > div.flex.align-items-center > button.btn.bg-primary.white-text.waves-effect.waves-light.flex.align-items-center.hide-on-small-only").click()
time.sleep(4)
driver.find_element_by_link_text("stephany_viitoriia").click()
driver.find_element_by_link_text("stephany_viitoriia").click()
time.sleep(4)
driver.find_element_by_css_selector("#modal-profile-warning > div > div > div.flex.align-items-center > button.btn.bg-secondary.waves-effect.waves-light").click()
driver.find_element_by_css_selector("#main > div.container > div.center-align.pt-20 > a").click()
driver.find_element_by_css_selector("#dropdown-filter > div.filter-radio > div:nth-child(4) > label > span").click()
driver.find_element_by_css_selector("#dropdown-filter > div:nth-child(2) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#main > div.container > div.row.flex.flex-wrap.list-promotions > div:nth-child(3) > div > div.btn-action > a").click()