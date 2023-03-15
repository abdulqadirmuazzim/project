# from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create your tests here.
web = webdriver.Edge()

web.get("http://127.0.0.1:8000/products")
time.sleep(3)
var = web.find_element(By.LINK_TEXT, "Products")
var.click()

time.sleep(3)
var2 = web.find_element(By.LINK_TEXT, "Home")
var2.click()

time.sleep(3)
var3 = web.find_element(By.LINK_TEXT, "Apis")
var3.click()

time.sleep(3)
web.quit()
