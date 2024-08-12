import ast
import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../.venv/.env')
load_dotenv(dotenv_path=env_path)

# converting string into python object
first_names = ast.literal_eval(os.getenv("first_name"))
last_names = ast.literal_eval(os.getenv("last_name"))
# passwords = ast.literal_eval(os.getenv("password"))

Firstname = random.choice(first_names)
Lastname = random.choice(last_names)
# Password = random.choice(passwords)

driver = webdriver.Chrome()

# def CreateNewAccount(driver):
driver.get("https://www.facebook.com/")
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
time.sleep(5)

F_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
F_name.send_keys(Firstname)
time.sleep(2)

L_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
L_name.send_keys(Lastname)
time.sleep(2)

MN_element = driver.find_element(By.XPATH, "//input[@name='reg_email__']")
MN_element.send_keys(os.getenv("Email"))
time.sleep(2)

# driver.implicitly_wait(10)

MNC_element = driver.find_element(By.XPATH, "//input[@name='reg_email_confirmation__']")
MNC_element.send_keys(os.getenv("Email"))
time.sleep(2)

pw_element = driver.find_element(By.XPATH, "//input[@name='reg_passwd__']")
pw_element.send_keys("Hello@123")
time.sleep(2)

dropdown = Select(driver.find_element(By.ID,"day"))
dropdown.select_by_value("20")

time.sleep(1)

dropdown = Select(driver.find_element(By.ID,"month"))
dropdown.select_by_value("10")

time.sleep(1)

dropdown = Select(driver.find_element(By.ID,"year"))
dropdown.select_by_value("1999")
time.sleep(1)

radio_button = driver.find_element(By.XPATH, "//input[@value='2']")
radio_button.click()
time.sleep(5)

signup_button = driver.find_element(By.NAME, "websubmit")
signup_button.click()
time.sleep(10)

print("Account Created Successfully")

driver.switch_to.window(driver.current_window_handle)
time.sleep(20)

# Create_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@id='u_0_0_lS']"))
# )
# Create_button.click()
# time.sleep(5)
# create_button = driver.find_element(By.XPATH, "//a[@id='u_0_0_lS']")
# create_button.click()

# CreateNewAccount(driver)
