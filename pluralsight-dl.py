from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
import re, os
from pathlib import Path
from creds import USERNAME, PASSWORD, COURSE_TITLE, PS_LIB_URL


driver = Firefox()
driver.get(PS_LIB_URL)

driver.find_element_by_id('Username').send_keys(USERNAME)
driver.find_element_by_id('Password').send_keys(PASSWORD)
driver.find_element_by_id('login').click()

main = driver.find_element_by_link_text(COURSE_TITLE)
Path(COURSE_TITLE).mkdir(parents=True, exist_ok=True)
os.chdir(COURSE_TITLE)
driver.get(main.get_attribute("href"))

driver.find_element_by_xpath("//button[.='Expand All']").click()