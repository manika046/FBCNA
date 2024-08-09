import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../.venv/.env')
load_dotenv(dotenv_path=env_path)

Firstname = os.getenv("first_name").split(',')
Lastname = os.getenv("last_name").split(',')
Password = os.getenv("password").split(',')

driver = webdriver.Chrome()

# def CreateNewAccount(driver):
driver.get("https://www.facebook.com/")
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
time.sleep(5)

F_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
F_name.send_keys(random.choice(Firstname))
time.sleep(5)

L_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
L_name.send_keys(random.choice(Lastname))
time.sleep(5)

pw_element = driver.find_element(By.XPATH, "//input[@name='reg_passwd__']")
pw_element.send_keys(random.choice(Password))
time.sleep(2)

# Create_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@id='u_0_0_lS']"))
# )
# Create_button.click()
# time.sleep(5)
# create_button = driver.find_element(By.XPATH, "//a[@id='u_0_0_lS']")
# create_button.click()

# CreateNewAccount(driver)
